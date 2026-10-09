---
name: chief-editor-review
description: "Create recurring evidence-backed Facebook or Instagram editorial reviews for Chief Editors and management. Use to compare a focal page with approved competitors, diagnose the current month's performance, inspect posts and actual media, extract usable audience signals, and deliver a verified standalone HTML report. Report-only: no SPS prompt changes or publishing."
---

# Chief Editor Review

Turn approved Facebook or Instagram evidence into a concise, critical, actionable editorial review. The report should help a Chief Editor decide what to commission, scale, improve, stop, or test; metrics are the evidence base, not the story.

This is a guided report-building skill. It helps the user export complete post details from Fanpage Karma, inspects whatever columns and media are actually available, builds the analysis dynamically, and leads production of the final report. It does not impose a fixed normalized schema or run a one-click report pipeline. It never changes SPS prompts, publishes, schedules, replies, or moderates.

Guide non-technical colleagues in plain language. Ask for business information, explain unfamiliar terms briefly, and perform the data and report mechanics yourself rather than giving the user a technical manual.

## Shared-version check

At the start of each new review, before loading detailed contracts, run `python3 <installed-skill>/scripts/sync_skill.py --target <installed-skill>` once. This installation includes permission to sync this skill from `marconml/sps-skills` `dev`, the user-designated shared update branch. The updater replaces the complete skill, backs up the prior copy, and preserves locally modified or untracked installations with a clear status. If updated, re-read the installed `SKILL.md` and relevant contracts before continuing; do not repeat the check during that review. On unavailable/deferred/local-change status, continue using the installed copy and state the status briefly. Record the installed commit and sync status in `qa/skill-version.json` for the report. Updates apply to new reviews, not reviews already underway. See [installation and updates](references/installation-updates.md) for first installation and recovery.

## Confirm the brief

If the user already supplied a Fanpage Karma export, inspect it before asking scope questions. The focal page name is sufficient when it identifies one exported profile; derive competitors from the export and request page URLs only to resolve ambiguous identities or missing evidence links. Treat the exported profile names and observed post dates as the provisional page, competitor, and period selection. Do not ask the user to repeat pages, competitors, or dates that are readable from the export.

When the focal page is Sunday Kiss / SundayKiss, load [the Sunday Kiss profile](references/sundaykiss-profile.md) for its approved pages, audience, Core labels and ad-review rule. When the focal page is GOtrip / GOtrip.hk, load [the GOtrip profile](references/gotrip-profile.md) before taxonomy and exclusion decisions. This profile applies only to GOtrip; the shared writing, media and QA contracts apply to every review. Reuse confirmed profile information and ask only for missing or changed business information.

Ask only for business information that is still missing:

1. Which exported profile is the focal page when that is not obvious.
2. Audience, performance objective, existing content pillars, pillar definitions, and usable Fanpage Karma tags.
3. Available media, comments, previous reports, and any additional exports.
4. Editorial rules and exclusions to preserve, plus whether video work is original production, repost selection or a mix.
5. Any approved current-period or next-period content plan, fixed product priorities, and known commissioning commitments.
6. Available data: the review month plus its preceding two months, and the following two months from the previous year; reuse supplied files and ask only for missing windows.
7. Any language override and any presentation-only reference report.

Use total interactions per post as the default primary KPI, unless the user explicitly selects another metric. Inspect the exported field and record its exact definition/components and any cross-platform inclusion; use per-post medians for typical performance and monthly totals for scale. Apply this default without asking the user to choose a KPI again. If the required total is absent or definitions are not comparable across pages, explain the gap and ask only for the evidence or decision needed to resolve it; do not silently substitute reach or an engagement rate.

Request two chronological exports, each containing the same approved focal page and competitors: the three complete months ending with the review month, and the two calendar months immediately after that review month in the previous year. For a September 2026 review, request 1 July–30 September 2026 and 1 October–30 November 2025. The first window supplies current diagnosis and its prior-two-month comparison; the second supplies next-month recurring topics and preparation lead-time. State exact dates, including year rollover, and reuse supplied coverage without requesting an entire year.

