#!/usr/bin/env python3
"""Run portable structural checks on a standalone Chief Editor HTML report."""

from __future__ import annotations

import argparse
import json
import re
from html.parser import HTMLParser
from pathlib import Path


REQUIRED_IDS = {"scope", "movement", "drivers", "actions", "methodology"}
REQUIRED_MODULES = {"page-scorecard", "core-pillar-comparison"}
REQUIRED_READING_PATH = ["scope", "movement", "drivers", "actions"]
SECRET_PATTERNS = {
    "apify_token": re.compile(r"apify_api_[A-Za-z0-9_-]+", re.I),
    "bearer_token": re.compile(r"Bearer\s+[A-Za-z0-9._~-]{16,}", re.I),
    "private_key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
}


class ReportParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.ids: set[str] = set()
        self.images: list[dict[str, str]] = []
        self.links: list[str] = []
        self.modules: set[str] = set()
        self.section_ids: list[str] = []
        self.title_depth = 0
        self.title_text: list[str] = []
        self.h1_count = 0
        self.default_language = ""
        self.language_toggle = False
        self.language_options: set[str] = set()
        self.bilingual_script = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = {key: value or "" for key, value in attrs}
        keys = {key for key, _ in attrs}
        if values.get("id"):
            self.ids.add(values["id"])
            if tag == "section":
                self.section_ids.append(values["id"])
        if values.get("data-module"):
            self.modules.add(values["data-module"])
        if tag == "body":
            self.default_language = values.get("data-default-language", "")
        if "data-language-toggle" in keys:
            self.language_toggle = True
        if values.get("data-lang-option"):
            self.language_options.add(values["data-lang-option"])
        if tag == "script" and "data-bilingual-report" in keys:
            self.bilingual_script = True
        if tag == "img":
            self.images.append({"src": values.get("src", ""), "alt": values.get("alt", "")})
        if tag == "a" and values.get("href"):
            self.links.append(values["href"])
        if tag == "title":
            self.title_depth += 1
        if tag == "h1":
            self.h1_count += 1

    def handle_endtag(self, tag: str) -> None:
        if tag == "title" and self.title_depth:
            self.title_depth -= 1

    def handle_data(self, data: str) -> None:
        if self.title_depth:
            self.title_text.append(data)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("report", type=Path)
    parser.add_argument("--receipt", type=Path)
    args = parser.parse_args()

    text = args.report.read_text(encoding="utf-8")
    tree = ReportParser()
    tree.feed(text)
    checks = {
        "has_title": bool("".join(tree.title_text).strip()),
        "one_h1": tree.h1_count == 1,
        "required_sections": not (REQUIRED_IDS - tree.ids),
        "standard_performance_modules": not (REQUIRED_MODULES - tree.modules),
        "data_first_reading_path": [
            section_id
            for section_id in tree.section_ids
            if section_id in REQUIRED_READING_PATH
        ]
        == REQUIRED_READING_PATH
        and (
            "decisions" not in tree.section_ids
            or tree.section_ids.index("drivers")
            < tree.section_ids.index("decisions")
            < tree.section_ids.index("actions")
        ),
        "bilingual_language_switch": (
            tree.default_language == "en"
            and tree.language_toggle
            and tree.language_options == {"en", "zh"}
            and tree.bilingual_script
        ),
        "no_unresolved_template_tokens": not re.search(r"\{\{[^{}]+\}\}", text),
        "images_embedded": all(item["src"].startswith("data:image/") for item in tree.images),
        "images_have_alt": all(bool(item["alt"].strip()) for item in tree.images),
        "facebook_evidence_links": any(
            link.startswith("https://www.facebook.com/") for link in tree.links
        ),
        "no_secrets": not any(pattern.search(text) for pattern in SECRET_PATTERNS.values()),
        "no_agent_instructions": not re.search(
            r"(?:system prompt|agent instruction|tell the agent|you are an ai)", text, re.I
        ),
    }
    receipt = {
        "status": "PASS" if all(checks.values()) else "FAIL",
        "checks": checks,
        "missing_section_ids": sorted(REQUIRED_IDS - tree.ids),
        "missing_module_ids": sorted(REQUIRED_MODULES - tree.modules),
        "section_order": tree.section_ids,
        "image_count": len(tree.images),
        "facebook_link_count": sum(
            link.startswith("https://www.facebook.com/") for link in tree.links
        ),
        "report_bytes": args.report.stat().st_size,
        "note": "Run rendered desktop/mobile inspection separately; this script checks portable structure only.",
    }
    output = json.dumps(receipt, ensure_ascii=False, indent=2) + "\n"
    if args.receipt:
        args.receipt.parent.mkdir(parents=True, exist_ok=True)
        args.receipt.write_text(output, encoding="utf-8")
    print(output, end="")
    return 0 if receipt["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
