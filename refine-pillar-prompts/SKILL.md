---
name: refine-pillar-prompts
description: "Analyze SPS pillar prompts and social content through performance-first Benchmarking, Reframing, Internalizing, and Corresponding. Use for evidence-backed prompt learning or a stable editorial performance report: contrast high and low performers, compare reliable same-topic cases across pages, discover competitor territories, and separate observations and supported inferences from hypotheses. Keep accuracy as a guardrail, not the performance objective. Prompt updates still require explicit item selection."
---

# Refine Pillar Prompts

Run an evidence-traceable social-performance review for the requested page and pillars. Choose the deliverable mode from the user's request:

- **Prompt-refinement mode** has two phases. Phase 1 is SPS-read-only and ends with a numbered Markdown learning brief. Phase 2 may update versioned SPS prompts only after the user selects exact item indexes from that brief.
- **Editorial-report mode** is report-only. Read and analyze approved evidence, follow [the editorial report contract](references/editorial-report-contract.md), deliver the requested report, and stop without offering or applying SPS changes unless the user separately asks for prompt refinement.

Evaluation drafts are a separate optional action and require a separate user request. Never infer approval from a recommendation level or a report recommendation.

## Performance Success Contract

The primary objective is the user's selected social-performance outcome, such as shares, reach, qualified comments, clicks, or conversions. Find repeatable content and creative mechanisms in the page's own work and approved competitors, explain the evidence behind them, and turn uncertainty into controlled tests.

Accuracy, non-misleading presentation, legal/privacy requirements, and source fidelity are guardrails. Satisfying a guardrail does not by itself prove that a change will improve performance.

Label every material conclusion by evidence status:

- **Observation**: directly reported or computed from approved data, with the metric, sample/post count, period, comparison basis, and post IDs or links where relevant.
- **Inference**: a performance explanation reasonably supported by one or more observations. Name confounders and counterexamples; do not state causation unless the design supports it.
- **Hypothesis / Test**: a reader perspective, editorial judgement, performance-blind finding, single example, or otherwise unverified proposal. State what future comparison would test it.

Only an Observation or evidence-anchored Inference may be presented as a performance finding. Performance-blind analysis is primarily for detecting possible problems and generating hypotheses.

## Explain the Concepts

Do not assume the user or a new Codex instance knows this system. Explain only the concepts needed for the requested run:

- **Social Page Studio (SPS)** is the workspace that stores social pages, topic-specific pillars, versioned prompts, designs, source material, and draft/publish records.
- A **page** is one social brand/account inside SPS.
- A **pillar** is one topic or editorial workflow inside a page, such as traffic accidents or entertainment.
- Pillar prompt files normally have separate responsibilities:
  - `research.md`: story selection, routing, source, and evidence rules.
  - `caption.md`: framing, information order, wording, attribution, and CTA rules.
  - `image.md`: source-image choice, composition, evidence, privacy, and generation/editing rules.
  - `engagement.md`: Page-authored first comments or replies.
  - `design.md`: stable visual identity and layout rules.
- **W-1, W-2, W-3...** label consecutive 7-day analysis slices. W-1 is the most recent slice, W-2 is the seven days before W-1, and so on. Always translate a W-x label into exact start/end dates and the page timezone before analysis. Do not make the user reason in W-x labels.

Explain the four methods in plain language:

- **Benchmarking**: compare genuinely similar high-, middle-, and low-performing posts from the same page using the selected social KPI to find repeatable mechanisms.
- **Reframing**: hide all performance information and review similar captions/images as a reader to detect possible clarity, trust, or presentation problems and propose tests.
- **Internalizing**: compare approved competitor examples, including reliable same-topic cases across pages, and extract transferable performance logic without copying wording, assets, layouts, or brand identity.
- **Corresponding**: study comments and replies on the page's own posts to find verified corrections, misunderstandings, visual-trust problems, and successful communication.

Treat the legacy name **Compare** as **Benchmarking** and **Invent** as **Reframing**.

## Mandatory Preflight

Before any tool call or data access, check what the user has already supplied and ask for every missing item. Group the questions concisely and explain unfamiliar terms. Wait for the answers; do not silently assume values.

Ask for:

