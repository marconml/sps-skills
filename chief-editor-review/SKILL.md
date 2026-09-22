---
name: chief-editor-review
description: "Create recurring evidence-backed Facebook or Instagram editorial reviews for Chief Editors and management. Use to compare a focal page with approved competitors, diagnose the current month's performance, inspect posts and actual media, extract usable audience signals, and deliver a verified standalone HTML report. Report-only: no SPS prompt changes or publishing."
---

# Chief Editor Review

Turn approved Facebook or Instagram evidence into a concise, critical, actionable editorial review. The report should help a Chief Editor decide what to commission, scale, improve, stop, or test; metrics are the evidence base, not the story.

This is a guided report-building skill. It helps the user export complete post details from Fanpage Karma, inspects whatever columns and media are actually available, builds the analysis dynamically, and leads production of the final report. It does not impose a fixed normalized schema or run a one-click report pipeline. It never changes SPS prompts, publishes, schedules, replies, or moderates.

Guide non-technical colleagues in plain language. Ask for business information, explain unfamiliar terms briefly, and perform the data and report mechanics yourself rather than giving the user a technical manual.

## Confirm the brief

Ask only for missing information:

1. Platform, focal page, and approved competitors.
2. Audience, performance objective, existing content pillars, pillar definitions, and usable Fanpage Karma tags.
3. Available Fanpage Karma exports, post metrics, media, comments, and previous reports.
4. Editorial rules and exclusions to preserve.
5. Any approved current-period or next-period content plan, fixed product priorities, and known commissioning commitments.
6. Whether prior-year same-period post data is available for an optional next-month editorial outlook. Use only the pages and months supplied; missing historical comparators do not block the review.
7. Any language override and any presentation-only reference report.

After learning the objective and inspecting the available metric names, ask the user to choose the primary KPI. Recommend one and explain why. For a Facebook sharing objective, recommend shares per post when shares are available; otherwise recommend the closest comparable metric that directly reflects the stated objective. Never silently substitute a KPI or assume that a similarly named rate uses the same denominator across pages.

Unless the user specifies otherwise, propose:

- the latest completed calendar month as the decision month and the two preceding completed months as context;
- Hong Kong time;
- shares per post as the recommended Facebook KPI when the objective is useful redistribution and the export includes shares;
- one bilingual English / Traditional Chinese report, defaulting to English with a top-right `中 / ENG` switch;
- source-language hooks and editorial examples in their original language;
- a new standalone HTML report with embedded images.

State the exact dates. Use approved Fanpage Karma tags when they reliably represent the newsroom taxonomy. Otherwise use the user's pillar definitions to classify posts. If neither exists, inspect the approved exports, propose a working taxonomy with definitions and examples, and obtain confirmation before drawing pillar conclusions. Present a short plan and wait for approval.

Treat approved content-pillar names as business taxonomy identifiers. Record their exact spelling and language in the brief, then render those labels verbatim in every report language; translate the surrounding analysis, not the taxonomy label.

Treat an approved content plan as strategic context, not performance evidence. Use it to define the decision space—what the newsroom intends to build, retain, or explore—while performance evidence determines how the execution should change. Import only directions relevant to the confirmed review; do not turn commercial or unrelated planning material into findings.

## Guide the Fanpage Karma export

Read [the collection contract](references/collection-contract.md).

Reuse an existing Fanpage Karma export when it covers the confirmed pages, dates, post population, fields, and selected KPI. Otherwise guide the user in plain language to export complete post details for every approved page over the same exact period. Do not ask the user to expose credentials or grant competitor access.

Inspect the workbook or CSV after export rather than assuming fixed column names, worksheets, formats, or metric formulas. Ask only for a corrected or additional export when a decision-critical field or population is missing.

## Run the coverage checkpoint

Before analysis, show the user a short **Coverage checkpoint** with the exact dates and timezone, each page's exported post count, available KPI fields, date/link/caption/format/tag coverage, media availability, promotion-status coverage, and comment availability. Mark the package `ready`, `partial`, or `blocked`; explain how every gap limits the report and obtain confirmation before continuing with a partial package.

Use the same dates and timezone across pages. Preserve the supplied Fanpage Karma exports unchanged. Preserve missing values as missing. Record post counts by page before exclusions, identified ad/paid-partnership counts, organic analyzed counts, metric coverage, unavailable media, unknown promotion status, and export limitations. Do not infer advertising from strong performance or commercial wording.