Unless the user specifies otherwise, propose:

- Hong Kong time;
- total interactions per post as the primary KPI, with its monthly median and total;
- one bilingual English / Traditional Chinese report, defaulting to English with a top-right `中 / ENG` switch;
- source-language hooks and editorial examples in their original language;
- a new standalone HTML report with embedded images.

Read back the exact exported dates and profiles before analysis. Use approved Fanpage Karma tags when they reliably represent the newsroom taxonomy. Otherwise use the user's pillar definitions to classify posts. If neither exists, inspect the approved exports, propose a working taxonomy with definitions and examples, and obtain confirmation before drawing pillar conclusions. Present a short plan and wait for approval.

Treat approved content-pillar names as business taxonomy identifiers. Record their exact spelling and language in the brief, then render those labels verbatim in every report language; translate the surrounding analysis, not the taxonomy label.

Treat an approved content plan as strategic context, not performance evidence. Use it to define the decision space—what the newsroom intends to build, retain, or explore—while performance evidence determines how the execution should change. Import only directions relevant to the confirmed review; do not turn commercial or unrelated planning material into findings.

## Guide the Fanpage Karma export

Read [the collection contract](references/collection-contract.md).

Reuse an existing Fanpage Karma export when it covers the confirmed pages, dates, post population, fields, and selected KPI. Otherwise guide the user in plain language to export complete post details for every approved page over the same exact period. Do not ask the user to expose credentials or grant competitor access.

Give this simple scope instruction before technical field guidance:

> In Fanpage Karma, select your own page by using `+ Profile`, then add all the competitors you want to compare to the same dashboard. Open the **Content** tab, select the reporting period, change the post table to **Top 5000**, and make **one combined export per date window** containing all selected pages. Upload the two Excel or CSV files here.

Do not tell the user to export each page separately. Before they begin, give the filled example from the collection contract so they can see every Fanpage Karma selection and every business answer Codex will need. Accept `Unknown`, `None`, or `Please propose` for information the user does not have.

Inspect the workbook or CSV after export rather than assuming fixed column names, worksheets, formats, or metric formulas. Ask only for a corrected or additional export when a decision-critical field or population is missing.

## Run the coverage checkpoint

Before analysis, show the user a short **Coverage checkpoint** with the profiles found, each profile's earliest and latest post timestamp, timezone status, exported post count, available KPI fields, date/link/caption/format/tag coverage, media availability, promotion-status coverage, and comment availability. Confirm that all intended profiles appear in the same export. If the valid post population is exactly 5,000, flag possible truncation and propose non-overlapping date batches covering the same intended date windows and all approved profiles; a shorter window or accepted limitation is the user’s choice. End the scope read-back with a plain confirmation such as: “I found these pages covering these dates. Is this the intended comparison?” Ask for a corrected export only when the user says the scope is wrong or the evidence is decision-critically incomplete. Mark the package `ready`, `partial`, or `blocked`; explain how every gap limits the report and obtain confirmation before continuing with a partial package.

Use the same dates and timezone across pages. Preserve the supplied Fanpage Karma exports unchanged. Preserve missing values as missing. Record post counts by page before exclusions, identified ad/paid-partnership counts, organic analyzed counts, metric coverage, unavailable media, unknown promotion status, and export limitations. Strong performance or commercial wording alone does not establish advertising. Apply an approved BU ad-review policy when the user authorises inference from combined evidence, recording inferred status separately from confirmed paid disclosure.

For comments, identify intentional PM-CTA posts before comment analysis. Exclude those posts from newsroom comment insight. For eligible posts, retain at most 20 ranked top-level comments per post unless the user approves another bounded rule. Remove commenter identities and separate Page-authored replies.