1. **Objective and metric**: the primary social KPI, its field definition, denominator when relevant, and whether paid and organic performance can be separated.
2. **Method**: Benchmarking, Reframing, Internalizing, Corresponding, or an explicit combination.
3. **Target and comparison scope**: page/brand, existing pillars, approved competitor pages, and whether competitor territory discovery is in scope. If SPS is connected, ask for the workspace/team, agent connection, page slug/name, and pillar slug/name. If the user does not know these identifiers, ask permission to list accessible SPS pages and pillars read-only.
4. **Prompt source for prompt-refinement mode**: permission to read the current full prompt files from SPS, or exported prompt files supplied by the user. Record paths, versions, status, and timezone. A report-only run may proceed without prompt files, but must say that it does not assess current prompt coverage.
5. **Evidence range**: exact dates and timezone. If the user says W-x, translate it into exact dates and ask for confirmation.
6. **Data access**:
   - Ask whether SPS exposes the required history, reach, images, embeddings, or comments for the selected methods.
   - If Facebook data is required and SPS does not expose it, ask whether direct read-only Meta Graph API access is allowed and whether `META_PAGE_ID` plus `META_PAGE_ACCESS_TOKEN` are available in an environment file or secret store.
   - Never ask the user to paste an access token into chat. Never print, log, copy into a report, or commit a token.
   - Approved exports or third-party collectors may be used read-only after scope and cost approval. Explain missing coverage and capability-test access without exposing secrets.
   - Explain that Benchmarking needs post history, images, publication times, the selected KPI, and any promotion/ad flags; Corresponding needs posts, comments, and replies. Required Page permissions vary, so capability-test read-only access before analysis.
7. **Advertising and exclusions**: the authoritative ad/sponsored/boosted field or approved classification rule, plus any other exclusions. If ad status is unavailable, record it as unknown rather than guessing.
8. **Method-specific material**:
   - Benchmarking: which Facebook Page/history source contains the chosen performance field.
   - Reframing: which post set should be judged with performance hidden.
   - Internalizing: CSV/file location, source identities, column meanings, image locations, metric meanings, and whether external performance is comparable.
   - Corresponding: comment source, whether replies are included, how Page-authored comments are identified, and whether commenter data must be further de-identified.
9. **Deliverable and language**: prompt-learning brief or editorial report, destination/format, audience, report language, and the source language that editorial examples should preserve. If a prompt-refinement destination is unspecified, propose `pillar-learning-brief-{pillar}-{YYYY-MM-DD}.md` in the current workspace.

If a required answer, permission, prompt snapshot, image, metric definition, or data capability is missing, stop before analysis and report exactly what remains missing.

## Safety and Data Boundaries

- Prefer SPS MCP for current prompts, internal history, embeddings, image references, and comments when those read capabilities are available.
- Allow user-supplied CSV files, exported prompts, attached images, and image URLs as evidence for Internalizing.
- Allow direct Facebook Page-token reads only after explicit user authorization and only when SPS lacks the required read capability. Use them read-only.
- Generate text embeddings through SPS MCP when available. If unavailable, ask the user how to proceed; never silently choose an outside embedding provider.
- Compute deterministic clustering or cosine similarity locally from approved embeddings.
- Inspect actual images visually. Do not treat image-embedding distance as human visual similarity.
- Use an authoritative ad/promotion field or a user-approved rule to identify advertising. Exclude identified ads from organic performance comparisons, retain them in an audit count by page, and state the pre-exclusion count, excluded-ad count, and analyzed count. Do not infer advertising solely from high performance or sales-oriented language.
- De-identify audience comments. Do not retain commenter names unless the user establishes a necessary, lawful reason.
- Do not reply, moderate, approve, schedule, publish, create evaluation drafts, update prompts, or make any other external change during the learning phase.
- Treat prompt application as a separate, user-authorized phase inside this skill. Create an evaluation draft only when the user requests it separately; selecting a learning item does not authorize draft creation.

## Read the Full Current Prompt

In prompt-refinement mode, read every current prompt file relevant to the selected method before learning. Never interpret a pillar from a shortened summary alone.

Keep a complete snapshot containing:

- page and pillar
- prompt path and purpose
- full current text
- version/status/update time
- evidence window and timezone

Use the full snapshot to check whether a proposed learning is already present, adds something genuinely new, or conflicts with an old instruction.

## Prepare the Performance Dataset

Use the same confirmed dates and timezone across pages. Retain post ID/permalink, page, full caption, actual media, publication time, pillar or territory, format, selected KPI, supporting metrics, ad/promotion status, and data-coverage flags. Keep missing values missing; never replace them with zero.

Before comparisons:

1. Record the collected post count by page.
2. Identify ads using the approved source or rule and record the excluded count by page.
3. Build the organic analysis set and record its post count by page.
4. State any unknown ad status, missing KPI coverage, unequal post age, or unavailable reach/promotion data.

