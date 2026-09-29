---
name: commit
description: Review uncommitted changes, propose a conventional commit message, and commit the agreed scope when authorized.
argument-hint: "[-y]"
---

# Commit

Inspect changes, agree on scope, and use [references/commit-template.md](references/commit-template.md) for the summary and message. A message-only request does not authorize a commit.

## 1. Inspect

Run `git status --porcelain=v1`, `git diff --staged`, `git diff`, and `git ls-files --others --exclude-standard`. Read relevant untracked source; note generated files, lockfiles, and binaries without dumping them. If there are no changes, report that and stop.

Distinguish this thread's changes, other changes, mixed files, and the pre-existing staged set. Do not infer authorship from filenames or staging alone.

## 2. Choose scope

- **Default:** reuse explicit scope already provided. Otherwise use this thread's changes if they are the only changes; when other work exists, show the groups and ask for this thread, everything, or only pre-staged changes. Ask whether to include or omit mixed files; do not silently split hunks.
- **`-y`:** commit only this thread's files; if this thread changed nothing, commit all changes. Omit mixed files and report them. Make one commit without waiting for further approval.

Show the selected scope and message before committing. In default mode, wait for message approval unless the user has already authorized committing without further review. For unrelated changes, propose separate commits; `-y` keeps the single-commit behavior.

## 3. Commit and report

Stage exactly the agreed paths with `git add -- <paths>`; use `git add -A` only for an agreed all-changes scope. If unrelated files were already staged, unstage them before committing and report it; preserve their working-tree edits.

Use `git commit -F <message-file>` or a quoted heredoc to preserve the message. Honor hooks. If a hook fails, inspect the resulting index/worktree, fix an in-scope cause, and retry normally; stop if the fix requires unrelated work. Never push, amend, or bypass hooks unless requested.

Report the new hash/subject, committed scope, and remaining changes using `git log --oneline -1` and `git status --short`.
