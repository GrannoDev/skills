---
name: commit
description: Review changes, propose a conventional commit message, and commit the agreed scope. Use when asked to commit or write a commit message.
argument-hint: "[-y]"
---

# Commit

Use [the output template](references/commit-template.md). A message-only request does not authorize committing.

1. Inspect `git status --porcelain=v1`, staged/unstaged diffs, and `git ls-files --others --exclude-standard`. Read relevant untracked source; summarize generated/binary files. Stop if clean. Distinguish this thread's work, other work, mixed files, and pre-staged changes; staging is not proof of authorship.
2. Default: reuse explicit scope. If only this thread's work exists, select it. Otherwise show groups and ask which to include; clarify mixed files rather than silently splitting hunks. Show scope/message and wait for message approval unless already authorized to commit without review.
3. `-y`: make one commit of this thread's files, or all changes if this thread changed nothing. Omit/report mixed files. Show scope/message without another approval. In default mode, propose separate commits for unrelated changes.
4. Stage exactly agreed paths using `git add -- <paths>`; use `-A` only for all-changes scope. Unstage unrelated pre-staged files and report it, preserving their edits. Commit with `git commit -F <message-file>` or a quoted heredoc.
5. Honor hooks. After failure, inspect index/worktree and retry only after fixing an in-scope cause; stop if unrelated work is required. Never push, amend, or bypass hooks unless requested.

Report hash/subject, committed scope, and remaining changes from `git log --oneline -1` and `git status --short`.
