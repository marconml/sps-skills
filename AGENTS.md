# SPS Skills contributor instructions

## Scope

These rules govern user-requested changes to reusable skill source in this
repository: instructions, references, scripts, assets, metadata and supporting
documentation. Reading, installing or running a skill, generating an output, or
editing live SPS prompts does **not** authorize source edits or Git publication.
An explicit user instruction such as read-only, no commit or no push takes
precedence over this default maintenance workflow.

## Repository and branch

- Canonical repository: `marconml/sps-skills`.
- SSH remote: `git@github.com:marconml/sps-skills.git`.
- Use `dev` for skill changes and publish them to `origin/dev`.
- Keep `main` as the stable release branch. Do not push to or merge into `main`,
  change repository permissions, or force-push as part of this workflow.
- If editing an installed skill outside this repository, locate the source
  checkout first and read this file there. Do not initialize Git inside an
  installed skill directory or push from an unrelated project. If the checkout
  or write access is missing, report what is needed.

## Maintenance workflow

1. Inspect the remote, current branch, working tree, index and local commits.
   Fetch `origin` before editing. Switch to `dev` safely and fast-forward to
   `origin/dev` where possible. If only the remote branch exists, create a local
   tracking branch. If neither exists, ask which base to use unless the user
   already specified it.
2. Preserve unrelated staged/unstaged files and local commits. Never reset,
   discard or silently stash someone else's work. Use a separate checkout when
   concurrent work prevents safe isolation; stop and explain unresolved conflicts.
3. Make only the requested source changes. Preserve the skills' operational
   behavior unless the user also requested a behavior change.
4. Validate each changed skill with the available skill-creator validator, check
   referenced files and review the instructions for contradictions. Run any
   relevant existing tests and `git diff --check`. If required validation fails
   or cannot run, report the blocker instead of publishing unverified changes.
5. Inspect the final diff for unrelated edits, credentials and generated user
   data. Stage only the task-owned paths or hunks; never sweep up unrelated
   changes with a blanket add. Review the entire staged diff before committing.
   Do not run an ordinary commit while unrelated changes remain in the index;
   isolate the work or use a scoped commit method that preserves their staged
   state. If safe isolation is not possible, stop and report the conflict.
6. Commit the validated changes with a concise Conventional Commit message.
   Before pushing, fetch again and inspect every commit ahead of `origin/dev`;
   do not publish unrelated pre-existing local commits. If the remote advanced,
   integrate safely without rewriting published history, revalidate and stop on
   conflicts. Never force-push.
7. Push with `git push -u origin dev`. Verify that the remote `dev` contains the
   new commit before reporting completion. A rejected push or missing credentials
   is an incomplete publication: report the local commit and exact blocker.
8. Report the changed files, validation result, commit ID and verified remote
   branch. Do not create empty commits when no source change was needed.

Apply this workflow after every user-authorized skill-source change unless the
user explicitly opts out. Commit/push does not authorize an SPS write, Facebook
publication, automatic release to `main`, or replacement of installed copies.

## New skills

Include a short, conditional source-maintenance section in each new `SKILL.md`,
consistent with the existing skills, so the rule remains discoverable when a
single skill folder is installed without this repository's root files.