Create a new working folder for every review. Keep untouched exports in `source-exports/`, temporary calculations and extracts in `working/`, downloaded originals and video frames in `media/`, validation receipts and screenshots in `qa/`, and the new standalone report at the run root. Never overwrite source exports or a previous report. Download media yourself from approved post/media links when accessible; record unavailable assets instead of substituting unrelated media.

## Analyze as a Chief Editor

Read and follow [the analysis contract](references/analysis-contract.md). Use all four methods:

- **Benchmarking**: fix comparable internal high, middle, and low sets before revealing performance.
- **Reframing**: inspect actual media with performance hidden to generate hypotheses; video judgments come from playback, while still-image judgments include the card/caption package.
- **Internalizing**: learn from approved competitor executions without copying.
- **Corresponding**: synthesize useful non-PM reader feedback and inspect Page replies separately.

Build calculations from the inspected export structure. Record the field mapping and KPI definition used for this run so another reviewer can audit it, but do not force the data into a permanent universal schema. Calculate the quantitative base needed for the approved brief: monthly medians/totals/counts, breakout concentration, cohort ranks, and eligible timing/frequency scores. Then inspect the actual media to make the editorial diagnosis, using the format-specific evidence rules below.

Make the current month the subject. Use the earlier two months to explain whether the movement is a continuation, reversal, or new break. Diagnose what editorial choices carried or dragged the month; do not merely restate the chart.

Treat every decision-material page gap, internal Core-pillar movement or cross-page general-pillar gap in Part 1 as a diagnostic question. Resolve it in Part 2 through like-for-like cohorts, performance distribution, content and packaging choices, and counterevidence; when the approved evidence cannot explain the residual gap, label it unresolved rather than leaving the scorecard to imply a cause.

For Reels or other short video, use a bounded frame review rather than pretending to inspect every frame. Inspect playback, selected frames from the opening three seconds, selected evenly spaced or scene-change frames across the timeline, and the closing payoff; use the audio/script where available. Deep-review a page-balanced, high/middle/low sample through its complete sequence. Record the frame-selection rule and silent or unavailable media explicitly. Use local transcription for structure, cross-check it against on-screen text and frames, and do not quote speech-recognition wording as verbatim evidence. Match recommendations to the approved production model. For a repost-led newsroom, translate the reading into source-video selection: which traveller need the original serves, what visible proof and narrative progression to look for, and what makes a candidate useful to publish. Original shooting or recutting briefs apply when that work is in scope. Diagnose whether the opening establishes a decision, tension, or payoff and whether the sequence keeps proving it; use playback alone for performance diagnosis. Captions and static covers identify posts, programmes and exclusions; they do not explain video performance.

For photo posts and carousels, inspect the actual image set rather than treating the caption or cover as the post. Inspect every image in every eligible carousel whose media is available; do not sample only the cover or a representative slide. Review image choice and proof, cover promise, on-image headline and wording, caption-image division, information density, card-by-card progression, swipe reason, and final payoff or action. The diagnosis should identify the editorial decision to preserve or change, not merely describe the asset.

Keep programme identity and subject taxonomy separate. Core pillars are the focal newsroom's named programmes, classified from its approved programme labels and used for internal month/format comparison. General pillars are derived from the reviewed content across all pages, with at most six report-level subjects, shared definitions and clear coverage. Merge related subjects by reader purpose; retain narrower distinctions in working subtopics. User examples illustrate the distinction rather than fixing the taxonomy. Classify the primary reader purpose independently of programme identity; retain geography as a separate facet when it cuts across subjects. A post may belong to a Core programme and one or more general subjects. Competitor Core fields contain only that competitor's real programme identity when available, never a borrowed focal programme label. Preserve each competitor's native territories for discovery. `Other` remains an intake queue to review.

Separate **Observation**, **Inference**, and **Hypothesis / Test**. Every performance conclusion needs an evidence anchor. A Test is an actionable experiment with a reason to invest editorial resources, not a substitute for missing evidence. First choose whether to retain/replicate, improve within the existing source, commission a separately supported new story, or stop at the diagnosis. Follow the recommendation gate in the analysis contract; report recommendations deliver an action, its rationale, and linked execution references rather than internal processing notes.

