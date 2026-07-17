# SPS Skills

Reusable Codex skills for Social Page Studio workflows.

## Skills

### `refine-pillar-prompts`

Runs one weekly pillar-prompt refinement iteration using:

- content-similar Facebook post pairs or clusters
- reach-aware Compare analysis
- performance-blind Invent analysis
- minimal versioned SPS prompt updates
- one evaluation draft per pillar

The default analysis window is the immediately previous seven days. Multiple
weekly iterations run only when explicitly requested.

### `find-reference-image`

Finds and verifies the strongest factual reference image for user-supplied text.
It extracts real visual anchors, improves weak search queries, inspects candidate
sources, ranks exact matches, and returns `no_match` instead of unrelated generic
imagery.

## Install with Codex

Ask Codex:

```text
Use $skill-installer to install the skill from:
https://github.com/marconml/sps-skills/tree/main/refine-pillar-prompts
```

For reference-image search, install:

```text
Use $skill-installer to install the skill from:
https://github.com/marconml/sps-skills/tree/main/find-reference-image
```

If the skill does not appear automatically, restart Codex.

## Use

Ask Codex:

```text
Use $refine-pillar-prompts to run one weekly Compare and Invent refinement
iteration for this SPS page.
```

Or provide source text directly:

```text
Use $find-reference-image to find the best factual reference image for this text:
[paste text]
```

## Update

Ask Codex:

```text
Update $refine-pillar-prompts from:
https://github.com/marconml/sps-skills/tree/main/refine-pillar-prompts

Back up and replace the existing installed copy.
```

For reference-image search:

```text
Update $find-reference-image from:
https://github.com/marconml/sps-skills/tree/main/find-reference-image

Back up and replace the existing installed copy.
```

## Requirements

- Social Page Studio MCP connection for SPS prompt and draft operations
- Facebook page history with reach data
- SPS MCP embeddings/clustering when available
- Configured LiteLLM embedding access only when SPS MCP embedding is unavailable
- An available image-search/browser tool, or `SERPER_API_KEY` for the bundled
  Serper helper

Do not store Facebook, LiteLLM, or Serper credentials in this repository.