For comments, identify intentional PM-CTA posts before comment analysis. Exclude those posts from newsroom comment insight. For eligible posts, retain at most 20 ranked top-level comments per post unless the user approves another bounded rule. Remove commenter identities and separate Page-authored replies.

Create a new working folder for every review. Keep untouched exports in `source-exports/`, temporary calculations and extracts in `working/`, downloaded originals and video frames in `media/`, validation receipts and screenshots in `qa/`, and the new standalone report at the run root. Never overwrite source exports or a previous report. Download media yourself from approved post/media links when accessible; record unavailable assets instead of substituting unrelated media.

## Analyze as a Chief Editor

Read and follow [the analysis contract](references/analysis-contract.md). Use all four methods:

- **Benchmarking**: fix comparable internal high, middle, and low sets before revealing performance.
- **Reframing**: inspect captions and actual images with performance hidden to generate hypotheses.
- **Internalizing**: learn from approved competitor executions without copying.
- **Corresponding**: synthesize useful non-PM reader feedback and inspect Page replies separately.

Build calculations from the inspected export structure. Record the field mapping and KPI definition used for this run so another reviewer can audit it, but do not force the data into a permanent universal schema. Calculate the quantitative base needed for the approved brief: monthly medians/totals/counts, breakout concentration, cohort ranks, and eligible timing/frequency scores. Then inspect captions and actual media to make the editorial diagnosis.

Make the current month the subject. Use the earlier two months to explain whether the movement is a continuation, reversal, or new break. Diagnose what editorial choices carried or dragged the month; do not merely restate the chart.

Treat every decision-material Page or Core-pillar gap in Part 1 as a diagnostic question. Resolve it in Part 2 through like-for-like cohorts, performance distribution, content and packaging choices, and counterevidence; when the approved evidence cannot explain the residual gap, label it unresolved rather than leaving the scorecard to imply a cause.

For Reels or other short video, use a bounded frame review rather than pretending to inspect every frame. Inspect the cover, selected frames from the opening three seconds, selected evenly spaced or scene-change frames across the timeline, and the closing payoff; use the audio/script where available. Deep-review a page-balanced, high/middle/low sample through its complete sequence. Record the frame-selection rule and silent or unavailable media explicitly. Use local transcription for structure, cross-check it against on-screen text and frames, and do not quote speech-recognition wording as verbatim evidence. Diagnose whether the opening establishes a decision, tension, or payoff and whether the sequence keeps proving it; do not reduce video analysis to caption or cover review.

For photo posts and carousels, inspect the actual image set rather than treating the caption or cover as the post. Inspect every image in every eligible carousel whose media is available; do not sample only the cover or a representative slide. Review image choice and proof, cover promise, on-image headline and wording, caption-image division, information density, card-by-card progression, swipe reason, and final payoff or action. The diagnosis should identify the editorial decision to preserve or change, not merely describe the asset.

Use two complementary competitor views: map comparable posts into the focal Page's approved pillars, and independently group each competitor's remaining output into its own recurring content territories. `Other` is an intake queue for discovery, not the final editorial explanation.

Separate **Observation**, **Inference**, and **Hypothesis / Test**. Every performance conclusion needs an evidence anchor. Suggestions unsupported by performance evidence remain tests.

Derive exact Suggested Hooks and Visual Tests from the original on-image package plus the focal Page's successful same-pillar, same-format high/middle/low evidence. Default to a minimum-change rewrite: preserve the story, house voice, familiar wording, approximate display load, line structure, and usable visual assets; change only the mechanism the evidence identifies as weak. Competitor executions may inform the mechanism but do not replace the focal Page's production grammar. Render proposed copy with its intended line breaks and actual visual hierarchy: each headline line uses the main proposal style, while smaller text maps to a verified eyebrow, badge, qualifier, or disclaimer role in the original/template. Treat a suggestion as directional until its source fidelity, wrapping, relative type size, and fit have been checked in the rendered format or template.

## Build the report

Read and follow [the report contract](references/report-contract.md). Use [the neutral HTML template](assets/chief-editor-report-template.html) as a presentation baseline, adapting it to the approved business-unit reference without carrying over old findings.

Keep the stable evidence-to-action reading path:

1. Current-Month Performance
2. Editorial Diagnosis
3. Next-Month Actions

