---
name: refine-pillar-prompts
description: "Refine versioned Social Page Studio pillar prompts from approved performance evidence through Benchmarking, Reframing, Internalizing, and Corresponding. Use for a numbered prompt-learning brief and selectively apply only user-chosen items. Use chief-editor-review instead for a management editorial report."
---

# Refine Pillar Prompts

Improve one or more SPS pillar prompts from traceable evidence. This skill owns prompt learning and selective SPS application; it does not produce a Chief Editor report or run paid Facebook collection.

If the user requests a recurring Facebook performance review, competitor review, CEO readout, or standalone HTML report, use `chief-editor-review`. Its evidence package or findings may later be supplied here as approved input.

## Success contract

Find repeatable content and creative mechanisms associated with the user's selected social-performance outcome. Accuracy, privacy, legal compliance, and source fidelity are guardrails rather than performance claims.

Label every material conclusion:

- **Observation**: directly supported by approved evidence, with metric, period, sample/post count, and links or IDs where relevant.
- **Inference**: a reasonable explanation anchored to observations, with confounders and counterexamples stated.
- **Hypothesis / Test**: performance-blind judgement, reader perspective, single example, or otherwise unverified proposal.

Only Observations and evidence-anchored Inferences may be presented as performance findings.

## Confirm the refinement brief

Ask only for missing information, then wait for confirmation before data access:

1. SPS workspace/team, page, pillar or pillars, and page timezone.
2. Primary performance objective and the metric definition or denominator when relevant.
3. Exact evidence dates. Translate W-1/W-2 labels into dates.
4. Requested methods: Benchmarking, Reframing, Internalizing, Corresponding, or a combination.
5. Evidence source: SPS history, user-supplied exports, or an approved `chief-editor-review` evidence package.
6. Permission to read the current full prompt files and their versions.
7. Desired learning-brief language and destination.

If required performance fields, images, prompt snapshots, permissions, or evidence coverage are unavailable, identify the missing item and stop. For new or refreshed external Facebook collection, hand off to `chief-editor-review` or ask for an approved export; do not improvise a paid collection inside this skill.

## Read source-of-truth prompts

Read every current prompt file relevant to the selected method. Keep a snapshot containing the page, pillar, full text, path, purpose, version/status/update time, evidence window, and timezone.

Typical ownership:

- `research.md`: selection, routing, sourcing, and evidence rules.
- `caption.md`: hook, framing, information order, wording, attribution, and CTA.
- `image.md`: source-image choice, visual evidence, composition, privacy, and image generation/editing.
- `engagement.md`: Page-authored first comments and replies.
- `design.md`: stable visual identity and layout.

Never infer the prompt from a summary or overwrite unrelated instructions.

## Analyze the evidence

Read and follow [the prompt-analysis contract](references/prompt-analysis-contract.md). Apply the four methods in the confirmed scope:

- **Benchmarking** compares genuinely similar high, middle, and low performers after the comparable set is fixed.
- **Reframing** reviews captions and images with performance hidden to generate hypotheses.
- **Internalizing** extracts transferable logic from approved competitor examples without copying.
- **Corresponding** uses de-identified reader feedback and inspects Page-authored replies separately.

Use local deterministic matching or an approved SPS embedding capability. Never silently send content to an outside embedding provider.

## Interpret findings against the live prompts

Classify each learning:

1. **Already covered**: cite the current rule and recommend no prompt change.
2. **Additive**: name the correct prompt file and propose one narrow addition.
3. **Conflict**: identify the exact old rule and propose the smallest replacement while preserving unrelated text.

High-performing content may confirm that an existing rule should be retained or scaled. Do not manufacture a rewrite merely to create an action item.

## Deliver the learning brief

Save a compact Markdown brief before any SPS write:

```md
# Pillar Learning Brief

- Page / pillar: ...
- Methods: ...
- Evidence window and timezone: ...
- Primary KPI and comparison basis: ...
- Evidence source and limitations: ...

| Index | Evidence status | Learning | Evidence | Recommended level |
|---:|---|---|---|---|
| 1 | Observation / Inference / Hypothesis-Test | [caption.md] Add: ... | Links/IDs, comparison and prompt-coverage status | High / Medium / Low |
```

Use **High** for repeated evidence that survives counterexamples or a verified factual/safety issue, **Medium** for one coherent anchored pattern with unresolved generalizability, and **Low** for limited or performance-blind evidence.

Then stop and ask:

> Which item indexes, if any, should I apply to SPS? Reply with indexes such as `1,3`, or `none`.

## Apply only selected items

Treat the reply as authorization for exactly those indexes.

For every selected item:

1. Reread the latest full target prompt and compare it with the learning snapshot.
2. If version drift changes the recommendation, show the rebased change and obtain confirmation again.
3. Make only the selected narrow addition. For a conflict, obtain explicit confirmation of the exact replacement.
4. Use the SPS versioned update capability, reread the saved prompt, and verify that unrelated content remains.
5. Stop on an uncertain or failed write rather than continuing silently.

Append an application receipt to the same brief with old/new versions and verification status. Evaluation drafts are separate and require a separate request.

## Safety boundaries

- Never request, print, log, report, or commit access tokens.
- De-identify audience comments.
- Prompt-learning approval does not authorize publishing, scheduling, replies, moderation, or evaluation drafts.
- A recommendation level never selects an item automatically.
- Do not apply a report recommendation directly to SPS; it must first appear as a numbered learning item here.

## Skill-source maintenance

The user has granted standing authorization to maintain this skill when an actual refinement run reveals a concrete, repeatable defect in its success criteria, workflow boundary, source-of-truth rule, gate/status definition, scripts, or examples. One-off pillar findings do not automatically become universal skill rules.

When maintenance is warranted:

1. Safely finish or stop the active SPS phase.
2. Edit the canonical `marconml/sps-skills` checkout on `dev`, following its root `AGENTS.md`.
3. Replace, merge, or remove the responsible rule; prefer a positive success contract over accumulated prohibitions.
4. Run a reproducing canary, the skill validator, relevant tests, contradiction/reference checks, secret review, and `git diff --check`.
5. Commit only validated task-owned changes, push to `origin/dev`, verify the remote commit, and refresh the installed copy from that exact source.
6. Report the diagnosis, files, tests, commit, remote verification, and installed-copy status.

Stop without pushing if validation, conflicts, access, or remote verification fails. Never force-push or push to `main` under this standing authorization.
