#!/usr/bin/env python3
"""Search Google Images through Serper and emit normalized results."""

import argparse
import json
import os
import sys
from typing import Any, Callable, Dict, List, Optional
from urllib.request import Request, urlopen


SERPER_IMAGES_URL = "https://google.serper.dev/images"


def search_images(
    query: str,
    *,
    api_key: str,
    limit: int = 10,
    gl: str = "hk",
    hl: str = "zh-tw",
    opener: Callable[..., Any] = urlopen,
) -> List[Dict[str, Any]]:
    """Submit an image query and return normalized, unique candidates."""
    query = query.strip()
    api_key = api_key.strip()
    if not query:
        raise ValueError("query must not be empty")
    if not api_key:
        raise ValueError("SERPER_API_KEY must not be empty")
    if limit <= 0:
        raise ValueError("limit must be greater than zero")

    payload = json.dumps({"q": query, "gl": gl, "hl": hl}).encode("utf-8")
    request = Request(
        SERPER_IMAGES_URL,
        data=payload,
        headers={
            "X-API-KEY": api_key,
            "Content-Type": "application/json",
        },
        method="POST",
    )

    with opener(request, timeout=30) as response:
        body = json.loads(response.read().decode("utf-8"))

    raw_images = body.get("images")
    if not isinstance(raw_images, list):
        raise ValueError("Serper response did not include an images list")

    results: List[Dict[str, Any]] = []
    seen_urls = set()
    for item in raw_images:
        if not isinstance(item, dict):
            continue
        image_url = item.get("imageUrl")
        if not isinstance(image_url, str) or not image_url or image_url in seen_urls:
            continue
        seen_urls.add(image_url)
        results.append(
            {
                "rank": len(results) + 1,
                "title": item.get("title"),
                "image_url": image_url,
                "thumbnail_url": item.get("thumbnailUrl"),
                "source": item.get("source"),
                "source_url": item.get("link"),
                "width": item.get("imageWidth"),
                "height": item.get("imageHeight"),
            }
        )
        if len(results) >= limit:
            break

    return results


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Search Google Images through Serper and return normalized JSON."
    )
    parser.add_argument("--query", required=True, help="Image-search query")
    parser.add_argument("--limit", type=int, default=10, help="Maximum results")
    parser.add_argument("--gl", default="hk", help="Serper country code")
    parser.add_argument("--hl", default="zh-tw", help="Serper language code")
    return parser


def main(argv: Optional[List[str]] = None) -> int:
    args = build_parser().parse_args(argv)
    api_key = os.environ.get("SERPER_API_KEY", "")
    try:
        images = search_images(
            args.query,
            api_key=api_key,
            limit=args.limit,
            gl=args.gl,
            hl=args.hl,
        )
    except Exception as exc:
        print(f"Image search failed: {exc}", file=sys.stderr)
        return 1

    print(json.dumps({"query": args.query, "images": images}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
