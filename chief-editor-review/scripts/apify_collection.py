#!/usr/bin/env python3
"""Run and recover bounded Apify collections without persisting credentials."""

from __future__ import annotations

import argparse
import getpass
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any


API_ROOT = "https://api.apify.com/v2"
TERMINAL = {"SUCCEEDED", "FAILED", "TIMED-OUT", "ABORTED"}
RECEIPT_FIELDS = (
    "id",
    "actId",
    "status",
    "startedAt",
    "finishedAt",
    "usageTotalUsd",
    "defaultDatasetId",
    "exitCode",
)


def token_from_secret_source() -> str:
    token = os.environ.get("APIFY_TOKEN", "").strip()
    if token:
        return token
    token = (getpass.getpass("") if sys.stdin.isatty() else sys.stdin.readline()).strip()
    if not token:
        raise RuntimeError("No Apify token supplied through APIFY_TOKEN or hidden stdin")
    return token


def request_json(
    url: str,
    token: str,
    *,
    method: str = "GET",
    payload: Any | None = None,
    timeout: int = 90,
) -> Any:
    data = None if payload is None else json.dumps(payload).encode("utf-8")
    request = urllib.request.Request(
        url,
        data=data,
        method=method,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "User-Agent": "Chief-Editor-Review/1.0",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return json.load(response)
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", "replace")[:1000]
        raise RuntimeError(f"Apify HTTP {exc.code}: {body}") from exc


def safe_run(run: dict[str, Any]) -> dict[str, Any]:
    return {field: run.get(field) for field in RECEIPT_FIELDS}


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def get_run(run_id: str, token: str) -> dict[str, Any]:
    return request_json(f"{API_ROOT}/actor-runs/{run_id}", token)["data"]


def get_dataset_count(dataset_id: str, token: str) -> int:
    data = request_json(f"{API_ROOT}/datasets/{dataset_id}", token)["data"]
    return int(data.get("itemCount") or 0)


def fetch_dataset(dataset_id: str, token: str, *, page_size: int = 1000) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    offset = 0
    while True:
        query = urllib.parse.urlencode(
            {"clean": "true", "format": "json", "offset": offset, "limit": page_size}
        )
        page = request_json(
            f"{API_ROOT}/datasets/{dataset_id}/items?{query}", token, timeout=240
        )
        if not isinstance(page, list):
            raise RuntimeError("Apify dataset response was not a JSON array")
        rows.extend(page)
        if len(page) < page_size:
            break
        offset += len(page)
    return rows


def wait_for_run(run_id: str, token: str, poll_seconds: float) -> dict[str, Any]:
    while True:
        run = get_run(run_id, token)
        status = run.get("status")
        print(
            json.dumps(
                {"run_id": run_id, "status": status, "cost_usd": run.get("usageTotalUsd")}
            ),
            flush=True,
        )
        if status in TERMINAL:
            return run
        time.sleep(poll_seconds)


def save_completed_run(
    run: dict[str, Any], token: str, output: Path, receipt: Path
) -> dict[str, Any]:
    if run.get("status") != "SUCCEEDED":
        raise RuntimeError(f"Run {run.get('id')} is {run.get('status')}, not SUCCEEDED")
    dataset_id = run.get("defaultDatasetId")
    if not dataset_id:
        raise RuntimeError("Completed run has no default dataset")
    rows = fetch_dataset(str(dataset_id), token)
    write_json(output, rows)
    saved_receipt = safe_run(run) | {"savedItemCount": len(rows)}
    write_json(receipt, saved_receipt)
    return {
        "run_id": run.get("id"),
        "saved_items": len(rows),
        "cost_usd": run.get("usageTotalUsd"),
        "output": os.fspath(output),
        "receipt": os.fspath(receipt),
    }


def command_run(args: argparse.Namespace) -> int:
    if args.max_charge <= 0:
        raise RuntimeError("--max-charge must be greater than zero")
    token = token_from_secret_source()
    actor_id = args.actor.replace("/", "~")
    actor_input = json.loads(args.input.read_text(encoding="utf-8"))
    query = urllib.parse.urlencode({"maxTotalChargeUsd": f"{args.max_charge:.2f}"})
    response = request_json(
        f"{API_ROOT}/acts/{actor_id}/runs?{query}", token, method="POST", payload=actor_input
    )
    run = response["data"]
    print(json.dumps({"run_id": run.get("id"), "status": run.get("status")}), flush=True)
    final = wait_for_run(str(run["id"]), token, args.poll_seconds)
    result = save_completed_run(final, token, args.output, args.receipt)
    print(json.dumps(result), flush=True)
    return 0


def command_status(args: argparse.Namespace) -> int:
    token = token_from_secret_source()
    run = get_run(args.run_id, token)
    dataset_id = run.get("defaultDatasetId")
    count = get_dataset_count(str(dataset_id), token) if dataset_id else 0
    print(json.dumps(safe_run(run) | {"datasetItemCount": count}), flush=True)
    return 0


def command_fetch(args: argparse.Namespace) -> int:
    token = token_from_secret_source()
    result = save_completed_run(get_run(args.run_id, token), token, args.output, args.receipt)
    print(json.dumps(result), flush=True)
    return 0


def command_abort(args: argparse.Namespace) -> int:
    token = token_from_secret_source()
    run = get_run(args.run_id, token)
    snapshot_items = None
    if args.snapshot:
        dataset_id = run.get("defaultDatasetId")
        if not dataset_id:
            raise RuntimeError("Run has no dataset to snapshot")
        rows = fetch_dataset(str(dataset_id), token)
        write_json(args.snapshot, rows)
        snapshot_items = len(rows)
    aborted = request_json(
        f"{API_ROOT}/actor-runs/{args.run_id}/abort?gracefully=true",
        token,
        method="POST",
        payload={},
    )["data"]
    print(
        json.dumps(
            {
                "run_id": args.run_id,
                "status_before_abort": run.get("status"),
                "abort_status": aborted.get("status"),
                "cost_usd_at_abort": run.get("usageTotalUsd"),
                "snapshot_items": snapshot_items,
                "snapshot": os.fspath(args.snapshot) if args.snapshot else None,
            }
        ),
        flush=True,
    )
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Bounded Apify collection helper. Supply APIFY_TOKEN securely or via hidden stdin."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    run_parser = subparsers.add_parser("run", help="Start, wait for, and save a bounded actor run")
    run_parser.add_argument("--actor", required=True, help="Actor ID, for example owner/actor")
    run_parser.add_argument("--input", required=True, type=Path, help="Credential-free actor input JSON")
    run_parser.add_argument("--output", required=True, type=Path)
    run_parser.add_argument("--receipt", required=True, type=Path)
    run_parser.add_argument("--max-charge", required=True, type=float)
    run_parser.add_argument("--poll-seconds", type=float, default=10.0)
    run_parser.set_defaults(handler=command_run)

    status_parser = subparsers.add_parser("status", help="Print redacted status and item count")
    status_parser.add_argument("--run-id", required=True)
    status_parser.set_defaults(handler=command_status)

    fetch_parser = subparsers.add_parser("fetch", help="Save an already completed run")
    fetch_parser.add_argument("--run-id", required=True)
    fetch_parser.add_argument("--output", required=True, type=Path)
    fetch_parser.add_argument("--receipt", required=True, type=Path)
    fetch_parser.set_defaults(handler=command_fetch)

    abort_parser = subparsers.add_parser("abort", help="Gracefully abort, optionally after a snapshot")
    abort_parser.add_argument("--run-id", required=True)
    abort_parser.add_argument("--snapshot", type=Path)
    abort_parser.set_defaults(handler=command_abort)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    try:
        return int(args.handler(args))
    except (OSError, ValueError, RuntimeError) as exc:
        print(json.dumps({"status": "ERROR", "error": str(exc)}), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
