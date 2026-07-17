---
name: find-reference-image
description: Find and verify the strongest factual reference image for user-supplied text by extracting real visual anchors, refining image-search queries, inspecting candidate source pages, and rejecting generic or unrelated imagery. Use when asked to find, choose, verify, rank, or improve a reference image or image-search query for a news story, social post, article, film or TV item, person, event, place, or official statement.
---

# Find Reference Image

Return one strong, factual image reference or an explicit `no_match`. Never fill a gap with an attractive but unrelated image.

## Workflow

1. Treat the user's text as the source of truth. Ask a question only when an essential identity or event is genuinely ambiguous.
2. Extract concrete visual anchors: named people or organizations, the specific event or action, exact place, official notice or document, actual scene, work, or character.
3. Build a retrieval query from two to five discriminative factual terms:
   - Use official or common Traditional Chinese for Hong Kong people, organizations, places, and local events.
   - Use the official English name for Western people and works. Mix languages when that best identifies the subject.
   - Add an event, action, place, or date only when it improves identity or freshness.
   - Do not add invented visual details or style words such as `blurred`, `background`, `generic`, `street view`, `dramatic`, `silhouette`, `stock photo`, `illustration`, or `cinematic`.
4. Search, inspect, and adjust. Make at most three query attempts:
   - Start with the strongest real-world anchor.
   - If results show the wrong subject, add the full name plus the event, place, or date.
   - If results are generic, remove style terms and add the real action, official statement, or source organization.
   - If results are outdated, add the relevant year or date.
   - If results are noisy, add an official domain or source type.
   - Record how and why each query changed.
5. Inspect the candidate's source page and preview. Do not trust only a thumbnail or result title.
6. Rank candidates and select the best valid result.

## Search Tools

Prefer an available image-search or browser tool. If none is available and `SERPER_API_KEY` is configured, run the bundled helper from this skill's directory:

```bash
python3 scripts/search_images.py --query '香港愛護動物協會 虐狗影片 下架 聲明' --limit 10
```

The helper uses Hong Kong and Traditional Chinese search localization by default. Never print, return, or store the API key.

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
query_adjustments:
  - "query -> reason for change"
selected:
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
