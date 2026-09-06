#!/usr/bin/env python3
"""Validate a normalized Chief Editor Review evidence package."""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any


POST_REQUIRED = {"post_id", "page", "permalink", "published_at", "caption", "format", "ad_status"}
COMMENT_REQUIRED = {"post_id", "text", "is_page_authored"}
IDENTITY_FIELDS = {
    "author",
    "author_id",
    "author_name",
    "avatar",
    "commenter",
    "commenter_id",
    "name",
    "profile_url",
    "user_id",
    "user_name",
    "username",
}
AD_STATUSES = {
    "ad",
    "boosted",
    "confirmed_ad",
    "declared_paid_partnership",
    "paid",
    "paid_partnership",
    "sponsored",
}
UNKNOWN_AD_STATUSES = {"", "not_declared_paid_partnership", "unavailable", "unknown"}


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def parse_datetime(value: Any) -> datetime | None:
    if not isinstance(value, str) or not value.strip():
        return None
    candidate = value.strip().replace("Z", "+00:00")
    try:
        return datetime.fromisoformat(candidate)
    except ValueError:
        return None


def page_name(value: Any) -> str:
    if isinstance(value, dict):
        return str(value.get("name") or value.get("url") or "").strip()
    return str(value or "").strip()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", required=True, type=Path)
    parser.add_argument("--posts", required=True, type=Path)
    parser.add_argument("--comments", type=Path)
    parser.add_argument("--receipt", type=Path)
    args = parser.parse_args()

    manifest = load_json(args.manifest)
    posts = load_json(args.posts)
    comments = load_json(args.comments) if args.comments else []
    errors: list[str] = []
    warnings: list[str] = []

    for field in ("focal_page", "competitors", "date_start", "date_end", "timezone", "primary_kpi"):
        if field not in manifest:
            errors.append(f"manifest missing {field}")
    if not isinstance(posts, list):
        errors.append("posts must be a JSON array")
        posts = []
    if not isinstance(comments, list):
        errors.append("comments must be a JSON array")
        comments = []

    metric = str(manifest.get("primary_kpi") or "shares")
    start = None
    end = None
    try:
        start = (
            datetime.fromisoformat(str(manifest.get("date_start")))
            if manifest.get("date_start")
            else None
        )
        end = (
            datetime.fromisoformat(str(manifest.get("date_end")))
            if manifest.get("date_end")
            else None
        )
    except ValueError:
        errors.append("manifest dates must be valid ISO dates")
    if start and end and start > end:
        errors.append("manifest date_start is after date_end")
    approved_pages = {page_name(manifest.get("focal_page"))}
    approved_pages.update(page_name(item) for item in manifest.get("competitors", []))
    approved_pages.discard("")

    counts: Counter[str] = Counter()
    ads: Counter[str] = Counter()
    organic: Counter[str] = Counter()
    metric_missing: Counter[str] = Counter()
    reactions_missing: Counter[str] = Counter()
    comments_missing: Counter[str] = Counter()
    shares_missing: Counter[str] = Counter()
    media_missing: Counter[str] = Counter()
    unknown_ad: Counter[str] = Counter()
    ids: set[str] = set()

    for index, post in enumerate(posts):
        if not isinstance(post, dict):
            errors.append(f"post {index} is not an object")
            continue
        missing = POST_REQUIRED - post.keys()
        if missing:
            errors.append(f"post {index} missing {sorted(missing)}")
        post_id = str(post.get("post_id") or "")
        if post_id:
            if post_id in ids:
                warnings.append(f"duplicate post_id {post_id}")
            ids.add(post_id)
        page = str(post.get("page") or "")
        counts[page] += 1
        if approved_pages and page not in approved_pages:
            errors.append(f"post {post_id or index} has unapproved page {page!r}")
        observed = parse_datetime(post.get("published_at"))
        if observed is None:
            errors.append(f"post {post_id or index} has invalid published_at")
        elif start and end and not (start.date() <= observed.date() <= end.date()):
            errors.append(f"post {post_id or index} falls outside manifest dates")
        if post.get(metric) is None:
            metric_missing[page] += 1
        if post.get("reactions") is None:
            reactions_missing[page] += 1
        if post.get("comments") is None:
            comments_missing[page] += 1
        if post.get("shares") is None:
            shares_missing[page] += 1
        ad_status = str(post.get("ad_status") or "unknown").casefold()
        if ad_status in AD_STATUSES:
            ads[page] += 1
        else:
            organic[page] += 1
            if ad_status in UNKNOWN_AD_STATUSES:
                unknown_ad[page] += 1
        if not post.get("media_path"):
            media_missing[page] += 1

    comment_counts: Counter[str] = Counter()
    page_reply_counts: Counter[str] = Counter()
    pm_cta_comments = 0
    for index, comment in enumerate(comments):
        if not isinstance(comment, dict):
            errors.append(f"comment {index} is not an object")
            continue
        missing = COMMENT_REQUIRED - comment.keys()
        if missing:
            errors.append(f"comment {index} missing {sorted(missing)}")
        leaked = sorted(IDENTITY_FIELDS & {str(key).casefold() for key in comment})
        if leaked:
            errors.append(f"comment {index} contains identity fields {leaked}")
        post_id = str(comment.get("post_id") or "")
        if post_id and post_id not in ids:
            warnings.append(f"comment {index} references unknown post_id {post_id}")
        comment_counts[post_id] += 1
        if comment.get("is_page_authored") is True:
            page_reply_counts[post_id] += 1
        if comment.get("is_pm_cta") is True:
            pm_cta_comments += 1

    comment_limit = int(
        (manifest.get("comments") or {}).get("max_ranked_top_level_per_post", 20)
    )
    over_limit = {post_id: count for post_id, count in comment_counts.items() if count > comment_limit}
    if over_limit:
        warnings.append(f"comment cap exceeded for {len(over_limit)} posts")
    if pm_cta_comments:
        warnings.append(f"{pm_cta_comments} PM-CTA comments remain and must be excluded from insight")

    coverage: dict[str, dict[str, int]] = defaultdict(dict)
    for page in sorted(set(counts) | approved_pages):
        coverage[page] = {
            "collected_posts": counts[page],
            "confirmed_ads_excluded": ads[page],
            "organic_analysis_posts": organic[page],
            "missing_primary_kpi": metric_missing[page],
            "missing_reactions": reactions_missing[page],
            "missing_comments": comments_missing[page],
            "missing_shares": shares_missing[page],
            "missing_media": media_missing[page],
            "unknown_ad_status": unknown_ad[page],
        }

    incomplete_metrics = any(
        counter
        for counter in (
            metric_missing,
            reactions_missing,
            comments_missing,
            shares_missing,
        )
    )
    status = "blocked" if errors else ("partial" if warnings or incomplete_metrics else "ready")
    receipt = {
        "status": status,
        "primary_kpi": metric,
        "date_start": manifest.get("date_start"),
        "date_end": manifest.get("date_end"),
        "timezone": manifest.get("timezone"),
        "coverage_by_page": coverage,
        "comments": {
            "rows": len(comments),
            "posts": len(comment_counts),
            "page_authored_rows": sum(page_reply_counts.values()),
            "pm_cta_rows_remaining": pm_cta_comments,
            "cap": comment_limit,
        },
        "errors": errors,
        "warnings": sorted(set(warnings)),
    }
    output = json.dumps(receipt, ensure_ascii=False, indent=2) + "\n"
    if args.receipt:
        args.receipt.parent.mkdir(parents=True, exist_ok=True)
        args.receipt.write_text(output, encoding="utf-8")
    print(output, end="")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
