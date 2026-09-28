---
name: blueprint-clean
description: Delete the blueprints in .blueprints/ that are done and list the ones that aren't, with their status and progress. Run only when the user invokes it by name.
argument-hint: "[-y]"
disable-model-invocation: true
---

# Blueprint Clean

Remove the blueprints that have been built, and show what's still in progress. Blueprints are gitignored, so a deleted blueprint can't be recovered. Confirm before deleting.

## Auto-approve with `-y`

If the user passes `-y` (`/blueprint-clean -y`, or "blueprint-clean -y"), delete the done blueprints without asking. Everything else in this skill still applies.

## 1. Read the blueprints

List `.blueprints/*.md` in the repo root. If the folder is missing or empty, say there are no blueprints and stop.

For each file, read:

- **Status:** `status` in the frontmatter.
- **Progress:** checked and total checkboxes under `## Implementation steps`.
- **Open questions:** the number of items under `## Open questions`, if it says anything other than "None."
- **Last changed:** the file's modification time.

## 2. Sort them

- **Done:** `status: done`. These get deleted.
- **Not done:** `draft`, `approved` or `building`.
- **Unreadable:** no frontmatter, or an unknown status. Never delete these; list them for the user to check.

## 3. Delete the done ones

List the done blueprints by title and slug, then ask the user to confirm (skip this with `-y`). Use a question tool if you have one. On confirmation, delete exactly those files.

If a blueprint's summary is worth keeping as documentation, the user can say so and you leave that file out.

## 4. Report

```
## Blueprints

Deleted <n>: team-invitations, csv-export

Not done:
| Blueprint | Status | Progress | Open questions | Last changed | Next |
|-----------|--------|----------|----------------|--------------|------|
| audit-log | building | 3/7 | 0 | 2 days ago | /blueprint-build audit-log |
| sso-login | draft | 0/5 | 2 | 3 weeks ago | /blueprint sso-login |
| billing-v2 | approved | 0/9 | 0 | today | /blueprint-build billing-v2 |
```

Put the next command to run in the Next column:

- **`draft`:** `/blueprint <slug>` to finish planning.
- **`approved` or `building`:** `/blueprint-build <slug>`.

Flag these under the table, one line each:

- **Looks finished:** every step is checked but the status isn't `done`. Suggest `/blueprint-build <slug>` to verify and write the summary.
- **Stale:** a `draft` or `building` blueprint that hasn't changed in over 30 days. Ask whether it's still wanted, but don't delete it.
- **Unreadable:** files from step 2 that couldn't be parsed.
