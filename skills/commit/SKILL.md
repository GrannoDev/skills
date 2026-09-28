---
name: commit
description: Summarize uncommitted changes as conventional-commit bullets and propose a commit message. Use when the user asks to commit or wants a commit message.
---

# Commit

Summarize the working tree, agree on scope with the user, propose a message, and commit only after they approve.

## 1. Gather the changes

Run these in the repo root:

```bash
git status --porcelain=v1
git diff --staged
git diff
git ls-files --others --exclude-standard
```

Read untracked files that look like source. Skip lockfiles, build output and binaries; note that they changed and move on.

If nothing has changed, say so and stop.

## 2. Ask about scope

Other sessions, editors or the user may have changed files that this thread never touched. Split the changes into two groups:

- **This thread:** files you created, edited or deleted in this conversation.
- **Other:** everything else.

If the "Other" group is empty, say that every change is from this thread and continue. Otherwise list both groups and ask the user which to commit. Use a question tool if you have one.

- **Only this thread** (list the files)
- **Everything** (list the extra files)

If a file has hunks from both groups, point it out. Ask whether to include the whole file or leave it out. Don't try to split hunks without asking.

If the user already staged files before you started, mention it and treat the staged set as a third option: "Only what's staged".

## 3. Summarize the changes

Show a short title and one bullet per logical change, each prefixed with its conventional-commit type:

```
Add CSV export to the reports page

- feat: export the current report as CSV from the toolbar
- fix: date filter dropped the last day of the range
- refactor: move report query building into reports/query.ts
- chore: bump papaparse to 5.4.1
```

Types: `feat`, `fix`, `refactor`, `perf`, `docs`, `test`, `style`, `build`, `ci`, `chore`, `revert`.

- Describe what changed for the user or the codebase. Don't list files.
- Group related edits across files into one bullet.
- Mark breaking changes with `!` after the type (`feat!:`) and say what breaks.

## 4. Propose the commit message

Pick the type of the most significant change (`feat` > `fix` > the rest). Always use this format, whatever earlier commits in the repo look like.

```
feat(reports): add CSV export

Adds an Export button to the reports toolbar that downloads the
current view as CSV.

- fix: date filter now includes the last day of the range
- refactor: report query building lives in reports/query.ts
- chore: bump papaparse to 5.4.1
```

- Subject: `type(scope): summary`. Use the imperative mood, lowercase after the colon, no trailing period, 72 characters or fewer.
- Scope: one lowercase word naming the feature, module or top-level folder the change is about (`auth`, `reports`, `api`). Leave it out if the change spans the whole repo.
- Body: say why the change was made and what it does, wrapped at 72 characters. Add the smaller changes as bullets.
- Footer: `BREAKING CHANGE: ...` when something breaks, and `Refs: <issue>` only when the user names an issue.

If the changes are unrelated, for example a feature plus an unrelated dependency bump, suggest splitting them into separate commits and propose a message for each.

## 5. Commit on approval

Wait for the user to approve or edit the message. Then:

- Stage exactly the agreed files: `git add -- <paths>`. Use `git add -A` only when the user chose "Everything".
- If files outside the agreed scope were already staged, unstage them first with `git restore --staged -- <paths>`, and tell the user you did.
- Commit with a heredoc so the formatting survives:

  ```bash
  git commit -F - <<'EOF'
  <subject>

  <body>
  EOF
  ```

- Show `git log --oneline -1` and `git status --short` so the user can see what was committed and what's left.

Never push, amend, or skip hooks (`--no-verify`) unless the user asks. If a hook fails, show its output, fix the cause if it's in scope, and create a new commit rather than amending.