For photo/carousel cases, derive exact Suggested Hooks and Visual Tests from the original on-image package plus the focal Page's successful same-pillar, same-format high/middle/low evidence. Default to a minimum-change rewrite: preserve the story, house voice, familiar wording, approximate display load, line structure, and usable visual assets; change only the mechanism the evidence identifies as weak. Competitor executions may inform the mechanism but do not replace the focal Page's production grammar. Render proposed copy with its intended line breaks and actual visual hierarchy: each headline line uses the main proposal style, while smaller text maps to a verified eyebrow, badge, qualifier, or disclaimer role in the original/template. Treat a suggestion as directional until its source fidelity, wrapping, relative type size, and fit have been checked in the rendered format or template.

## Build the report

Read and follow [the report contract](references/report-contract.md). Use [the neutral HTML template](assets/chief-editor-report-template.html) as a presentation baseline, adapting it to the approved business-unit reference without carrying over old findings.

Keep the stable evidence-to-action reading path:

1. Current-Month Performance
2. Editorial Diagnosis
3. Next-Month Actions

Start with evidence, then move from diagnosis to action. Build comparative cases within the same media format: carousel/photo cases compare with carousel/photo cases, and video/Reel cases with video/Reel cases. A cross-format example can stand alone but is not comparative evidence. The opening hero is a compact management synopsis of the whole review: what happened in the decision month, the strongest editorial explanation, and the most important operating implication. Keep detailed briefs and status calls in the final action layer. Part 1 shows what changed in the decision month and keeps the Page-level scorecard and Core-pillar comparison as standard modules. Part 2 opens its focal-page and competitor subparts with concise month-level overviews. In 2A, show visual monthly changes and a 400–600-character Chinese, finding-led analysis for each Core pillar before its cases. In 2B, analyse the competitor with the largest current-versus-prior-month median increase before competitor cases, using the report contract’s scope and ranking rules. Summaries name a period-specific change and an editorial implication supported by the comparison; a statement equally true in every month is a topic label, not a finding. End Part 2 with a short management synthesis only when it improves retention; use a separate CEO Takeaways chapter only when it adds meaning not already delivered by those overviews.

Use the supplied prior-year following-two-month window for a historical next-month topic review when relevant seasonal comparators exist; longer supplied history can supplement it. Use supplied history, not an assumption that every calendar month is complete. When the user supplies relevant prior-year data or an approved plan, insert **Next-Month Editorial Outlook** between Diagnosis and Actions. A candidate qualifies only when the same season, festival, observance, service cycle, or other predictable trigger recurs inside the current planning window; the historical post directly addressed that trigger; and the editor can act on it now. Verify the current-year trigger with an approved source. A following-month historical post may inform earlier commissioning only when that same trigger falls earlier this year or requires preparation lead-time. After a topic passes this gate, use its historical high/middle/low evidence and the current diagnosis to shape the package. One-off people, incidents, general evergreen posts, and posts that merely happened to publish in the old date range stay outside the Outlook. Use the approved BU count of qualified historical directions. Place an available historical image, source-language title link and highlighted KPI beside each direction. Each point leads with the topic or direction, explains the editorial opportunity, links a source-language title example, and states the editor's next step and evidence status. Place the fuller historical high/low examples after the points in a compact expandable evidence module. Label every item as a historical signal, Inference, or Test rather than a forecast. Keep detailed evidence in the Outlook and keep the final Actions chapter as the single assignable action layer.

