---
name: chief-editor-review
description: "Create recurring evidence-backed Facebook or Instagram editorial reviews for Chief Editors and management. Use to compare a focal page with approved competitors, diagnose the current month's performance, inspect posts and actual media, extract usable audience signals, and deliver a verified standalone HTML report. Report-only: no SPS prompt changes or publishing."
---

# Chief Editor Review

Turn approved Facebook or Instagram evidence into a concise, critical, actionable editorial review. The report should help a Chief Editor decide what to commission, scale, improve, stop, or test; metrics are the evidence base, not the story.

This is an end-to-end report skill. It may reuse an existing evidence package, import approved exports, or perform approved bounded collection. It never changes SPS prompts, publishes, schedules, replies, or moderates.

Guide non-technical colleagues in plain language. Ask for business information, explain unfamiliar terms briefly, and perform the data and report mechanics yourself rather than giving the user a technical manual.

## Confirm the brief

Ask only for missing information:

1. Platform, focal page, and approved competitors.
2. Audience, performance objective, existing content pillars, and usable pillar tags.
3. Available posts, metrics, images, comments, previous reports, and approved data access.
4. Editorial rules and exclusions to preserve.
5. Any approved current-period or next-period content plan, fixed product priorities, and known commissioning commitments.
6. Any language override and any presentation-only reference report.

Unless the user specifies otherwise, propose:

- the latest completed calendar month as the decision month and the two preceding completed months as context;
- Hong Kong time;
- shares per post as the primary KPI;
- one bilingual English / Traditional Chinese report, defaulting to English with a top-right `中 / ENG` switch;
- source-language hooks and editorial examples in their original language;
- a new standalone HTML report with embedded images.

State the exact dates. If pillars are unknown, propose a working classification from approved data before drawing pillar conclusions. Present a short plan and wait for approval.

Treat approved content-pillar names as business taxonomy identifiers. Record their exact spelling and language in the brief, then render those labels verbatim in every report language; translate the surrounding analysis, not the taxonomy label.

Treat an approved content plan as strategic context, not performance evidence. Use it to define the decision space—what the newsroom intends to build, retain, or explore—while performance evidence determines how the execution should change. Import only directions relevant to the confirmed review; do not turn commercial or unrelated planning material into findings.

## Decide whether collection is needed

Read [the collection contract](references/collection-contract.md).

Reuse existing data when it covers the confirmed pages, dates, fields, media, and required comments. Recollect only missing or stale coverage. Before any paid collection, show the scope, maximum approved cost, canary size, and stopping condition; wait for explicit approval.

When Apify is approved and a suitable actor/input is already known, use `scripts/apify_collection.py` rather than recreating credential-handling, polling, fetch, or receipt logic. Never request credentials in chat or write them into files.

## Build the evidence package

Use the same dates and timezone across pages. Save raw data, normalized posts, de-identified usable comments, original media, and redacted receipts in a new run directory. Preserve missing values as missing.

Record post counts by page before exclusions, identified ad/paid-partnership counts, organic analyzed counts, metric coverage, unavailable media, unknown promotion status, and collection limitations. Do not infer advertising from strong performance or commercial wording.

For comments, identify intentional PM-CTA posts before comment collection when the approved source permits it. Exclude those posts from newsroom comment analysis. For eligible posts, retain at most 20 ranked top-level comments per post unless the user approves another bounded rule. Remove commenter identities and separate Page-authored replies.

Use `scripts/validate_evidence.py` on normalized evidence before analysis. A failed evidence gate results in a `partial` or `blocked` receipt, not invented coverage.

## Analyze as a Chief Editor

Read and follow [the analysis contract](references/analysis-contract.md). Use all four methods:

- **Benchmarking**: fix comparable internal high, middle, and low sets before revealing performance.
- **Reframing**: inspect captions and actual images with performance hidden to generate hypotheses.
- **Internalizing**: learn from approved competitor executions without copying.
- **Corresponding**: synthesize useful non-PM reader feedback and inspect Page replies separately.

