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

## Install with Codex

Ask Codex:

```text
Use $skill-installer to install the skill from:
https://github.com/marconml/sps-skills/tree/main/refine-pillar-prompts
```

If the skill does not appear automatically, restart Codex.

## Use

Ask Codex:

```text
Use $refine-pillar-prompts to run one weekly Compare and Invent refinement
iteration for this SPS page.
```

## Update

Ask Codex:

```text
Update $refine-pillar-prompts from:
https://github.com/marconml/sps-skills/tree/main/refine-pillar-prompts

Back up and replace the existing installed copy.
```

## Requirements

- Social Page Studio MCP connection for SPS prompt and draft operations
- Facebook page history with reach data
- SPS MCP embeddings/clustering when available
- Configured LiteLLM embedding access only when SPS MCP embedding is unavailable

Do not store Facebook or LiteLLM credentials in this repository.
