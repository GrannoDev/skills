---
name: blueprint-clean
description: Delete completed .blueprints/ plans and report remaining plans with status and progress. Run only when invoked by name.
argument-hint: "[-y]"
disable-model-invocation: true
---

# Blueprint Clean

Remove only blueprints with `status: done`. These files are usually gitignored; deletion may be unrecoverable. Default to confirming the exact list; `-y` authorizes deletion without another question.

## Workflow

1. List `.blueprints/*/PLAN.md` and legacy `.blueprints/*.md`. If none exist, report that and stop.
2. Read each file's title, slug, frontmatter status, modification date, checked/total steps under Implementation steps, and unresolved Open questions (`None.` means zero).
3. Separate `done`, unfinished (`draft`, `approved`, `building`), and unreadable/unknown-status files. Never delete the last two groups.
4. Show the done plans, naming any other files in their `.blueprints/<slug>/` directories, and ask for confirmation unless `-y` or an earlier instruction already authorizes their deletion. Keep any files the user wants as documentation. Delete exactly the authorized list: the `<slug>/` directory, or the legacy file.

## Output

```markdown
Deleted <n>: <slugs, or None.>

| Blueprint | Status | Progress | Open questions | Last changed | Next |
| --- | --- | --- | --- | --- | --- |
| <slug> | <status> | <checked>/<total> | <count> | <YYYY-MM-DD> | <command> |
```

Next: `/blueprint <slug>` for drafts; `/blueprint-build <slug>` for approved/building plans. Under the table, flag unreadable files, unfinished plans with every step checked, and draft/building plans unchanged for over 30 days. Do not delete a plan merely because it is stale or looks finished.