The exclusions receipt belongs in the learning brief context or the report's `Review Basis / Scope`.

## Build Internal Comparable Sets

Use this section for Benchmarking and Reframing.

For every eligible post, retain the fields from the prepared performance dataset. Keep the selected KPI and supporting performance fields hidden until Benchmarking explicitly reveals them.

Assign posts to the closest existing pillar from meaning and the user-approved pillar definitions; in prompt-refinement mode, also use the current full pillar prompt. Exclude ambiguous posts.

Embed caption/content only; never put performance, image, or publication time into the embedding input. Within each pillar:

1. Rank or cluster posts by semantic similarity.
2. Select useful pairs or small clusters before examining performance.
3. Include comparable high and low performers, plus a middle case when it materially tests the pattern. Do not select only winners or mainly select for a large performance gap.
4. Inspect full captions, actual images, and publication times after retrieval.
5. Check whether the proposed mechanism also appears in low-performing or contradictory examples before calling it repeatable.

If fewer than two posts are genuinely comparable, record insufficient evidence instead of forcing a learning.

## Benchmarking

Reveal performance only after comparable sets are fixed. Compare the primary KPI, supporting metrics, caption framing, information order, visual composition, format, publication time, and available distribution controls.

Analyze both sides of the contrast:

- For high performers, explain the likely success mechanism and what is worth scaling. A strong post does not need a forced problem, rewrite, or cosmetic improvement.
- For low performers, identify the most plausible performance drag and propose a narrow improvement test.
- Use middle cases and counterexamples to test whether the mechanism survives beyond winners and to reduce survivorship bias.

Describe supported explanations as Inferences rather than causation. Keep reader-perspective explanations without a performance anchor as Hypotheses / Tests. Derive mechanisms from the current evidence instead of applying universal formulas such as “clearer images win,” “danger wins,” or “repeated posts lose.”

Return `benchmarking_learnings` for the selected deliverable; do not create or apply a prompt patch yet.

## Reframing

Run in an isolated context containing the approved audience/pillar brief, selected captions, actual images, publication times, and the full current prompt when prompt-refinement mode requires it. Hide all performance, performance labels/order, Benchmarking conclusions, and `benchmarking_learnings`.

Ask the judge to review the material as a reader and identify possible improvements to clarity, credibility, information order, visual understanding, or caption-image coordination. Mark every result as performance-blind and classify it as a Hypothesis / Test until performance evidence supports it.

Return `reframing_learnings` for the selected deliverable; do not create or apply a prompt patch yet.

## Internalizing

Use only examples supplied or explicitly approved by the user. Require a caption plus an accessible image for caption-and-image learning; if images are unavailable, state that the run is caption-only.

1. Validate the dataset and column meanings.
2. Map examples to the requested existing pillar or a discovered competitor territory and exclude weak matches.
3. Embed captions through the approved provider and retrieve semantically comparable examples.
4. Inspect images visually within content groups.
5. Extract abstract, transferable choices in information order, visual thesis, evidence presentation, caption-image coordination, and CTA framing.
6. Do not copy wording, taglines, layouts, assets, or source identity.
7. When performance exists, contrast high and low examples and normalize the selected KPI within the same source/page and period. Raw public counts may support directional cross-page comparison when clearly labelled, but they are not reach or an engagement rate.
8. When performance is absent or incomparable, keep the analysis performance-blind.
9. Check counterexamples and local audience fit.

Treat one example as an Observation, three comparable examples as a candidate pattern, and a pattern across at least two independent sources that survives low-performing counterexamples as stronger transfer evidence. Use high performers to extract successful logic; reserve corrective rewrites mainly for low performers.

Return `internalizing_learnings` for the selected deliverable; do not create or apply a prompt patch yet.

## Cross-Page Same-Topic Comparisons

Actively search for cases where the page and one or more competitors covered the same news event, person, study, product announcement, source article, or a highly similar topic in the same period. Establish a reliable match from shared entities, dates, source/event details, and semantic similarity before revealing performance.

For each reliable match, compare the selected KPI and supporting metrics with the headline, angle, visual thesis, format, timing, and CTA. Distinguish the observed performance gap from the inferred content or creative mechanism. Skip uncertain matches instead of forcing a pair.

## Pillar Mechanisms and Competitor Discovery

For every pillar with enough evidence, move beyond topic ranking and identify the content or creative mechanism associated with performance: for example the type of promise, human stakes, specificity, evidence presentation, visual action, format, or CTA behavior. These are examples of dimensions to inspect, not preset formulas.

