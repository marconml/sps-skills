# Fanpage Karma Export and Coverage Contract

Read this reference whenever evidence must be checked, imported, or refreshed. Codex leads the process in plain language; the user should not need to understand schemas, scripts, or APIs.

## Confirm the export request

Write a short, credential-free brief containing:

- focal page and approved competitor page names or URLs;
- exact start date, end date, and timezone;
- platform and complete-post scope;
- audience and editorial objective;
- selected primary KPI and the reason it fits the objective;
- approved pillar names, definitions, and Fanpage Karma tags when available;
- known exclusions, promotion rule, report language, and available comments/media.

Ask the user to choose the primary KPI after explaining a recommendation. For a Facebook objective centred on useful redistribution, recommend shares per post when the export exposes shares. If the objective or available fields point elsewhere, recommend the closest direct and comparable measure. Confirm whether Fanpage Karma reports a raw count, an interaction total, or a rate and record any denominator. Do not assume that public engagement equals reach or an engagement rate.

## Guide the Fanpage Karma export

First inspect any workbook or CSV the user already supplied. Reuse it when it contains the complete post population for every approved page over the same exact dates. Do not require a new export only because the column names or workbook layout differ from a previous run.

When a new export is needed, guide the user through these outcomes in Fanpage Karma:

1. Open the dashboard or analysis containing the focal page and all approved competitors.
2. Set the exact shared reporting period and confirm the timezone used for publication timestamps.
3. Open the Posts or Content view, select the requested key figures/KPIs, and show all posts rather than only top posts or a dashboard summary.
4. Export the complete post-detail table to Excel or CSV. If the account splits pages or metrics across exports, export each necessary table and retain the page names and period in the filenames.
5. If comments are in scope and available through an approved export, export them separately. Absence of comments does not become zero comments; it becomes a coverage limitation.

Ask the user to provide the exported files, not credentials. Never request Fanpage Karma login details, Facebook Page tokens, or competitor credentials in chat.

## Inspect dynamically

Open the supplied files and identify the actual sheets, headers, metric labels, formulas or notes, row grain, date range, page identities, and post population. Build a run-specific field map. Never demand fixed worksheet names or normalize the export into a permanent universal schema.

For every eligible publication, seek the strongest available equivalents of:

- stable post ID and direct permalink;
- page identity;
- full caption and first-line hook;
- publication timestamp and timezone;
- content format;
- media URL or post URL from which approved media can be downloaded;
- raw reactions, comments, shares, and the selected primary KPI;
- approved tags or another pillar-classification input;
- authoritative promotion/ad status or `unknown`.

Preserve missing values as missing. Keep the original metric label and definition. If a metric is available for some pages but not others, do not use it as a cross-page KPI without explicit qualification.

## Dynamic pillar handling

Use one of these routes, in order:

1. Use approved Fanpage Karma tags when they consistently represent the newsroom's content pillars.
2. Apply user-supplied pillar definitions, documenting ambiguous assignments.
3. If neither is available, inspect topics and formats in the approved exports, propose a small working taxonomy with definitions and examples, and wait for confirmation before pillar analysis.

Keep an `Unresolved` intake group for genuinely ambiguous posts. Do not hide a large share of output inside `Other`; revisit it for coherent recurring territories.

## Media and comments

Codex downloads original media from approved post or media links into the run folder when accessible. Do not make the user install a downloader. Record inaccessible, expired, or absent media rather than replacing it with unrelated imagery.

For every eligible carousel with available media, download and inspect every image in order. For each Reel or short video selected for media analysis, inspect selected frames: the cover, multiple frames from the opening three seconds, evenly spaced or scene-change frames across the body, and the closing payoff. Record the frame-selection rule; do not imply frame-by-frame inspection. Use audio or a local transcript where available, with speech recognition treated as structural assistance rather than a verbatim source.

Comments are analyzed only when lawfully supplied. Identify intentional comment-to-private-message posts from the caption/Page-reply pattern and exclude them from newsroom comment insight. Remove commenter names, usernames, profile URLs, avatars, IDs, and other identity fields. Keep Page-authored replies separate. Missing comment exports limit the Corresponding method and must be disclosed.

## Working folder discipline

Create a new folder for each review and preserve previous runs:

```text
<review-name>-<YYYY-MM-DD>/
  source-exports/   # untouched Fanpage Karma Excel/CSV files
  working/          # run-specific field map, calculations, classifications, extracts
  media/            # downloaded originals, carousel images, selected video frames
  qa/               # coverage receipt, validation output, desktop/mobile screenshots
  report.html       # new standalone deliverable
```

Never edit files in `source-exports/`. Temporary scripts and transformed tables belong in `working/`; they are run-specific aids, not a fixed end-to-end runner. Exclude credentials, private URLs, commenter identities, and source media from Git.

## Coverage checkpoint

Before analysis, present a compact table with one row per page and show:

- exact exported date range and timezone;
- exported post count;
- post ID/link, caption, timestamp, format, tag/pillar, and primary-KPI coverage;
- supporting metric coverage;
- promotion-status coverage;
- media and carousel completeness;
- Reel availability and selected-frame feasibility;
- comment availability for the focal page;
- exclusions, duplicates/reposts, and material limitations.

Reconcile the export's earliest/latest timestamps and row counts against the requested scope. Flag filters, truncated top-post exports, duplicated rows, summary-only files, mismatched periods, missing competitors, and unequal KPI definitions.

Return one status:

- `ready`: the evidence supports the confirmed decisions;
- `partial`: useful evidence exists, every gap and affected conclusion is named, and the user accepts proceeding;
- `blocked`: the post population, period, page identity, or chosen KPI is too incomplete for the requested comparison.

Do not begin performance conclusions until the checkpoint is resolved. Never silently supplement Fanpage Karma exports with an outside collection service.
