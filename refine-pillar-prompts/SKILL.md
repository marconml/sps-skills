---
name: refine-pillar-prompts
description: "Improve Social Page Studio (SPS) pillar prompts from one week of Facebook history using SPS MCP-only data, text embeddings, image discovery, prompt storage, and drafts, with reach-aware Compare and performance-blind Invent analysis. Use when Codex is asked to refine, improve, learn, or self-improve one or more existing SPS pillar prompts from similar Facebook posts, compare reach differences, or create one evaluation draft per pillar. Run one weekly iteration by default; run multiple weeks only when the user explicitly requests it."
---

# Refine Pillar Prompts

Run one evidence-traceable refinement iteration for each requested existing SPS pillar.

## Defaults

- Analyze only the immediately previous 7 days. Do not fetch W-2, W-3, W-4, or other older windows unless the user explicitly requests a multi-iteration run.
- Run exactly one iteration. If the user requests multiple weeks, repeat this single-iteration workflow in chronological order, one week at a time.
- Use Facebook reach as the only performance KPI. Ignore engagement, reactions, comments, shares, and clicks when deciding which post performed better.
- Use existing SPS pillars and their current prompts. Do not invent a new pillar taxonomy.
- Create evaluation posts as drafts only. Do not approve, schedule, or publish unless the user explicitly requests that separately.
- Preserve full captions in the evidence report so the user can understand each comparison.

## Resolve Inputs

Determine:

1. SPS page and Facebook page.
2. Requested pillars; if omitted, use all enabled pillars on the SPS page.
3. The 7-day analysis window; default to the preceding 7 days ending now.
4. Whether SPS MCP exposes the required page history, reach, embedding, image-reference, prompt, and draft capabilities for this agent.

Snapshot every pillar's initial prompt before analysis.

## MCP-Only Provider Boundary

Use the persistent Social Page Studio MCP as the only provider for this workflow:

1. Read page context, enabled pillars, current prompts, Facebook post history, lifetime reach, and actual post-image URLs through SPS MCP.
2. Generate every caption/content embedding with `generate_text_embedding`. Use the returned vector only for this analysis and preserve the MCP metadata receipt when available.
3. Compute deterministic cosine similarity or clustering locally from MCP-returned vectors when SPS does not expose a clustering tool. Local similarity math is allowed; generating vectors outside MCP is not.
4. Use actual post images returned through SPS MCP for Compare and Invent inspection. If a new reference-image search is necessary, use `search_reference_images` and carry the selected reference through `submit_research` or `attach_reference_image` as appropriate.
5. Apply prompt updates and create evaluation drafts through SPS MCP.

Do not use LiteLLM, OpenAI or Azure directly, a local embedding model, sentence-transformers, Facebook Graph API directly, Serper directly, browser/general web image search, bundled search scripts, or any other custom provider or fallback.

Treat providers behind SPS MCP as server-owned and opaque. Never read or require provider API keys. If a required MCP capability is unavailable, disabled, or denied, stop and report the exact tool, organization setting, or scope that is missing; do not bypass MCP.

## Build Comparable Sets

For every post in the 7-day window, retain:

- post ID and permalink
- full caption/content
- actual image or image URL when present
- publication time, normalized to the page's timezone
- lifetime reach as currently returned by Facebook

Assign posts to the closest existing pillar from their meaning and the pillar prompt. Exclude ambiguous posts rather than forcing membership.

Create one content embedding per post from the caption/content only. Use embeddings only to retrieve semantically comparable posts; do not include reach, image, or publication time in the embedding input.

Within each pillar:

1. Cluster or rank posts by content similarity.
2. Select the closest useful pairs or small clusters before examining reach differences.
3. Prefer up to three high-similarity comparisons with distinct posts. Never select a pair mainly because it has a large reach gap.
4. After retrieval, inspect the full captions, actual images, and publication times with visual and audience reasoning. Do not treat image-embedding distance as human visual similarity.

If a pillar has fewer than two genuinely comparable posts, record insufficient comparison evidence and keep that mode's prompt patch empty.

## Mode A: Compare

For each selected pair or cluster, reveal reach and compare:

- full caption and framing
- information order and drafting choices
- actual visual composition and what the audience sees first
- publication time
- reach and reach difference

Start from the audience's likely experience. Explain why the higher-reach post may have been more immediately understandable, relevant, curiosity-producing, or emotionally legible than the lower-reach post.

Do not begin with predefined claims such as "clearer images win," "danger wins," or "repeated posts lose." Derive each hypothesis from the actual matched posts. Treat explanations as hypotheses, not proven causation.

Produce a minimal `compare_patch` against the initial pillar prompt. Each added or changed rule must cite the matched evidence that motivated it. Leave unrelated prompt text unchanged.

## Mode B: Invent

Run this mode in an isolated context. Provide:

- the initial pillar prompt
- the selected semantically similar captions
- the actual images
- publication times

Do not provide reach, performance labels, ordering by performance, Compare conclusions, or the `compare_patch`. Ask the judge to reason only from an audience perspective and identify concrete improvements to the content drafting or image-generation instructions.

Produce a minimal `invent_patch` against the same initial prompt. Do not claim that an invented rule is performance-proven.

## Produce the Final Prompt

Reconcile both independent patches:

1. Remove duplicates and keep changes local to the relevant pillar.
2. Preserve existing constraints that the evidence does not address.
3. Prefer measured Compare evidence when an Invent suggestion conflicts with it.
4. Record rejected or conflicting rules instead of silently applying them.
5. Apply the resulting minimal change to the versioned SPS pillar prompt through MCP.

Do not replace the whole prompt merely to incorporate a small learned rule.

## Create One Evaluation Draft per Pillar

Generate one new draft using each final prompt. The draft should make the newly applied rules visible in normal use.

Append this note to the caption:

```text
*Week {window_label} - {pillar}: applied learned rules {concise_rule_list}*
```

Keep the post in draft state unless the user explicitly asks to approve, schedule, or publish it.

## Report

For each pillar, show:

1. Analysis window and number of usable posts.
2. Each Compare pair/cluster: full captions, image links/previews, publication times, reach, similarity, observed differences, and the resulting hypothesis.
3. Invent evidence: full captions, image links/previews, publication times, and confirmation that performance was hidden from the judge.
4. Compare learning and `compare_patch`.
5. Invent learning and `invent_patch`.
6. Conflicts or rejected rules.
7. Initial prompt and final prompt, preferably as a compact diff plus full final text.
8. Evaluation draft ID/link and its caption.

Clearly separate observed facts from interpretation. Do not present a one-week pattern as a universal causal law.

## Multi-Week Requests

Only when the user explicitly asks for multiple iterations, run the same workflow once per requested week, oldest to newest. Carry the final prompt from one iteration into the next, preserve every version, create one evaluation draft per pillar per week, and report the initial prompt from the first iteration and final prompt from the last.
