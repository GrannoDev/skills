---
name: blueprint-clean
description: Delete completed .blueprints/ plans and report unfinished plans with status and progress. Run only when invoked by name.
argument-hint: "[-y]"
disable-model-invocation: true
---

# Blueprint clean

List `.blueprints/*/PLAN.md` and legacy `.blueprints/*.md`. Stop if none exist. Read title, slug, status, modification date, checked/total Implementation steps, and unresolved Open questions. `None.` means zero questions.

Only `status: done` permits deletion. Show the exact plans and any other files in their directories. Confirm unless `-y` or prior authorization covers deletion; preserve files the user wants as documentation. Delete only authorized directories or legacy files. Gitignored plans may be unrecoverable.

Report deleted slugs, then:

| Blueprint | Status | Progress | Open questions | Last changed | Next |
| --- | --- | --- | --- | --- | --- |
| <slug> | <status> | <checked>/<total> | <count> | <date> | <command> |

Next is `/blueprint <slug>` for drafts and `/blueprint-build <slug>` for approved/building plans; unknown statuses need manual review. Flag unreadable/unknown files, unfinished plans with all steps checked, and draft/building plans unchanged for 30+ days. Never delete these based on age or apparent completion.
