---
name: blueprint
description: Plan one feature with the user and save a self-contained blueprint for /blueprint-build. Run only when invoked by name.
argument-hint: "[-q] [feature]"
disable-model-invocation: true
---

# Blueprint

Write `.blueprints/<slug>.md` using [references/blueprint-template.md](references/blueprint-template.md). Plan only; do not implement the feature.

## Modes

- **Default:** confirm the scope, Context, and each design section before moving on. Save confirmed sections immediately.
- **`-q`:** draft all sections without intermediate confirmations. Mark unsupported choices *(assumed)* and put unresolved business or product decisions in Open questions. Critique the draft, then ask once for approval.

Show the draft being reviewed with each confirmation. Ask only for information the request and repo do not answer.

## Workflow

1. **Select the feature.** Infer it from the request or ask. Choose a kebab-case slug. Resume an existing draft from its first unconfirmed section; ask before replacing a blueprint with another status. Record confirmed sections under `confirmed_sections` so another session can resume.
2. **Prepare storage.** Keep `.blueprints/` locally gitignored. Check with `git check-ignore`; if needed, append `.blueprints/` to the common git directory's `info/exclude` and report it. In a non-git directory, skip the exclusion and say so.
3. **Pin the scope.** Write the goal, non-goals, and constraints. For a new file, set `status: draft`, today's date, and `base_branch` to the repo's default branch (or note that it could not be determined). Preserve existing metadata when resuming.
4. **Explore.** Inspect nearby models and migrations, API conventions, tests and fixtures, and integration/UI touch points. Record relevant file paths and conventions in Context. Explore yourself or use read-only subagents when available.
5. **Design in order.** Draft Domain models, APIs, Data flow, Logic to test, and Implementation steps. Follow the template's content requirements. Record decisions with reasons and alternatives. If a later section changes an earlier one, update it and reconfirm the changed contract.
6. **Critique.** Check for unenforced invariants, missing error paths or tests, undefined references, vague requirements, and steps that leave the build broken. A fresh read-only agent may do this when available. Correct omissions; ask about fixes that require a new product decision.
7. **Approve.** Show counts of models, APIs, test cases, and steps, plus assumptions and open questions. Unresolved questions keep the status `draft`. Otherwise ask for approval; only an explicit approval sets `status: approved`.

End with the file path and `/blueprint-build <slug>`. Do not start building automatically.
