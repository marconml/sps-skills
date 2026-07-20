---
name: find-reference-image
description: Find and verify the strongest factual reference image for user-supplied text through Social Page Studio MCP only by extracting real visual anchors, refining image-search queries, inspecting returned provenance, and rejecting generic or unrelated imagery. Use when asked to find, choose, verify, rank, or improve a reference image or image-search query for a news story, social post, article, film or TV item, person, event, place, or official statement.
---

# Find Reference Image

Return one strong, factual image reference or an explicit `no_match`. Never fill a gap with an attractive but unrelated image.

## Provider Boundary

Use Social Page Studio (SPS) MCP as the only image-search provider and the only route for carrying a found reference into SPS.

- Search with `search_reference_images` in the persistent `social_page_studio` MCP.
- Preserve its `receiptId`, result ID, image URL, and source-page URL.
- When the reference belongs to new research, pass the chosen URL and source-page URL through `submit_research` using `candidates[].mediaReferences` or `providedMediaReferences`.
- When attaching a search result to an existing candidate or post, use `attach_reference_image` only when that MCP tool and scope are available.
- Do not call Serper, Google Images, Bing, a browser image search, general web search, a bundled helper, or any direct/custom image-search API.
- Treat the provider behind SPS MCP as server-owned and opaque. Do not bypass MCP to call that provider directly.
- If SPS MCP image search is unavailable, disabled, or denied, stop with `no_match` and report the exact MCP capability or scope that is missing. Do not fall back to another provider.

## Workflow

1. Treat the user's text as the source of truth. Ask a question only when an essential identity or event is genuinely ambiguous.
2. Extract concrete visual anchors: named people or organizations, the specific event or action, exact place, official notice or document, actual scene, work, or character.
3. Build a retrieval query from two to five discriminative factual terms:
   - Use official or common Traditional Chinese for Hong Kong people, organizations, places, and local events.
   - Use the official English name for Western people and works. Mix languages when that best identifies the subject.
   - Add an event, action, place, or date only when it improves identity or freshness.
   - Do not add invented visual details or style words such as `blurred`, `background`, `generic`, `street view`, `dramatic`, `silhouette`, `stock photo`, `illustration`, or `cinematic`.
4. Search through SPS MCP, inspect, and adjust. Make at most three query attempts:
   - Start with the strongest real-world anchor.
   - If results show the wrong subject, add the full name plus the event, place, or date.
   - If results are generic, remove style terms and add the real action, official statement, or source organization.
   - If results are outdated, add the relevant year or date.
   - If results are noisy, add an official domain or source type.
   - Record how and why each query changed.
5. Inspect the preview and provenance returned by SPS MCP. If MCP does not return enough evidence to verify identity, event, date, and source page, reject the candidate. Do not open a browser or use another search provider as a fallback.
6. Rank candidates and select the best valid result.

## MCP Tools

Use only these SPS MCP routes:

1. `get_image_search_strategy` when page or pillar search rules are needed.
2. `search_reference_images` for each query attempt.
3. `submit_research` to persist new research with the selected media reference.
4. `attach_reference_image` only for an existing candidate or post.

Never require or read a local image-search API key.

## Selection Rules

Prefer candidates in this order:

1. An image supplied by the user or the original source article/post.
2. An official page, post, statement, press release, or press kit.
3. A reputable editorial photo of the exact subject and event.
4. A clean secondary source that clearly matches the facts.

Score each valid candidate out of 10:

- Exact factual match: 0–4
- Source authority and traceable provenance: 0–3
- Composition and usable resolution: 0–2
- Clean image without unnecessary overlays: 0–1

Reject a candidate regardless of score when it shows the wrong identity, event, date, or place. Also reject generic stock imagery, AI-generated or synthetic scenes, misleading composites, Street View unless the story is specifically about that view, unsafe graphic material, inaccessible sources, and images with no credible provenance. Prefer a clean image over a watermarked or text-covered copy when both show the same scene.

If no suitable candidate exists after three searches, return `no_match`, list the queries tried, and explain why. Do not substitute generic scenery or create a synthetic scene.

## Output

Return:

```yaml
status: selected | no_match
query_used: "..."
search_receipt_id: "..."
query_adjustments:
  - "query -> reason for change"
selected:
  result_id: "..."
  image_url: "..."
  source_page_url: "..."
  title: "..."
  source: "..."
  reason: "..."
  score: 0
alternates: [] # maximum two
cautions: []
```

Selecting a reference does not grant usage rights. Preserve the source URL and state any licensing or attribution uncertainty.

## Query Example

For a local SPCA story, reject `Hong Kong SPCA building street view blurred`: it invents a building scene and asks for a visual style. Prefer `香港愛護動物協會 虐狗影片 下架 聲明`, which searches for the actual organization, action, and statement.
