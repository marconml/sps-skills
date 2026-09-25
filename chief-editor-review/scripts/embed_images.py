#!/usr/bin/env python3
"""Embed local report images referenced by data-embed-src as data URIs."""

from __future__ import annotations

import argparse
import base64
import mimetypes
import re
from pathlib import Path


ATTRIBUTE = re.compile(r'\sdata-embed-src=(?P<quote>["\'])(?P<path>.*?)(?P=quote)')


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--base-dir", type=Path)
    args = parser.parse_args()

    base_dir = (args.base_dir or args.input.parent).resolve()
    html = args.input.read_text(encoding="utf-8")
    embedded = 0

    def replace(match: re.Match[str]) -> str:
        nonlocal embedded
        relative = Path(match.group("path"))
        if relative.is_absolute():
            media = relative.resolve()
        else:
            media = (base_dir / relative).resolve()
        if not media.is_file():
            raise FileNotFoundError(f"Evidence image not found: {media}")
        mime, _ = mimetypes.guess_type(media.name)
        if not mime or not mime.startswith("image/"):
            raise ValueError(f"Unsupported evidence image type: {media}")
        encoded = base64.b64encode(media.read_bytes()).decode("ascii")
        embedded += 1
        return f' src="data:{mime};base64,{encoded}"'

    rendered = ATTRIBUTE.sub(replace, html)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(rendered, encoding="utf-8")
    print(f"embedded_images={embedded} output={args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