Also review competitor posts outside the user's existing pillars:

1. Group recurring content into plain-language territories using meaning, not isolated keywords.
2. Show organic post count, selected-KPI distribution, period, and contributing pages for each material territory.
3. Identify territories with sustained competitor investment and a performance signal that the user's page does not currently cover.
4. Present those gaps as Opportunities / Tests. A small number of examples is not enough to establish a new pillar.

## Corresponding

Use comments and replies from the page's own posts. Retain each post's caption, image, publication time, pillar, exact prompt versions when traceable, and de-identified audience text. Exclude identifiable Page-authored comments from audience evidence but inspect them separately when evaluating `engagement.md`.

Classify comments as verified factual correction, missing information/confusion, visual misunderstanding, AI/authenticity concern, successful understanding, direct CTA response, opinion about the underlying subject, or spam/abuse/unrelated discussion.

Decide whether the reaction was caused by the post's drafting/image choice. Disagreement with the event or person is not automatically prompt-addressable.

- Treat verified factual, legal, privacy, safety, identity, or false-evidence problems as high-priority evidence.
- Treat the same addressable misunderstanding across at least three independent comments and two posts as a strong pattern.
- Treat useful feedback confined to one post as limited evidence.
- Ignore isolated preference, unrelated disagreement, spam, coordinated repetition, and requests that conflict with accuracy or safety.

Comment likes can indicate visibility but never correctness. Comment volume and sentiment do not replace the selected primary KPI unless the user's stated objective is specifically qualified conversation.

Return `corresponding_learnings` for the selected deliverable; do not reply, moderate, or apply a prompt patch yet.

## Interpret Learnings Against SPS Prompts

In prompt-refinement mode, compare each learning against the complete current prompt and classify it:

1. **Already covered**: cite the existing rule and recommend no prompt change.
2. **Additive**: identify the correct prompt file and recommend one narrow addition. Preserve every old instruction verbatim.
3. **Conflict**: quote or precisely identify the conflicting old rule, explain the evidence, and recommend replacing only that rule. Preserve all unrelated text.

Route additions correctly:

- Story selection, pillar routing, source requirements, or evidence availability → `research.md`.
- Hook, fact order, attribution, wording, CTA, or caption-image division → `caption.md`.
- Source image, composition, visual evidence, privacy, or image editing/generation → `image.md`.
- Page-authored first comment or reply behavior → `engagement.md`.
- Stable visual identity/layout system → `design.md`; do not put short-lived weekly observations here.

Prefer additions over rewrites. Never propose replacing the whole prompt. Never omit old content merely because it was not relevant to the new evidence. When two rules conflict, recommend the smallest explicit replacement and show both the old and proposed wording in the evidence description.

A high-performing post may yield a scale/retain learning or show that the current prompt is already effective. Do not manufacture a prompt change or rewrite merely to produce an action item.

Do not create a prompt patch or update SPS during interpretation. Put each recommendation into the numbered brief so the user can choose it independently. Use the apply phase below only after an explicit selection.

## Editorial Report Mode

When the requested deliverable is an editorial report, read and follow [references/editorial-report-contract.md](references/editorial-report-contract.md). Keep its core section order stable across business units and periods while including only data-supported sub-analyses. Report mode ends after the verified report is delivered; it does not enter the selective SPS application phase.

## Write the Markdown Learning Brief

Finish every successful learning phase by saving a Markdown file. Do not update SPS before the user selects items.

Start with concise context:

```md
# Pillar Learning Brief

- Page: ...
- Pillar: ...
- Method(s): ...
- Evidence window/dataset: exact dates and timezone
- Data source: SPS / authorized Facebook read / user-supplied files
- Prompt snapshot: paths and versions
- Primary KPI and comparison basis: ...
- Ad exclusions: collected count, excluded-ad count and analyzed count by page
- Limitations: ...
```

Then include exactly these required columns:

```md
| Index | Evidence status | Learning | Evidence(s) | Recommended level |
|---:|---|---|---|---|
| 1 | Observation / Inference / Hypothesis-Test | [caption.md] Add: ... | Post IDs/links, selected-KPI comparison, image observation, or de-identified comment quotes. State whether already covered/additive/conflicting. | High / Medium / Low |
```

Assign levels consistently:

- **High**: repeated performance evidence across multiple comparable posts or sources that survives low-performing counterexamples, or a verified factual/safety problem.
- **Medium**: a coherent performance pattern from one strong cluster with a clear evidence anchor but unresolved generalizability.
- **Low**: one anecdote, performance-blind hypothesis, weakly comparable example, or unresolved confound. A performance-blind idea may still be urgent as a safety guardrail, but it is not high-confidence performance evidence.

