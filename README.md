# SPS Skills

Reusable Codex skills for Social Page Studio workflows.

## Skills

### `refine-pillar-prompts`

Runs one weekly pillar-prompt refinement iteration using:

- Social Page Studio MCP-only history, reach, embeddings, and image references
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
imagery. Image discovery and research media references use Social Page Studio MCP
only.

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

- Social Page Studio MCP connection with access to the target page
- MCP-provided Facebook page history and lifetime reach
- MCP `generate_text_embedding` capability
- MCP `search_reference_images` and `submit_research` capabilities when image
  discovery or research media references are needed
- MCP prompt-version and draft capabilities

The skills do not use direct Facebook, LiteLLM, Azure, Serper, browser-search, or
other provider credentials. Provider access must remain behind Social Page Studio
MCP.