Run `scripts/analyze_performance.py` to produce the reusable quantitative base: organic monthly medians/totals/counts, breakout concentration, cohort ranks, and eligible timing/frequency scores. Treat that output as calculation evidence, then inspect captions and actual media to make the editorial diagnosis.

Make the current month the subject. Use the earlier two months to explain whether the movement is a continuation, reversal, or new break. Diagnose what editorial choices carried or dragged the month; do not merely restate the chart.

Treat every decision-material Page or Core-pillar gap in Part 1 as a diagnostic question. Resolve it in Part 2 through like-for-like cohorts, performance distribution, content and packaging choices, and counterevidence; when the approved evidence cannot explain the residual gap, label it unresolved rather than leaving the scorecard to imply a cause.

For Reels or other short video, use a hybrid media review when the brief requires actual-video diagnosis: inspect every eligible video's caption, cover, first three seconds, full audio/script where available, and fixed keyframes across the full timeline; then deep-review a page-balanced, high/middle/low sample through its complete script and visual sequence. Record silent or unavailable media explicitly. Use local transcription for structure, cross-check it against on-screen text and frames, and do not quote speech-recognition wording as verbatim evidence. Diagnose whether the opening establishes a decision, tension, or payoff and whether the sequence keeps proving it; do not reduce video analysis to caption or cover review.

For photo posts and carousels, inspect the actual image set rather than treating the caption or cover as the post. Deep-review representative cases for image choice and proof, cover promise, on-image headline and wording, caption-image division, information density, card-by-card progression, swipe reason, and final payoff or action. The diagnosis should identify the editorial decision to preserve or change, not merely describe the asset.

Use two complementary competitor views: map comparable posts into the focal Page's approved pillars, and independently group each competitor's remaining output into its own recurring content territories. `Other` is an intake queue for discovery, not the final editorial explanation.

Separate **Observation**, **Inference**, and **Hypothesis / Test**. Every performance conclusion needs an evidence anchor. Suggestions unsupported by performance evidence remain tests.

## Build the report

Read and follow [the report contract](references/report-contract.md). Use [the neutral HTML template](assets/chief-editor-report-template.html) as a presentation baseline, adapting it to the approved business-unit reference without carrying over old findings.

Keep the stable evidence-to-action reading path:

1. Current-Month Performance
2. Editorial Diagnosis
3. Next-Month Actions

Start with evidence, then move from diagnosis to action. The opening hero is a compact management synopsis of the whole review: what happened in the decision month, the strongest editorial explanation, and the most important operating implication. Keep detailed briefs and status calls in the final action layer. Part 1 shows what changed in the decision month and keeps the Page-level scorecard and Core-pillar comparison as standard modules. Part 2 opens its focal-page and competitor subparts with concise month-level overviews before presenting the deeper cohort and case evidence. End Part 2 with a short management synthesis only when it improves retention; use a separate CEO Takeaways chapter only when it adds meaning not already delivered by those overviews. Part 3 contains every Scale / Improve / Stop / Test decision so the report has one action layer.

Place post-level evidence inside the diagnosis it supports rather than after the actions. Show original media uncropped, use the source-language first line as the linked title, and include competitor links wherever a comparison or opportunity depends on them. Diagnose the whole eligible high/middle/low cohort before choosing representative cases. High performers explain what to replicate; comparable low performers or negative examples explain what failed and carry the improvement tests. Each deep case should cover the content promise, headline architecture, visual hierarchy, likely sharing logic, counterevidence or limitation, and the transferable editorial rule.

Make every material editorial difference immediately inspectable. Follow the judgement with one or two compact, clickable representative post examples; show both sides when a reliable comparison exists, and use the strongest available side when it does not. Full linked evidence cards directly beside the judgement already satisfy this requirement.

