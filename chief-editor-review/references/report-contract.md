# Chief Editor Report Contract

Read this reference whenever the deliverable is a Chief Editor, CEO, management, or recurring editorial review.

## Editorial voice

Write for a time-poor Chief Editor. Lead with editorial judgement: what changed in story choice or packaging, why it matters, and what to commission next. Metrics prove or bound the judgement; they are not the card headline unless the number itself changes the decision.

Keep process notes, agent instructions, selection mechanics, causal disclaimers, exclusions, and detailed data limitations in the methodology/trust layer. A short lead beneath a section heading must contain a decision-useful takeaway.

## Opening basis

Use a compact scope band for the exact period/timezone, focal and competitor set, audience, primary KPI, and current-month comparison basis. Named competitor omissions, ad counts, and collection receipts belong in Methodology / Caveats unless they materially change the headline conclusion.

The hero should communicate the principal performance decision, business implication, and one evidence anchor in roughly 30 seconds.

## 1. Executive Summary / Editorial Calls

Give two to four calls for the next cycle. Each card contains:

- the commissioning, mix, or packaging decision;
- why it matters in editorial language;
- one compact evidence anchor or a Hypothesis / Test label;
- an unambiguous action status.

Define the complete status set once. Default meanings:

- **Scale**: increase allocation behind a supported mechanism.
- **Improve**: retain the editorial product but redesign its selection or package.
- **Stop**: cease a content, creative, or distribution practice when evidence supports doing so.
- **Test**: run a bounded experiment where evidence is promising but incomplete.

Do not use Stop for analytical warnings such as calling engagement reach or treating medians as causal.

## 2. Current-Month Movement & Diagnosis

Make the current month the narrative subject. Use the prior two months to classify its movement as continuation, reversal, or break. Explain what carried it, what dragged it, and whether competitor movement suggests an internal editorial issue or a broader market/news-cycle signal.

Use median primary-KPI performance to represent the typical post. Show total performance separately as an output/scale signal and always show post count. Average may appear only when it adds a distinct explanation and is labelled as breakout-sensitive.

For three monthly observations, a clean multi-page line/slope chart is suitable when:

- the y-axis and metric are explicit;
- the current month is visually emphasized;
- exact values and post counts remain available;
- lines and legend remain readable with all approved competitors;
- the chart is described as a rolling three-month comparison, not a long-run trend.

Check every bar/line length against its exact value. Make the strongest comparator's median conspicuous rather than burying it in body copy.

### Standard comparison modules

Part 2 always includes two compact comparison modules, collapsed by default in standalone HTML and marked for QA with `data-module="page-scorecard"` and `data-module="core-pillar-comparison"`. When the output format cannot collapse content, use two equivalently labelled compact blocks.

1. **Page-level scorecard**: include every approved page, the stated comparison period, organic analyzed post count, median primary KPI, total primary KPI, and one concise editorial read. Add breakout concentration only when it changes interpretation.
2. **Core-pillar comparison and Chief Editor calls**: include every focal-page Core pillar, decision-month output and median primary KPI, the prior-two-month baseline, the strongest relevant comparator with its median and post count, and a Scale / Improve / Stop / Test call with a short editorial reason.

These modules are the reusable diagnostic index across business units and months. Keep the main narrative selective; place detailed rows inside the modules. If a required value is unavailable, keep the module and label the field unavailable with its coverage limitation.

## 3. Why Readers Shared — and What They Asked For

This is the main analytical section. Organize it around up to three editorial mechanisms or opportunities, not around a list of charts.

For each mechanism:

1. **Observation**: show the cohort or matched-case evidence, including post count and counterexamples.
2. **Inference**: explain the topic, headline, visual, format, or distribution logic that likely carried or dragged performance.
3. **Editorial response**: state what to replicate or what bounded test should change.

### Post evidence

Name each example with the source-language first-line caption or most recognizable on-image headline. Make it link directly to the original Facebook post. Show page, date, pillar/territory, format, primary KPI, reactions, comments, shares, and original media.

Use `object-fit: contain` or equivalent letterboxing so original images are fully visible. When media is unavailable or a post is text-only, label the state rather than substituting unrelated imagery.

Place evidence beside the mechanism it supports. High performers lead with **What to replicate** and need no forced rewrite. Low performers lead with the likely issue, then an evidence-based suggested hook and visual improvement labelled as a test. Editorial examples follow the source language, even when the report narrative is English.

For every Suggested Hook or Visual Test, make the evidence trail auditable in nearby prose: reader feedback may identify the content question; comparable performance evidence determines the packaging mechanism; approved sources support the claims. If the performance evidence supports only a content opportunity, do not manufacture a data-backed hook—defer it until the source and packaging basis are available.

