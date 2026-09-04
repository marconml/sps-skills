---
name: fix-monster-glyphs
description: "Repair malformed Chinese characters (怪獸字、AI 錯字、變形中文字) in images using exactly three ordered steps: find a verified font library, overlay the correct glyph, then fix its styling to match surrounding text. Use for local character corrections in posters, screenshots, thumbnails, and social graphics, including Hong Kong Traditional Chinese. Not for ordinary proofreading or whole-image redesign."
---

# 怪獸字修復 · Fix Monster Glyphs

**找字庫 → 疊字 → 配風格 · Find → Overlay → Match**

嚴格依次完成三步；不能用模型猜字或整圖重畫取代。依環境工具規則實作，受限時如實說明。

## 1. 找字庫 · Find

找到包含正確字形、且接近原字款的字庫。優先原字體；無法確認時，用候選字體排出鄰近的正常字（例如「胎」「萬」），比較字體類型及筆畫粗幼後再選擇。核對目標字、地區字形、授權及缺字／fallback，說明實際採用的字體；不能只因含有該字便選用。

## 2. 疊字 · Overlay

以使用者最新指定的原圖為底稿，先提取目標字的可見筆畫框，排除描邊及陰影，記錄位置、寬度、高度與基線。將正確字形水平及垂直分別拉伸，對齊量得的字框，再透明疊回局部清除錯字的位置；不能只估字號，或把尺寸匹配留到第三步。同字在不同大小的文字中須逐處量度。保留原檔、其他內容及可調整字層。

## 3. 配風格 · Match

在已對齊的尺寸下，匹配筆畫粗幼、填色、描邊、陰影及質感，保持正確筆畫與內部留白。加粗、模糊或描邊後再次檢查可見尺寸；若仍像另一種字體，返回第一步重選，再依次疊字及配風格。需要量度與實作細節時讀取 [風格匹配筆記](references/style-matching.md)。

在原尺寸及放大圖分別核對字形、尺寸與風格，確認其他內容保留，然後輸出完整新圖供預覽及下載。尺寸一致不代表字款一致；有明顯差距時不可宣稱完全匹配，應改進或清楚交代限制。

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