Place post-level evidence inside the diagnosis it supports rather than after the actions. Show original media uncropped, use the source-language first line as the linked title, and include competitor links wherever a comparison or opportunity depends on them. Diagnose the whole eligible high/middle/low cohort before choosing representative cases. High performers explain what to replicate; comparable low performers or negative examples explain possible weaknesses and uncertainty, with an improvement test only when the recommendation gate passes. Each case presents exactly three separate insights following the strong/weak case contract: media evidence supports an explanation, its viewer consequence and a specific editorial response. Select a weak case only when actual-media inspection identifies a concrete weakness; otherwise replace it or retain it as a low-performance observation outside the weak-case slot. Apply the report contract’s editorial-voice routing: decision-changing differences stay beside the case; general analytic safeguards belong once in Methodology.

Make every material editorial difference immediately inspectable. Follow the judgement with one or two compact, clickable representative post examples; show both sides when a reliable comparison exists, and use the strongest available side when it does not. Full linked evidence cards directly beside the judgement already satisfy this requirement.

Make chapters and subparts visually unmistakable. Use strong numbered chapter bands and clearly labelled focal-page and competitor subparts, adding reader signals only when usable comment evidence supports findings so a time-poor reader always knows whether they are looking at data, diagnosis, synthesis, or action. Label nested items by function—such as `Case study`, `Negative example`, or `Competitor opportunity`—without repeating the parent number; reserve numbering for the main chapters, the `2A` / `2B` / `2C` subparts, and the final action list. When Part 2 is long, add a compact local index and collapse secondary evidence.

Use the report contract’s visual reading hierarchy: aligned median/total panels with synchronized page controls and endpoint labels ranked by each metric; paired current/baseline Core medians with counts separate; small monthly pillar charts; expandable distributions/details only where useful. Keep mobile values readable and preserve semantic colors, units and exact-value access. Highlight the primary KPI beside case media, with media-origin/coverage detail in Methodology. Final Actions consolidate supported findings into three concrete priorities instead of owner/status headings.

Keep each deep case economical and give each post one analytical home. Put the complete post-specific editorial read directly beneath its media and metadata, replacing any short descriptive caption. A case-level synthesis is reserved for cross-post comparison and the transferable rule; a second `Editor’s cut` or equivalent layer is unnecessary. Apply the same decision-useful depth to every management-visible case for which the evidence is available.

For bilingual copy, lock claims, anchors, status, limitations and actions in the finding ledger. Author natural Hong Kong Traditional Chinese first, complete its Chinese-only clarity review, then write English from the approved Chinese and ledger. Headings use concrete actors, media details and ordinary verbs; each insight explains what viewers understand or cannot decide. Check semantic parity after both layers are complete. The report contract defines the successful body copy and examples.

Unless the user explicitly opts out, deliver both English and Traditional Chinese in the same standalone file. English is the initial view; the language switch changes the complete management narrative while keeping evidence, metrics, images, links, and source-language examples shared.

Use `scripts/embed_images.py` to make local evidence media self-contained. Run `scripts/validate_report.py` and `scripts/browser_qa.js`, then inspect the resulting desktop and mobile screenshots. Verify chart scales, labels, exact values, images, links, text hierarchy, evidence status, credential exclusion, and preservation of previous reports.

## Deliver and stop

Return the new standalone HTML plus a short receipt naming:

- exact period and timezone;
- pages and primary KPI;
- exported, ad-excluded, and analyzed post counts;
- comment coverage;
- material limitations;
- report and English / Chinese QA paths.

Do not offer or apply SPS prompt changes as part of the report. If the user later wants prompt changes, hand the approved findings to `refine-pillar-prompts` as a separate task.

## Hard boundaries

- No credentials, access tokens, commenter identities, or private source URLs in reports or Git.
- No competitor credentials.
- No missing value treated as zero and no invented post, metric, image, link, quote, or match.
- No SPS prompt update, publication, scheduling, reply, or moderation in this skill.

## Skill-source maintenance

Ordinary report runs may refresh the installed copy through the shared-version check; they do not edit reusable source or publish Git changes. If the user explicitly requests a reusable skill change, edit the canonical source, follow its repository instructions, validate with de-identified fixtures, and never commit run data, reports, comments, credentials, or downloaded social media.