Start with evidence, then move from diagnosis to action. The opening hero is a compact management synopsis of the whole review: what happened in the decision month, the strongest editorial explanation, and the most important operating implication. Keep detailed briefs and status calls in the final action layer. Part 1 shows what changed in the decision month and keeps the Page-level scorecard and Core-pillar comparison as standard modules. Part 2 opens its focal-page and competitor subparts with concise month-level overviews before presenting the deeper cohort and case evidence. End Part 2 with a short management synthesis only when it improves retention; use a separate CEO Takeaways chapter only when it adds meaning not already delivered by those overviews.

When the user supplies relevant prior-year data and wants forward planning, insert **Next-Month Editorial Outlook** between Diagnosis and Actions. A candidate qualifies only when the same season, festival, observance, service cycle, or other predictable trigger recurs inside the current planning window; the historical post directly addressed that trigger; and the editor can act on it now. Verify the current-year trigger with an approved source. A following-month historical post may inform earlier commissioning only when that same trigger falls earlier this year or requires preparation lead-time. After a topic passes this gate, use its historical high/middle/low evidence and the current diagnosis to shape the package. One-off people, incidents, general evergreen posts, and posts that merely happened to publish in the old date range stay outside the Outlook. Present up to three numbered editorial points; when three qualify, show exactly three. Each point leads with the topic or direction, explains the editorial opportunity, links a source-language title example, and states the editor's next step and evidence status. Place the fuller historical high/low examples after the points in a compact expandable evidence module. Label every item as a historical signal, Inference, or Test rather than a forecast. Keep detailed evidence in the Outlook and keep the final Actions chapter as the single assignable action layer.

Place post-level evidence inside the diagnosis it supports rather than after the actions. Show original media uncropped, use the source-language first line as the linked title, and include competitor links wherever a comparison or opportunity depends on them. Diagnose the whole eligible high/middle/low cohort before choosing representative cases. High performers explain what to replicate; comparable low performers or negative examples explain what failed and carry the improvement tests. Each deep case should cover the content promise, headline architecture, visual hierarchy, likely sharing logic, counterevidence or limitation, and the transferable editorial rule.

Make every material editorial difference immediately inspectable. Follow the judgement with one or two compact, clickable representative post examples; show both sides when a reliable comparison exists, and use the strongest available side when it does not. Full linked evidence cards directly beside the judgement already satisfy this requirement.

Make chapters and subparts visually unmistakable. Use strong numbered chapter bands and clearly labelled focal-page, competitor, and reader-signal subparts so a time-poor reader always knows whether they are looking at data, diagnosis, synthesis, or action. Label nested items by function—such as `Case study`, `Negative example`, or `Competitor opportunity`—without repeating the parent number; reserve numbering for the main chapters, the `2A` / `2B` / `2C` subparts, and the final action list. When Part 2 is long, add a compact local index and collapse secondary evidence.

Use color as semantic reinforcement, not decoration: dark teal for report structure, green for positive movement or advantage, red for negative movement or disadvantage, amber for opportunities/tests, blue for evidence/cases, and grey for context. Fix the Core-pillar comparison as a horizontal table on desktop, with one row per pillar and the seven columns defined in the report contract. Color the complete rise/fall and Ahead/Behind text while retaining arrows, words, and exact values so meaning never depends on color alone. On narrow screens, stack the same labelled cells as pillar cards, preserving every value and the column order.

Keep each deep case economical and give each post one analytical home. Put the complete post-specific editorial read directly beneath its media and metadata, replacing any short descriptive caption. A case-level synthesis is reserved for cross-post comparison and the transferable rule; a second `Editor’s cut` or equivalent layer is unnecessary. Apply the same decision-useful depth to every management-visible case for which the evidence is available.

For bilingual copy, first lock a language-neutral finding ledger containing each claim, evidence anchor, status, limitation, and action. Draft the English management narrative from that ledger, then author the Traditional Chinese narrative independently for a Hong Kong editorial reader. Use natural Chinese sentence order and keep only familiar newsroom terms that are clearer in English. Finally audit both layers against the ledger so their numbers, evidence status, meaning, and actions match without requiring sentence-by-sentence translation.

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

Ordinary report runs do not modify this skill. If the user explicitly requests a reusable skill change, edit the canonical source, follow its repository instructions, validate with de-identified fixtures, and never commit run data, reports, comments, credentials, or downloaded social media.
