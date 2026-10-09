# Installation and shared updates

Canonical source: `marconml/sps-skills`. Colleagues follow `dev`, the owner-designated update branch; maintainers validate changes before pushing there. `main` is outside this distribution workflow. Starting a new review runs the updater once, before reading detailed guidance. The report receipt records the installed commit, making a review reproducible even after a later release.

## First installation

Ask Codex to download `https://raw.githubusercontent.com/marconml/sps-skills/dev/chief-editor-review/scripts/sync_skill.py` to a temporary file, inspect it, and run it with Python 3.9 or newer. It installs the complete skill into `$CODEX_HOME/skills/chief-editor-review`, or `~/.codex/skills/chief-editor-review` when unset. Use the updater for the first installation so its baseline is recorded. An ordinary GitHub skill-folder installation works too: when identical to the shared release, its first check registers that baseline.

Suggested message to colleagues:

> 安裝 https://github.com/marconml/sps-skills/tree/dev/chief-editor-review 。請用該 skill 的 scripts/sync_skill.py 首次安裝，之後每次開始新 review 前檢查 dev 最新版。更新前備份，保留本機修改，並記錄使用版本。

The installed skill becomes available on the next turn. If the client still shows its prior skill list, start a new chat or restart the client. The first-install prompt authorizes shared updates; no separate scheduled job is needed. Checks occur when Codex follows the skill entrypoint, not as an operating-system background service.

## Status and recovery

- `installed`, `updated`, `up_to_date`: use the reported commit. After `updated`, re-read the skill and applicable references.
- `local_changes`: retain the install and show changed paths. Review/copy those edits separately before restoring the tracked baseline; the updater does not merge them automatically.
- `unmanaged`: preserve the existing install. A user may explicitly approve `--adopt` after reviewing replacement; it makes a complete backup first.
- `unavailable`, `deferred`: retain the existing version; record the failed check. If no install exists, installation remains incomplete. A crashed process can leave a lock; remove it only after verifying no sync is running.

State and complete backups live in a sibling `.sps-skill-state/chief-editor-review/` folder, outside the installed skill. The updater ignores Python bytecode caches, hashes every other installed file, downloads an immutable commit archive, validates paths/size, stages all files, and rolls back replacement on failure. It affects only this skill; report exports and output folders are outside its target.

To restore a backup, first preserve the current installed folder, copy the selected backup into the target, and rebuild the matching state from that version before resuming automatic sync. Without matching state, the updater preserves it as a local/unmanaged install. Backups are retained for manual recovery rather than silently deleted.