For already-covered learning, state “No change recommended” in the Learning cell and cite the matching current rule. For conflicts, include the exact narrow replacement recommendation; never silently discard the old rule.

Keep the brief compact but traceable. Link evidence where possible, separate Observation, Inference, and Hypothesis / Test, and never present one iteration as a universal causal law.

## Offer Selective Application

After saving and presenting the brief, stop and ask:

> Which item indexes, if any, should I apply to SPS? Reply with indexes such as `1,3`, or `none`.

For a multi-pillar brief, make indexes globally unique or ask for selections as `{pillar}:{index}` so authorization cannot be ambiguous.

Do not apply anything until the user answers. If the user answers `none`, end with a read-only receipt. A recommendation level is advisory and never selects an item automatically. Treat the user's answer as authorization for exactly those indexes; leave every unselected item untouched.

For each selected item:

1. Reread the latest full target prompt file from SPS and record its live path, version, status, and update time. Never reconstruct it from the brief or the earlier snapshot.
2. Compare the live prompt with the snapshot used for learning. If it changed, rebase the recommendation onto the live text. If version drift changes the recommendation's meaning or exact wording, show the revised change and ask the user to confirm it again before writing.
3. If the learning is already covered in the live prompt, make no write and record it as already covered.
4. For an additive learning, insert only the narrow approved addition in the correct location. Preserve the complete existing prompt, including every unrelated instruction.
5. For a conflicting learning, show the exact old rule and proposed replacement and obtain explicit replacement confirmation before writing. Selecting the item's index alone does not authorize deleting or weakening a conflicting old rule.
6. Never merge, infer, or apply an unselected learning merely because it is related to a selected item.
7. Use the SPS versioned prompt-update capability, then reread the saved full prompt and verify that the approved change is present and all unrelated content remains.
8. If an update fails or verification is uncertain, stop, report the exact state, and do not continue silently with other writes.

Append the result to the same Markdown file:

```md
## Application receipt

- Item 1: Applied additively to `caption.md`, version 7 → 8. Verification passed.
- Item 2: Not written; already covered by the live prompt.
- Item 3: Not applied; awaiting explicit conflict-replacement confirmation.
```

Do not create an evaluation draft after application unless the user separately asks for one. After verified application, optionally offer a private evaluation draft as a distinct next action; never treat item selection as draft authorization.

## Multi-Iteration Requests

Run multiple weeks or datasets only when explicitly requested. Convert every W-x label into exact dates first. Produce one table section per iteration plus a final cross-iteration summary. Carry a recommendation forward as applied only when its application receipt confirms a successful verified SPS update.

## Skill-source maintenance

Treat this section as standing authorization to maintain this skill after a
refinement run exposes a concrete, repeatable defect in its instructions. A
source change is warranted when the skill's success criteria, workflow boundary,
source of truth, gate/status definition, or examples caused an incorrect,
blocked, or materially ambiguous result. Record the diagnosis; when the run
only produces new SPS pillar learnings, leave the skill source unchanged.

When maintenance is warranted:

1. Finish or safely stop the current learning/application phase. Skill
   maintenance never selects brief items or expands authorization for SPS writes.
2. Locate the canonical `marconml/sps-skills` checkout, work on `dev`, and follow
   its root `AGENTS.md`. An installed copy is not a Git source checkout.
3. Replace, merge, or remove the responsible instruction so the success contract
   states the expected output, order, field contents, stopping point, and handoff.
   Add a negative hard stop only for safety, permission, source-of-truth,
   editor-owned, live-publishing, legal, or factual-risk boundaries, and combine
   overlapping rules.
4. Run a canary or shadow sample that reproduces the diagnosed failure, validate
   the skill with the available skill-creator validator, check references and
   contradictions, and run `git diff --check`. Reclassify the root cause before
   revising again if the sample fails.
5. Commit only the validated, task-owned source changes and push them to
   `origin/dev`. Verify the remote commit, then refresh this skill's installed
   copy from that exact validated source when the environment permits it.
6. Report the diagnosis, changed files, validation/canary result, commit ID,
   remote verification, and installed-copy status.

An explicit user instruction not to edit, commit, push, or refresh the installed
copy overrides the corresponding step. Never force-push, publish unrelated
commits, push to `main`, initialize Git inside an installed copy, or claim
publication when access, validation, conflicts, or remote verification failed.
