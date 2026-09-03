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

### `fix-monster-glyphs` · 怪獸字修復

Repairs malformed Chinese characters in images using exactly three steps:

1. **Find** a font library containing the verified character.
2. **Overlay** the correct glyph at the original position.
3. **Match** the surrounding lettering's weight, color, outline, shadow, and texture.

Supports Hong Kong Traditional Chinese glyphs and preserves the rest of the image.
Includes a practical style-matching guide. It does not require an SPS MCP connection.

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

For malformed-character repair, install:

```text
Use $skill-installer to install the skill from:
https://github.com/marconml/sps-skills/tree/main/fix-monster-glyphs
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

Or attach an image and specify the correct characters:

```text
Use $fix-monster-glyphs to correct the text to 「響咹」.
Follow Find → Overlay → Match and keep the original headline style.
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

For malformed-character repair:

```text
Update $fix-monster-glyphs from:
https://github.com/marconml/sps-skills/tree/main/fix-monster-glyphs

Back up and replace the existing installed copy.
```

## Contributing on `dev`

`dev` is the shared development branch; `main` remains the stable release branch.
Contributors need GitHub write access to this repository and working SSH access.
Creating the branch does not grant repository access.

For a new contributor checkout:

```bash
git clone --branch dev git@github.com:marconml/sps-skills.git
cd sps-skills
```

Read [AGENTS.md](AGENTS.md) before editing. Every user-requested skill-source
change should be validated, committed and pushed to `dev`, unless the user
explicitly opts out. Keep unrelated work out of commits; never force-push.
Merging or releasing to `main` is a separate action.

To install or update a development version, use the same instructions above but
replace `/tree/main/` with `/tree/dev/` in the skill URL. Pushing a change does not
automatically update already installed copies. Each skill includes a conditional
maintenance note so the source-editing rule travels with single-skill installs;
ordinary skill runs do not commit or push anything.

## Requirements

For the SPS-connected content and reference-image workflows:

- Social Page Studio MCP connection with access to the target page
- MCP-provided Facebook page history and lifetime reach
- MCP `generate_text_embedding` capability
- MCP `search_reference_images` and `submit_research` capabilities when image
  discovery or research media references are needed
- MCP prompt-version and draft capabilities

Those workflows do not use direct Facebook, LiteLLM, Azure, Serper, browser-search, or
other provider credentials. Provider access must remain behind Social Page Studio
MCP.

`fix-monster-glyphs` instead needs the source image, the intended correct text,
a suitable font library, and local font-rendering and image-compositing tools.
Fonts must be used under their applicable licenses; no fonts or user images are
bundled with the skill.
