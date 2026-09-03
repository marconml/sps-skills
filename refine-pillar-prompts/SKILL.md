---
name: refine-pillar-prompts
description: "Analyze existing Social Page Studio (SPS) pillar prompts through explicitly selected evidence methods: Benchmarking compares similar internal posts using reach differences; Reframing proposes performance-blind improvements from an audience perspective; Internalizing extracts transferable caption and image lessons from user-supplied external examples; Corresponding learns from comments on the page's own posts. Use when Codex is asked to refine, improve, learn, or self-improve one or more SPS pillar prompts. Explain SPS and week labels to newcomers, ask for all missing access and source information before using tools, and first produce a numbered Markdown learning brief without SPS writes. Then ask which item indexes the user wants to apply and update only those explicitly selected items. When a run exposes a repeatable defect in this skill's own instructions, maintain its canonical dev source under the skill-source maintenance contract."
---

# Refine Pillar Prompts

Run one evidence-traceable learning iteration for each requested pillar in two phases. Phase 1 is SPS-read-only: ask for context, analyze the evidence, and write a numbered Markdown brief without changing SPS. The Markdown brief is the only permitted output write in this phase. Phase 2 may update versioned SPS prompts, but only after the user selects exact item indexes from that brief. Never infer approval from a recommendation level. Evaluation drafts are a separate optional action and require a separate user request.

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

- **Benchmarking**: retrieve genuinely similar posts from the same page, then use reach differences to form observational improvement hypotheses.
- **Reframing**: hide all performance information and review similar captions/images as a reader to find clarity, trust, or presentation improvements.
- **Internalizing**: study examples supplied by the user from other sources and extract transferable craft without copying wording, assets, layouts, or brand identity.
- **Corresponding**: study comments and replies on the page's own posts to find verified corrections, misunderstandings, visual-trust problems, and successful communication.

Treat the legacy name **Compare** as **Benchmarking** and **Invent** as **Reframing**.

## Mandatory Preflight

Before any tool call or data access, check what the user has already supplied and ask for every missing item. Group the questions concisely and explain unfamiliar terms. Wait for the answers; do not silently assume values.

Ask for:

1. **Method**: Benchmarking, Reframing, Internalizing, Corresponding, or an explicit combination.
2. **Target**: page/brand and pillar in plain language. If SPS is connected, ask for the workspace/team, agent connection, page slug/name, and pillar slug/name. If the user does not know these identifiers, ask permission to list accessible SPS pages and pillars read-only.
3. **Prompt source**: permission to read the current full prompt files from SPS, or exported prompt files supplied by the user. Record paths, versions, status, and timezone.
4. **Evidence range**: exact dates and timezone. If the user says W-x, translate it into exact dates and ask for confirmation.
5. **Data access**:
   - Ask whether SPS exposes the required history, reach, images, embeddings, or comments for the selected methods.
   - If Facebook data is required and SPS does not expose it, ask whether direct read-only Meta Graph API access is allowed and whether `META_PAGE_ID` plus `META_PAGE_ACCESS_TOKEN` are available in an environment file or secret store.
   - Never ask the user to paste an access token into chat. Never print, log, copy into a report, or commit a token.
   - Explain that Benchmarking usually needs post history, images, publication times, and lifetime reach; Corresponding needs posts, comments, and replies. Required Page permissions vary, so capability-test read-only access before analysis.
6. **Method-specific material**:
   - Benchmarking: which Facebook Page/history source and which performance field means reach.
   - Reframing: which post set should be judged with performance hidden.
   - Internalizing: CSV/file location, source identities, column meanings, image locations, metric meanings, and whether external performance is comparable.
   - Corresponding: comment source, whether replies are included, how Page-authored comments are identified, and whether commenter data must be further de-identified.
7. **Brief destination**: where to save the Markdown learning brief. If the user has no preference, propose `pillar-learning-brief-{pillar}-{YYYY-MM-DD}.md` in the current workspace and obtain confirmation.

If a required answer, permission, prompt snapshot, image, metric definition, or data capability is missing, stop before analysis and report exactly what remains missing.

## Safety and Data Boundaries

- Prefer SPS MCP for current prompts, internal history, embeddings, image references, and comments when those read capabilities are available.
- Allow user-supplied CSV files, exported prompts, attached images, and image URLs as evidence for Internalizing.
- Allow direct Facebook Page-token reads only after explicit user authorization and only when SPS lacks the required read capability. Use them read-only.
- Generate text embeddings through SPS MCP when available. If unavailable, ask the user how to proceed; never silently choose an outside embedding provider.
- Compute deterministic clustering or cosine similarity locally from approved embeddings.
- Inspect actual images visually. Do not treat image-embedding distance as human visual similarity.
- De-identify audience comments. Do not retain commenter names unless the user establishes a necessary, lawful reason.
- Do not reply, moderate, approve, schedule, publish, create evaluation drafts, update prompts, or make any other external change during the learning phase.
- Treat prompt application as a separate, user-authorized phase inside this skill. Create an evaluation draft only when the user requests it separately; selecting a learning item does not authorize draft creation.

## Read the Full Current Prompt

Before learning, read every current prompt file relevant to the selected method. Never interpret a pillar from a shortened summary alone.

Keep a complete snapshot containing:

- page and pillar
- prompt path and purpose
- full current text
- version/status/update time
- evidence window and timezone

