# Collection Contract

Read this reference whenever evidence must be checked, imported, refreshed, or collected.

## Collection request

Record a credential-free run manifest before collection:

```json
{
  "focal_page": "Page name and URL",
  "competitors": ["Approved page names and URLs"],
  "excluded_pages": [],
  "date_start": "YYYY-MM-DD",
  "date_end": "YYYY-MM-DD",
  "timezone": "Asia/Hong_Kong",
  "decision_month": "YYYY-MM",
  "primary_kpi": "shares",
  "pillars": [{"name": "Pillar", "tags": []}],
  "report_language": "English",
  "comments": {"enabled": true, "max_ranked_top_level_per_post": 20, "exclude_pm_cta_posts": true},
  "ad_rule": "Authoritative field or approved classification rule",
  "maximum_approved_cost_usd": 0
}
```

The user confirms business scope in plain language. Actor IDs and provider-specific inputs belong in a separate local collection plan, never in the report.

## Access

Check existing approved access without revealing secrets. Never ask anyone to paste credentials in chat or request competitors' credentials. When access is unavailable, give the user this forwarding message:

> Please arrange approved access for a three-month Facebook review of our page and selected competitors, or provide exported posts, metrics, downloaded images, and our page's comments and replies. Configure access securely for Codex and confirm collection costs.

Test access with the smallest useful canary. For paid collection, record the approved ceiling and pass it to the provider as an enforceable charge limit when available.

## Required post evidence

For every page and eligible publication in the exact period, seek:

- stable post ID and direct permalink;
- page identity;
- full caption and first-line hook;
- publication timestamp and confirmed timezone;
- content format;
- original media URL and downloaded local media when accessible;
- reactions, comments, shares, and the selected KPI;
- authoritative promotion/ad status or `unknown`;
- source and field-level coverage flags.

Public engagement is not reach or an engagement rate. Do not infer an unavailable denominator.

## Ads and reposts

Record every collected occurrence. Exclude confirmed ads and paid partnerships from organic performance analysis while retaining numeric counts by page. Unknown ad status remains visible as a limitation.

Preserve exact and materially identical reposts for page-level totals. Flag caption-and-media identity so the analysis can avoid treating unchanged creative as a creative contrast.

## Comments

Comments are collected only from the focal page unless the user approves another lawful scope. Identify PM-CTA posts from the post/caption/Page-reply pattern before collecting comments where possible; exclude those posts from newsroom comment insight.

For each remaining post, retain at most the approved number of ranked top-level comments, default 20. Keep comment text, likes/rank where available, post ID, and Page-authored status. Remove commenter name, username, profile URL, avatar, user ID, and other identity fields. Preserve missing rank/like values as missing.

## Run layout and receipt

Use a new directory so previous reports and evidence remain intact:

```text
runs/<run-id>/
  manifest.json
  collection-plan.json
  raw/posts.json
  raw/comments.json
  normalized/posts.json
  normalized/comments-deidentified.json
  media/
  receipts/posts.json
  receipts/comments.json
  coverage.json
```

Receipts may contain run ID, actor ID, terminal status, start/finish time, cost, dataset ID, item count, and output path. Exclude tokens, request headers, signed URLs, and user identities.

Return one status:

- `ready`: required coverage passed and analysis may begin.
- `partial`: usable evidence exists but named gaps constrain findings.
- `blocked`: required access, approval, budget, or evidence is absent.

Exports may proceed as `partial` when the user accepts their stated missing coverage. Never silently supplement them with unapproved external services.
