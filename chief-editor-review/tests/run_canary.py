#!/usr/bin/env python3
"""Exercise evidence validation, image embedding, and report validation offline."""

from __future__ import annotations

import argparse
import importlib.util
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "tests" / "fixtures"


def run(*args: str) -> None:
    subprocess.run([sys.executable, *args], check=True)


def run_canary(output_dir: Path) -> None:
    spec = importlib.util.spec_from_file_location(
        "chief_editor_review_analysis", ROOT / "scripts" / "analyze_performance.py"
    )
    assert spec and spec.loader
    analysis = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(analysis)
    assert analysis.percentile_score(2, [1, 2, 2, 3]) == 50
    assert analysis.number(None) is None
    output_dir.mkdir(parents=True, exist_ok=True)
    run(
        str(ROOT / "scripts" / "validate_evidence.py"),
        "--manifest",
        str(FIXTURES / "manifest.json"),
        "--posts",
        str(FIXTURES / "posts.json"),
        "--comments",
        str(FIXTURES / "comments.json"),
        "--receipt",
        str(output_dir / "evidence-receipt.json"),
    )
    evidence_receipt = json.loads(
        (output_dir / "evidence-receipt.json").read_text(encoding="utf-8")
    )
    assert evidence_receipt["status"] == "ready"
    assert (
        evidence_receipt["coverage_by_page"]["Example Health"]["confirmed_ads_excluded"]
        == 1
    )
    assert evidence_receipt["comments"]["pm_cta_rows_remaining"] == 0
    run(
        str(ROOT / "scripts" / "analyze_performance.py"),
        "--manifest",
        str(FIXTURES / "manifest.json"),
        "--posts",
        str(FIXTURES / "posts.json"),
        "--output",
        str(output_dir / "performance.json"),
    )
    performance = json.loads(
        (output_dir / "performance.json").read_text(encoding="utf-8")
    )
    assert performance["organic_post_count"] == 2
    assert performance["confirmed_ads_excluded_by_page"]["Example Health"] == 1

    hook_case = json.loads(
        (FIXTURES / "hook-evidence-case.json").read_text(encoding="utf-8")
    )
    tiers = {post["tier"] for post in hook_case["posts"]}
    proposal = hook_case["proposal_evidence"]
    assert {"high", "middle", "low"}.issubset(tiers)
    assert hook_case["duplicates_resolved"] is True
    assert proposal["packaging_basis"] == "comparable_high_middle_low"
    assert proposal["claim_basis"] == "approved source"
    assert proposal["surface_phrase_is_formula"] is False
    assert all(comment["allowed_role"] == "content_need" for comment in hook_case["comments"])

    template = (ROOT / "assets" / "chief-editor-report-template.html").read_text(
        encoding="utf-8"
    )
    values = {
        "REPORT_TITLE": "Canary Chief Editor Review",
        "REPORT_LABEL": "CANARY · AUGUST 2026 FACEBOOK REVIEW",
        "MONTH_STATUS_HEADLINE": "August improved, but one mechanism did most of the work.",
        "MONTH_STATUS_DECK": "Synthetic content validates the data-to-diagnosis-to-action path.",
        "HERO_EVIDENCE_ANCHOR": "Median shares and post counts remain visible.",
        "DECISION_MONTH": "Decision month · August 2026",
        "CONTEXT_MONTHS": "June–July · context",
        "PRIMARY_KPI": "Primary KPI · shares",
        "PAGE_SCOPE": "Example Health + 1 comparator",
        "OBJECTIVE": "Earn more useful shares per post.",
        "AUDIENCE": "Synthetic test audience.",
        "REVIEW_BASIS": "August decision; June and July context.",
        "DECISION_USE": "Commissioning and packaging.",
        "SOCIAL_POST_URL": "https://www.facebook.com/example.health/posts/example-1",
        "LOCAL_IMAGE_PATH": str(FIXTURES / "evidence.svg"),
        "IMAGE_ALT": "Synthetic canary evidence",
        "SOURCE_LANGUAGE": "en",
        "SOURCE_HOOK": "A practical choice readers can use",
        "SHARES": "42",
        "REACTIONS": "108",
        "COMMENTS": "9",
        "POST_DATE": "12 Aug 2026",
        "FORMAT": "Image",
        "MONTHLY_CHART_SVG": '<svg viewBox="0 0 600 160" role="img" aria-label="Canary monthly median shares"><polyline points="30,120 300,90 570,55" fill="none" stroke="#087f83" stroke-width="5"/></svg>',
        "CORE_PILLAR_COMPARISON_HTML": "<table><tr><th>Core pillar</th></tr><tr><td>三高管理</td></tr></table>",
        "MOVEMENT_HEADLINE": "Start with what changed.",
        "MOVEMENT_TAKEAWAY": "August is the decision month; June and July provide context.",
        "FOCAL_MOVEMENT_TITLE": "The typical post improved.",
        "FOCAL_MOVEMENT": "Median shares rose while output remained visible.",
        "MARKET_MOVEMENT_TITLE": "The comparator also moved.",
        "MARKET_MOVEMENT": "The shared movement keeps the news cycle in view.",
        "DRIVERS_HEADLINE": "Diagnose the editorial choices behind the movement.",
        "DRIVERS_TAKEAWAY": "The case illustrates a complete synthetic cohort finding.",
        "MECHANISM_ANALYSIS": "A cohort-level editorial difference comes before its references.",
        "MECHANISM_REFERENCE_LINKS_HTML": '<div class="reference-links"><a href="https://www.facebook.com/example.health/posts/reference-1">Reference one</a><a href="https://www.facebook.com/comparator.health/posts/reference-2">Reference two</a></div>',
        "MECHANISM_EVIDENCE_ANCHOR": "Synthetic cohort evidence anchor.",
        "FOCAL_OVERVIEW_TITLE": "One mechanism carried the month.",
        "FOCAL_OVERVIEW": "The complete focal-page set identifies the largest driver and drag before the case evidence.",
        "FOCAL_OVERVIEW_EVIDENCE": "Synthetic high, middle, and low cohorts.",
        "COMPETITOR_OVERVIEW_TITLE": "The material comparison gap is diagnosed.",
        "COMPETITOR_OVERVIEW": "Like-for-like cohorts and Page-native territories explain what management should notice.",
        "COMPETITOR_OVERVIEW_EVIDENCE": "The unresolved residual remains labelled.",
        "ACTIONS_HEADLINE": "Turn the diagnosis into one action layer.",
        "ACTIONS_TAKEAWAY": "Every Scale, Improve, Stop, or Test call belongs here.",
        "METHODOLOGY": "Synthetic evidence only. No credentials or identities.",
        "ZH_TRANSLATION_JSON": json.dumps(
            {
                "Canary Chief Editor Review": "Canary Chief Editor 中文檢討",
                "August improved, but one mechanism did most of the work.": "八月有改善，但主要由一個內容機制帶動。",
                "Synthetic content validates the data-to-diagnosis-to-action path.": "合成內容用於驗證由數據、診斷到行動的閱讀流程。",
            },
            ensure_ascii=False,
        ),
    }

    def replace(match: re.Match[str]) -> str:
        key = match.group(1)
        return values.get(key, key.replace("_", " ").title())

    draft = re.sub(r"\{\{([A-Z0-9_]+)\}\}", replace, template)
    draft_path = output_dir / "draft.html"
    draft_path.write_text(draft, encoding="utf-8")
    report_path = output_dir / "report.html"
    run(
        str(ROOT / "scripts" / "embed_images.py"),
        "--input",
        str(draft_path),
        "--output",
        str(report_path),
    )
    run(
        str(ROOT / "scripts" / "validate_report.py"),
        str(report_path),
        "--receipt",
        str(output_dir / "report-receipt.json"),
    )
    report_receipt = json.loads(
        (output_dir / "report-receipt.json").read_text(encoding="utf-8")
    )
    assert report_receipt["status"] == "PASS"
    assert report_receipt["image_count"] == 1
    assert report_receipt["checks"]["standard_performance_modules"] is True
    assert report_receipt["checks"]["data_first_reading_path"] is True
    assert report_receipt["checks"]["bilingual_language_switch"] is True
    assert "decisions" not in report_receipt["section_order"]
    report_text = report_path.read_text(encoding="utf-8")
    assert "三高管理" in report_text
    assert "Blood Pressure, Glucose &amp; Lipids" not in report_text
    assert report_text.index("One mechanism carried the month.") < report_text.index(
        "A practical choice readers can use"
    )
    assert report_text.index("The material comparison gap is diagnosed.") < report_text.index(
        "Competitor Diagnosis Title"
    )
    assert report_text.index("A cohort-level editorial difference comes before its references.") < report_text.index(
        "Reference one"
    ) < report_text.index("Synthetic cohort evidence anchor.")

    instagram_path = output_dir / "instagram-report.html"
    instagram_path.write_text(
        report_text.replace("https://www.facebook.com/", "https://www.instagram.com/"),
        encoding="utf-8",
    )
    run(
        str(ROOT / "scripts" / "validate_report.py"),
        str(instagram_path),
        "--receipt",
        str(output_dir / "instagram-report-receipt.json"),
    )
    instagram_receipt = json.loads(
        (output_dir / "instagram-report-receipt.json").read_text(encoding="utf-8")
    )
    assert instagram_receipt["status"] == "PASS"
    assert instagram_receipt["checks"]["social_evidence_links"] is True


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path)
    args = parser.parse_args()
    if args.output_dir:
        run_canary(args.output_dir)
    else:
        with tempfile.TemporaryDirectory(prefix="chief-editor-review-canary-") as temp:
            run_canary(Path(temp))
    print("chief-editor-review canary: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