### Same-topic cases

Present every reliable case as a compact side-by-side comparison. Include every page's original image, source-language hook, direct link, date, format, selected KPI, and supporting metrics. Explain the shared incident/source briefly, then focus on angle and execution differences. Do not compare materially different incidents or unchanged reposts as creative variants.

### Competitor opportunities

Pair every material opportunity with at least one successful linked execution reference and one lower-performing counterexample when approved media is available. Show original media and metrics, identify the transferable mechanism from the relevant high–middle–low cohort, and provide one source-language adaptation for the focal brand. The opportunity itself must rest on sustained territory volume, performance distribution, and counterexamples—not the single winner or its surface wording.

### Comments

Promote up to three supported newsroom insights from non-PM-CTA posts. Each insight includes the reader signal, editorial meaning, coverage response, and linked example posts. Add a packaging response only when independently supported by comparable performance evidence. Do not present chatbot trigger volume as reader conversation. Keep sampling mechanics and excluded trigger volume in Methodology / Caveats.

## 4. Next-Month Commissioning Plan

Translate established findings into numbered briefs an editor can assign. Each item states:

- Scale, Improve, Stop, or Test;
- what to commission;
- the successful topic/headline/visual/content contract;
- a linked model when it materially clarifies execution;
- how the next monthly review will judge it.

Refer back to evidence already shown rather than introducing a new metric dump after the recommendations. Do not place a separate post-evidence section after the action plan.

## Methodology / Caveats

Place methodology last or in a collapsed section. Name `chief-editor-review` and the four methods. Include only the detail needed to audit:

- dates, timezone, source, and metric meanings;
- collected, confirmed-ad-excluded, and analyzed counts by page;
- missing values, unknown promotion status, unequal post age, and unavailable reach;
- comparable-set and same-topic matching;
- duplicate/repost handling;
- comment sampling and PM-CTA exclusion;
- public engagement and causal limitations.

## Stable presentation

Preserve the approved business unit's broad typography, colors, hierarchy, evidence-card anatomy, responsive behavior, and section order. Reference reports control presentation only; never copy their old findings.

For more than two competitors, use a compact page scorecard followed by responsive or horizontally scrollable pillar/territory matrices. Remove optional charts that do not change a decision. Principal analysis stays at normal body-reading size; captions and metadata may be smaller.

## Bilingual standalone output

Unless the user explicitly requests a single language, deliver one standalone HTML containing a complete English and Traditional Chinese editorial layer. English is the default on every load. Place a fixed, keyboard-accessible `中 / ENG` switch at the top right and update the document language, title, active state, and visible copy when it changes.

Translate the hero, navigation, scope, section headings, editorial analysis, chart and table labels, calls, recommendations, and methodology. Keep original post hooks, quoted wording, links, metrics, and media shared rather than duplicating the evidence layer. Source-language editorial examples remain in that language; familiar newsroom terms such as shares, median, hook, visual, Core pillar, Scale, Improve, Stop, and Test may remain in English when that is clearer.

Use authored bilingual copy embedded in the file; the report must not depend on a browser translation feature, network request, or external translation service at runtime. English and Chinese must communicate the same finding, evidence status, numbers, and action—translation may adapt phrasing for natural reading but must not introduce a new claim.

## QA gate

Before delivery verify:

- exact period, timezone, pages, KPI, and post counts;
- current month is the decision subject and earlier months are context;
- every performance conclusion is an Observation or anchored Inference;
- hypotheses/tests are labelled;
- the whole eligible cohort informed the high/middle/low conclusions;
- identical reposts are not treated as creative comparisons;
- reliable same-topic matches have match receipts, every comparator link, and available original media;
- competitor opportunities have sustained evidence plus a successful execution reference;
- every Suggested Hook and Visual Test identifies comparable packaging evidence; comments are used only for content needs unless an independent performance anchor is present;
- editorial examples preserve source language and introduce no unsupported claim;
- comment findings exclude PM-CTA posts and are limited to supported newsroom insights;
- action cards contain editorial decisions rather than agent instructions or methodology warnings;
- chart encodings, bar lengths, scales, legends, and exact values agree;
- Part 2 contains the Page-level scorecard and Core-pillar comparison modules with the required fields and QA markers;
- the report defaults to English, the top-right `中 / ENG` switch changes the complete editorial layer, and both languages preserve evidence and action parity;
- all images render fully, links work, and no external image dependency remains;
- English and Chinese desktop/mobile views have no clipped text, accidental tiny analysis, or horizontal page overflow;
- unresolved template tokens, credentials, commenter identities, and private collection URLs are absent;
- previous reports remain unchanged.
