# 怪獸字修復 · Fix Monster Glyphs

這是一套可分享的 Codex 技能，嚴格按以下三步修復圖片中的怪獸字：

1. **找字庫**：取得及核對正確字形。
2. **疊字**：將真實字形疊回原圖。
3. **修正風格**：匹配原字款，完成驗證與交付。

## 安裝與使用

1. 請 Codex 從這個儲存庫安裝：

   ```text
   Use $skill-installer to install the skill from:
   https://github.com/marconml/sps-skills/tree/main/fix-monster-glyphs
   ```

   手動安裝亦可：將 `fix-monster-glyphs` 資料夾放到 `~/.codex/skills/`；設定了 `CODEX_HOME` 時使用其下的 `skills/`。
2. 在可載入該技能的 Codex 工作階段附上原圖，輸入：

   `用 $fix-monster-glyphs 按找字庫 → 疊字 → 修正風格，修正圖中的「嬲」並保留原標題字款。`

直接學習方法：閱讀 [SKILL.md](SKILL.md)，再看 [風格匹配實作筆記](references/style-matching.md)。

這是工作流程技能，並非一鍵修圖程式；依所在環境使用可用的圖像編輯或字體排版工具。包內不含私人原圖、付費服務金鑰或第三方字體。
