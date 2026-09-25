# Fanpage Karma Export and Coverage Contract

Read this reference whenever evidence must be checked, imported, or refreshed. Codex leads the process in plain language; the user should not need to understand schemas, scripts, or APIs.

## Let Fanpage Karma carry the scope

If an export is already available, inspect it first. Populate the credential-free brief from the file wherever possible:

- focal page and approved competitor page names or URLs;
- exact start date, end date, and timezone;
- platform and complete-post scope;
- audience and editorial objective;
- selected primary KPI and the reason it fits the objective;
- approved pillar names, definitions, and Fanpage Karma tags when available;
- known exclusions, promotion rule, report language, and available comments/media.

Do not ask the user to repeat page names, competitors, or dates that are readable from the export. Ask which profile is the focal page only when the file does not make that clear. Ask other questions only when a missing answer changes the analysis.

Ask the user to choose the primary KPI after explaining a recommendation. For a Facebook objective centred on useful redistribution, recommend shares per post when the export exposes shares. If the objective or available fields point elsewhere, recommend the closest direct and comparable measure. Confirm whether Fanpage Karma reports a raw count, an interaction total, or a rate and record any denominator. Do not assume that public engagement equals reach or an engagement rate.

## Guide the Fanpage Karma export

First inspect any workbook or CSV the user already supplied. Reuse it when it contains the complete post population for the intended pages over the same exact dates. Do not require a new export only because the column names or workbook layout differ from a previous run.

When a new export is needed, begin with this plain-language instruction:

> In Fanpage Karma, select your own page by using `+ Profile`, then add all the competitors you want to compare to the same dashboard. Open the **Content** tab, select the reporting period, change the post table to **Top 5000**, and make **one combined export** containing all selected pages. Upload that single Excel or CSV file here.

Guide the user further only when needed:

1. In the profile list, click `+ Profile` and add the focal page plus every competitor to compare. Keep all intended profiles in the same dashboard selection.
2. Open the **Content** tab for individual post data; do not export a Benchmarking summary or one page at a time.
3. Select the exact shared reporting period. If the user asks for a recommendation, propose exact start and end dates rather than saying only “three months.”
4. Change the result/table size to **Top 5000 Posts** and use `No filter` unless the user deliberately approved a narrower content filter. This maximizes post-history coverage but does not guarantee completeness when more than 5,000 posts fall inside the period.
5. Select the available key figures/KPIs needed for the brief, then use the Content export control to download one combined Excel or CSV containing every selected profile.
6. If comment text is unavailable in the combined post export, record that limitation and continue only at the approved coverage level. Do not ask the user to split or repeat the post export by profile.

Ask the user to provide the exported files, not credentials. Never request Fanpage Karma login details, Facebook Page tokens, or competitor credentials in chat.

## Filled example for a non-technical user

Show an example like this before asking the user to export. Replace the example names and dates only when the user has already supplied real choices.

```text
Fanpage Karma selections
Platform: Facebook
Profiles in the same dashboard:
- Our page: Example Health
- Competitor 1: Competitor A
- Competitor 2: Competitor B
Content tab: Top 5000 Posts Overview
Filter: No filter
Period: 1 June 2026 to 31 August 2026
Timezone: Hong Kong time, if Fanpage Karma asks
Post columns: combined interactions, shares/reposts, likes, comments,
impressions/views, reach, post date, profile, message, post ID, post link,
and image/media link where available
Export: One combined Excel or CSV for all three profiles

Information to tell Codex after uploading
Our page: Example Health
Audience: Hong Kong adults interested in practical health information
Objective: Increase useful sharing of service-led health content
Primary KPI: Please recommend from the exported fields
Existing pillars or tags: Three-high management; elder care; prevention
Pillar definitions: Three-high management covers blood pressure, glucose,
and blood lipids; elder care covers practical support for older adults
Editorial rules/exclusions: Do not recommend stopping required service posts
Available media and comment text: Only what is included in the export
Previous reports: None
Current or next-period content plan: None
Prior-year data for an outlook: None
Report language: English and Traditional Chinese
Reference report: None
```

Tell the user that `Unknown`, `None`, and `Please propose` are valid answers. Do not make them invent pillars, KPI definitions, plans, or rules they do not have.

## Inspect dynamically

Open the supplied files and identify the actual sheets, headers, metric labels, formulas or notes, row grain, date range, page identities, and post population. Build a run-specific field map. Never demand fixed worksheet names or normalize the export into a permanent universal schema.

Derive and show a scope read-back before requesting business clarification:

- every profile found and its exported post count;
- the earliest and latest valid post timestamp for each profile;
- whether all profiles cover the same period;
- the timezone when present, or `unknown` when the export does not state it;
- summary/average rows, empty profiles, or other non-post records that will be excluded.

End with a direct question: “I found these pages covering these dates. Is this the intended comparison?” If the user confirms, keep the export as the source of truth. If not, explain exactly which Fanpage Karma selection to change and request a replacement export. Do not conduct a separate scope interview unless the export is absent or ambiguous.

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

Reconcile the export's earliest and latest timestamps and row counts across the selected profiles. Flag filters, truncated top-post exports, duplicated rows, summary-only files, mismatched periods, missing competitors, and unequal KPI definitions.

Count valid post records after removing summary/average rows. If the combined export contains exactly 5,000 valid posts, treat possible truncation as a material coverage warning. Recommend a shorter date range and a new one-export run when complete history is required; otherwise record the user's acceptance of the Top 5000 limit.

Return one status:

- `ready`: the evidence supports the confirmed decisions;
- `partial`: useful evidence exists, every gap and affected conclusion is named, and the user accepts proceeding;
- `blocked`: the post population, period, page identity, or chosen KPI is too incomplete for the requested comparison.

Do not begin performance conclusions until the checkpoint is resolved. Never silently supplement Fanpage Karma exports with an outside collection service.