Use the full snapshot to check whether a proposed learning is already present, adds something genuinely new, or conflicts with an old instruction.

## Build Internal Comparable Sets

Use this section for Benchmarking and Reframing.

For every eligible post, retain the post ID/permalink, full caption, actual image, publication time in the page timezone, pillar assignment, and reach when available. Keep reach hidden until Benchmarking explicitly reveals it.

Assign posts to the closest existing pillar from meaning and the current full pillar prompt. Exclude ambiguous posts.

Embed caption/content only; never put reach, image, or publication time into the embedding input. Within each pillar:

1. Rank or cluster posts by semantic similarity.
2. Select useful pairs or small clusters before examining reach.
3. Prefer up to three high-similarity comparisons with distinct posts. Never select mainly for a large reach gap.
4. Inspect full captions, actual images, and publication times after retrieval.

If fewer than two posts are genuinely comparable, record insufficient evidence instead of forcing a learning.

## Benchmarking

Reveal reach only after comparable posts are fixed. Compare caption framing, information order, visual composition, publication time, reach, and reach difference.

Reason from the audience's likely experience, but describe the explanation as an observational hypothesis rather than causation. Check counterexamples and avoid predefined universal rules such as “clearer images win,” “danger wins,” or “repeated posts lose.”

Return `benchmarking_learnings` for the brief; do not create or apply a prompt patch yet.

## Reframing

Run in an isolated context containing the full current prompt, selected captions, actual images, and publication times. Hide reach, performance labels/order, Benchmarking conclusions, and `benchmarking_learnings`.

Ask the judge to review the material as a reader and identify concrete improvements to clarity, credibility, information order, visual understanding, or caption-image coordination. Mark every result as performance-blind.

Return `reframing_learnings` for the brief; do not create or apply a prompt patch yet.

## Internalizing

Use only examples supplied or explicitly approved by the user. Require a caption plus an accessible image for caption-and-image learning; if images are unavailable, state that the run is caption-only.

1. Validate the dataset and column meanings.
2. Map examples to the requested existing pillar and exclude weak matches.
3. Embed captions through the approved provider and retrieve semantically comparable examples.
4. Inspect images visually within content groups.
5. Extract abstract, transferable choices in information order, visual thesis, evidence presentation, caption-image coordination, and CTA framing.
6. Do not copy wording, taglines, layouts, assets, or source identity.
7. When performance exists, compare like-for-like examples and normalize within the same source/page and period. Never compare raw reach across differently sized pages or treat public likes/comments as reach.
8. When performance is absent or incomparable, keep the analysis performance-blind.
9. Check counterexamples and local audience fit.

Treat one example as an observation, three comparable examples as a candidate pattern, and a pattern across at least two independent sources that survives counterexamples as stronger transfer evidence.

Return `internalizing_learnings` for the brief; do not create or apply a prompt patch yet.

## Corresponding

Use comments and replies from the page's own posts. Retain each post's caption, image, publication time, pillar, exact prompt versions when traceable, and de-identified audience text. Exclude identifiable Page-authored comments from audience evidence but inspect them separately when evaluating `engagement.md`.

Classify comments as verified factual correction, missing information/confusion, visual misunderstanding, AI/authenticity concern, successful understanding, direct CTA response, opinion about the underlying subject, or spam/abuse/unrelated discussion.

Decide whether the reaction was caused by the post's drafting/image choice. Disagreement with the event or person is not automatically prompt-addressable.

- Treat verified factual, legal, privacy, safety, identity, or false-evidence problems as high-priority evidence.
- Treat the same addressable misunderstanding across at least three independent comments and two posts as a strong pattern.
- Treat useful feedback confined to one post as limited evidence.
- Ignore isolated preference, unrelated disagreement, spam, coordinated repetition, and requests that conflict with accuracy or safety.

Comment likes can indicate visibility but never correctness. Comment volume and sentiment do not replace reach as the performance KPI.

Return `corresponding_learnings` for the brief; do not reply, moderate, or apply a prompt patch yet.

## Interpret Learnings Against SPS Prompts

For each learning, compare it against the complete current prompt and classify it:

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

Do not create a prompt patch or update SPS during interpretation. Put each recommendation into the numbered brief so the user can choose it independently. Use the apply phase below only after an explicit selection.

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
- Limitations: ...
```

Then include exactly these required columns:

```md
| Index | Learning | Evidence(s) | Recommended level |
|---:|---|---|---|
| 1 | [caption.md] Add: ... | Post IDs/links, reach comparison, image observation, or de-identified comment quotes. State whether already covered/additive/conflicting. | High / Medium / Low |
```

Assign levels consistently:

- **High**: verified factual/safety problem, or repeated independent evidence across multiple comparable posts/sources with no unresolved counterexample.
- **Medium**: coherent evidence from one strong cluster or repeated reactions within one post, but not yet stable across posts/sources.
- **Low**: one anecdote, performance-blind hypothesis, weakly comparable example, or unresolved confound.

For already-covered learning, state “No change recommended” in the Learning cell and cite the matching current rule. For conflicts, include the exact narrow replacement recommendation; never silently discard the old rule.

Keep the brief compact but traceable. Link evidence where possible, state observed facts separately from interpretation, and never present one iteration as a universal causal law.

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
