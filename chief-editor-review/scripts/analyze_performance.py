#!/usr/bin/env python3
"""Compute portable quantitative evidence for a Chief Editor review."""

from __future__ import annotations

import argparse
import json
import math
import statistics
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any, Iterable
from zoneinfo import ZoneInfo


AD_STATUSES = {
    "ad",
    "boosted",
    "confirmed_ad",
    "declared_paid_partnership",
    "paid",
    "paid_partnership",
    "sponsored",
}


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def number(value: Any) -> float | None:
    if value is None or isinstance(value, bool):
        return None
    try:
        result = float(value)
    except (TypeError, ValueError):
        return None
    return result if math.isfinite(result) else None


def metric_summary(values: Iterable[Any]) -> dict[str, int | float | None]:
    clean = [item for value in values if (item := number(value)) is not None]
    return {
        "coverage": len(clean),
        "median": statistics.median(clean) if clean else None,
        "total": sum(clean) if clean else None,
        "average": statistics.fmean(clean) if clean else None,
    }


def parse_time(value: str, timezone: ZoneInfo) -> datetime:
    observed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if observed.tzinfo is None:
        observed = observed.replace(tzinfo=timezone)
    return observed.astimezone(timezone)


def percentile_score(value: float, peer_values: list[float]) -> float:
    fewer = sum(peer < value for peer in peer_values)
    tied = sum(peer == value for peer in peer_values)
    return 100.0 * (fewer + 0.5 * tied) / len(peer_values)


def cohort(score: float) -> str:
    if score < 100 / 3:
        return "bottom"
    if score < 200 / 3:
        return "middle"
    return "top"


def rounded(value: Any) -> Any:
    return round(value, 2) if isinstance(value, float) else value


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", required=True, type=Path)
    parser.add_argument("--posts", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    manifest = load_json(args.manifest)
    posts = load_json(args.posts)
    timezone = ZoneInfo(str(manifest["timezone"]))
    focal = manifest["focal_page"]
    focal_page = focal.get("name") if isinstance(focal, dict) else focal
    primary_kpi = str(manifest.get("primary_kpi") or "shares")

    enriched: list[dict[str, Any]] = []
    excluded_ads: Counter[str] = Counter()
    for post in posts:
        row = dict(post)
        page = str(row.get("page") or "")
        row["_observed"] = parse_time(str(row["published_at"]), timezone)
        row["month"] = row["_observed"].strftime("%Y-%m")
        row["is_ad"] = str(row.get("ad_status") or "unknown").casefold() in AD_STATUSES
        if row["is_ad"]:
            excluded_ads[page] += 1
        else:
            enriched.append(row)

    monthly_groups: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    for row in enriched:
        monthly_groups[(str(row.get("page") or ""), row["month"])].append(row)

    monthly = []
    for (page, month), rows in sorted(monthly_groups.items()):
        shares = [row.get("shares") for row in rows]
        clean_shares = sorted(
            (value for raw in shares if (value := number(raw)) is not None), reverse=True
        )
        top_count = max(1, math.ceil(len(clean_shares) * 0.1)) if clean_shares else 0
        total_shares = sum(clean_shares)
        monthly.append(
            {
                "page": page,
                "month": month,
                "post_count": len(rows),
                "shares": metric_summary(shares),
                "reactions": metric_summary(row.get("reactions") for row in rows),
                "comments": metric_summary(row.get("comments") for row in rows),
                "primary_kpi": metric_summary(row.get(primary_kpi) for row in rows),
                "top_10_percent_share_contribution": (
                    sum(clean_shares[:top_count]) / total_shares if total_shares else None
                ),
            }
        )

    comparison_groups: dict[tuple[str, str, str], list[dict[str, Any]]] = defaultdict(list)
    for row in enriched:
        comparison_groups[
            (
                str(row.get("page") or ""),
                str(row.get("pillar") or "Unclassified"),
                str(row.get("format") or "Unknown"),
            )
        ].append(row)

    ranked_posts = []
    timing_rows = []
    for (page, pillar, post_format), rows in sorted(comparison_groups.items()):
        values = [value for row in rows if (value := number(row.get("shares"))) is not None]
        if not values:
            continue
        for row in rows:
            value = number(row.get("shares"))
            if value is None:
                continue
            score = percentile_score(value, values)
            ranked_posts.append(
                {
                    "post_id": row.get("post_id"),
                    "page": page,
                    "month": row["month"],
                    "pillar": pillar,
                    "format": post_format,
                    "shares": value,
                    "within_pillar_format_score": score,
                    "cohort": cohort(score),
                    "peer_post_count": len(values),
                }
            )
            if page == focal_page and len(values) >= 5:
                timing_rows.append((row, score, pillar, post_format, len(values)))

    daily_volume: Counter[str] = Counter(
        row["_observed"].strftime("%Y-%m-%d") for row in enriched if row.get("page") == focal_page
    )
    timing_buckets: dict[tuple[str, str], list[float]] = defaultdict(list)
    for row, score, pillar, post_format, group_size in timing_rows:
        observed = row["_observed"]
        timing_buckets[("hour", f"{observed.hour:02d}:00")].append(score)
        timing_buckets[("weekday", observed.strftime("%A"))].append(score)
        timing_buckets[("daily_posting_volume", str(daily_volume[observed.strftime("%Y-%m-%d")]))].append(score)
        timing_buckets[("eligible_group", f"{pillar} | {post_format} | n={group_size}")].append(score)

    timing = [
        {
            "dimension": dimension,
            "value": value,
            "post_count": len(scores),
            "median_share_score": statistics.median(scores),
        }
        for (dimension, value), scores in sorted(timing_buckets.items())
    ]

    result = {
        "scope": {
            "date_start": manifest.get("date_start"),
            "date_end": manifest.get("date_end"),
            "timezone": str(timezone),
            "focal_page": focal_page,
            "primary_kpi": primary_kpi,
        },
        "organic_post_count": len(enriched),
        "confirmed_ads_excluded_by_page": dict(excluded_ads),
        "monthly_by_page": monthly,
        "ranked_posts": ranked_posts,
        "timing_frequency": timing,
        "timing_score_definition": "100 × (posts with fewer shares + half the tied posts) ÷ group size",
    }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, default=rounded) + "\n",
        encoding="utf-8",
    )
    print(json.dumps({"status": "PASS", "output": str(args.output), "organic_posts": len(enriched)}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
