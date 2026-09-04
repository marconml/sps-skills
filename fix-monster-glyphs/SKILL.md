---
name: fix-monster-glyphs
description: "Repair malformed Chinese characters (怪獸字、AI 錯字、變形中文字) in images using exactly three ordered steps: find a verified font library, overlay the correct glyph, then fix its styling to match surrounding text. Use for local character corrections in posters, screenshots, thumbnails, and social graphics, including Hong Kong Traditional Chinese. Not for ordinary proofreading or whole-image redesign."
---

# 怪獸字修復 · Fix Monster Glyphs

**找字庫 → 疊字 → 配風格 · Find → Overlay → Match**

嚴格依次完成三步；不能用模型猜字或整圖重畫取代。依環境工具規則實作，受限時如實說明。

## 1. 找字庫 · Find

找到包含目標字的字庫，實際排出並核對字形。優先原字體，遵循使用者指定的地區字形或產品；檢查授權及缺字／fallback，說明實際採用的字體。找不到時指出所缺資料，不憑空畫字。

## 2. 疊字 · Overlay

以原圖或使用者選定版本為底稿，局部清除錯字，將核對過的字形透明疊回去，對齊位置、大小及基線。保留原檔、其他內容及可調整字層，避免矩形底板和錯字殘影。

## 3. 配風格 · Match

調整疊字的粗幼、比例、字距、填色、描邊、陰影及質感，使它融入旁邊文字；保持正確筆畫與內部留白。需要實作細節時讀取 [風格匹配筆記](references/style-matching.md)。

在原尺寸及放大圖核對字形和風格，確認其他內容保留，然後輸出完整新圖供預覽及下載。只有疊字仍不算完成；有風格差距時繼續調整或明確說明。

使用例：「用 $fix-monster-glyphs，找字庫 → 疊字 → 配風格，修好『嬲』並保留原標題字款。」

## Skill-source maintenance

This section applies only to user-requested edits to this skill's own reusable
files, not ordinary skill use, generated outputs or live SPS prompt changes.
Work in the `marconml/sps-skills` source checkout on `dev` and follow its root
`AGENTS.md`. After each change, validate, commit only task-owned changes and
push to `origin/dev`; verify the remote commit before reporting completion.
An explicit user instruction not to commit or push overrides this default.
Never force-push, publish unrelated commits or push to `main`.

For an installed copy outside the source checkout, locate that checkout first;
do not initialize Git here or use an unrelated project's remote. Report missing
access, validation failures or conflicts instead of claiming publication.