Make chapters and subparts visually unmistakable. Use strong numbered chapter bands and clearly labelled focal-page, competitor, and reader-signal subparts so a time-poor reader always knows whether they are looking at data, diagnosis, synthesis, or action. Label nested items by function—such as `Case study`, `Negative example`, or `Competitor opportunity`—without repeating the parent number; reserve numbering for the main chapters, the `2A` / `2B` / `2C` subparts, and the final action list. When Part 2 is long, add a compact local index and collapse secondary evidence.

Use color as semantic reinforcement, not decoration: dark teal for report structure, green for positive movement or advantage, red for negative movement or disadvantage, amber for opportunities/tests, blue for evidence/cases, and grey for context. In the Core-pillar comparison, color the complete rise/fall and Ahead/Behind text while retaining arrows, words, and exact values so meaning never depends on color alone. Render this matrix as stacked pillar cards on narrow screens.

Keep each deep case economical and give each post one analytical home. Put the complete post-specific editorial read directly beneath its media and metadata, replacing any short descriptive caption. A case-level synthesis is reserved for cross-post comparison and the transferable rule; a second `Editor’s cut` or equivalent layer is unnecessary. Apply the same decision-useful depth to every management-visible case for which the evidence is available.

For bilingual copy, first lock a language-neutral finding ledger containing each claim, evidence anchor, status, limitation, and action. Draft the English management narrative from that ledger, then author the Traditional Chinese narrative independently for a Hong Kong editorial reader. Use natural Chinese sentence order and keep only familiar newsroom terms that are clearer in English. Finally audit both layers against the ledger so their numbers, evidence status, meaning, and actions match without requiring sentence-by-sentence translation.

Unless the user explicitly opts out, deliver both English and Traditional Chinese in the same standalone file. English is the initial view; the language switch changes the complete management narrative while keeping evidence, metrics, images, links, and source-language examples shared.

Use `scripts/embed_images.py` to make local evidence media self-contained. Run `scripts/validate_report.py` and `scripts/browser_qa.js`, then inspect the resulting desktop and mobile screenshots. Verify chart scales, labels, exact values, images, links, text hierarchy, evidence status, credential exclusion, and preservation of previous reports.

## Deliver and stop

Return the new standalone HTML plus a short receipt naming:

- exact period and timezone;
- pages and primary KPI;
- collected, ad-excluded, and analyzed post counts;
- comment coverage;
- material limitations;
- report and English / Chinese QA paths.

Do not offer or apply SPS prompt changes as part of the report. If the user later wants prompt changes, hand the approved findings to `refine-pillar-prompts` as a separate task.

## Hard boundaries

- No credentials, access tokens, commenter identities, or private collection URLs in reports or Git.
- No paid collection without explicit scope and budget approval.
- No competitor credentials.
- No missing value treated as zero and no invented post, metric, image, link, quote, or match.
- No SPS prompt update, publication, scheduling, reply, or moderation in this skill.

## Skill-source maintenance

The user has granted standing authorization to maintain this skill when an actual review exposes a concrete, repeatable defect in its success criteria, workflow boundary, source of truth, collection/analysis logic, report template, scripts, gates, or examples. A one-off report preference becomes a permanent rule only when the user explicitly asks or the defect is demonstrably reusable.

When maintenance is warranted:

1. Finish or safely stop the active review; never mix report production with an unverified source update.
2. Locate the canonical `marconml/sps-skills` checkout, work on `dev`, and follow its root `AGENTS.md`.
3. Replace, merge, or remove the responsible instruction or implementation. Prefer a positive success contract over accumulated prohibitions.
4. Reproduce the issue with a de-identified canary, run the skill validator and relevant script/report tests, inspect references and contradictions, scan for secrets and user data, and run `git diff --check`.
5. Commit only validated skill-source changes, push to `origin/dev`, verify the remote commit, and refresh this machine's installed copy from that exact source.
6. Report the diagnosis, files, validation, commit, remote verification, and installed-copy status.

Stop without pushing when validation, conflicts, access, or remote verification fails. Never force-push, push to `main`, or commit run data, reports, real comments, credentials, or downloaded social media.
