# skills

Agent skills by [GrannoDev](https://github.com/GrannoDev).

## Install

```bash
npx skills add GrannoDev/skills
```

Install a single skill:

```bash
npx skills add GrannoDev/skills --skill <name>
```

## Skills

| Skill | Description |
| --- | --- |
| [blueprint](skills/blueprint/SKILL.md) | Plans a feature section by section into a blueprint: domain models, APIs, data flow, logic to test and steps. |
| [blueprint-build](skills/blueprint-build/SKILL.md) | Builds an approved blueprint tests-first and records how it works, verification and deviations. |
| [blueprint-clean](skills/blueprint-clean/SKILL.md) | Deletes finished blueprints and lists the ones still in progress. |
| [break-ui](skills/break-ui/SKILL.md) | Exercises a UI in a browser, simulator or emulator and reports ranked, reproduced bugs; delegates when available. |
| [ca-release](skills/ca-release/SKILL.md) | Releases a Climbalong app: merges into main/master, bumps and tags the version, pushes, and merges back into develop and pushes it. |
| [commit](skills/commit/SKILL.md) | Reviews changes, proposes a conventional commit message and commits the authorized scope. |
| [setup-project](skills/setup-project/SKILL.md) | Drafts how to run the app, verify changes (auth and test accounts) and which tests to write, has you confirm or change each section, then saves it to AGENTS.md. |
| [start-project](skills/start-project/SKILL.md) | Starts the project's services in order from the `/setup-project` setup, waits until each is ready, and reports URLs and logs. |
| [stop-project](skills/stop-project/SKILL.md) | Stops selected project services in reverse order, verifies process ownership and keeps data. |
| [use-tdd](skills/use-tdd/SKILL.md) | Fixes a bug test-first: a focused regression test that fails before the fix and passes after. |
| [what-if](skills/what-if/SKILL.md) | Walks through a feature's edge cases one question at a time and ends with a test plan. |

## Adding a skill

Each skill is a folder under `skills/` with a `SKILL.md`:

```
skills/<name>/
  SKILL.md        # frontmatter (name, description) + instructions
  references/     # optional: extra docs loaded on demand
  scripts/        # optional: helper scripts
```

`name` must match the folder name. `description` says what the skill does and when to use it; agents read it to decide when to load the skill.

Keep the workflow in `SKILL.md` and define recurring deliverables in a linked template. Keep short output formats inline. Templates specify required fields, evidence and empty-section behavior; examples should not supply unrelated business rules.

## Output templates

| Deliverable | Template |
| --- | --- |
| Feature plan | [Blueprint](skills/blueprint/references/blueprint-template.md) |
| Implementation report | [Build summary](skills/blueprint-build/references/summary-template.md) |
| Project instructions | [Project setup](skills/setup-project/references/setup-template.md) |
| Edge-case ledger and test plan | [What-if report](skills/what-if/references/report-template.md) |
| Reproduced UI bugs | [UI bug report](skills/break-ui/references/report-template.md) |
| Change summary and commit message | [Commit output](skills/commit/references/commit-template.md) |

When revising a skill, check its default mode, each flag and its resume/failure path. Preserve invocation policy and authorization boundaries. A template makes the output shape repeatable; evidence requirements and explicit decision rules make its content more reliable.
