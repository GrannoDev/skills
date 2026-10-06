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
| [bug-hunter](skills/bug-hunter/SKILL.md) | Reproduces feature bugs across UI, APIs and stored state using controlled test data, then verifies requested fixes with evidence. |
| [ca-release](skills/ca-release/SKILL.md) | Releases a Climbalong app: merges into main/master, bumps and tags the version, pushes, and merges back into develop and pushes it. |
| [commit](skills/commit/SKILL.md) | Reviews changes, proposes a conventional commit message and commits the authorized scope. |
| [evidence-based-verification](skills/evidence-based-verification/SKILL.md) | Verifies behavior with focused checks, saves only videos or images, and summarizes results in chat. |
| [setup-project](skills/setup-project/SKILL.md) | Confirms startup, verification, test commands, and auth setup, then saves them in AGENTS.md. |
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

Keep instructions short and specific: exact inputs, actions, outputs, and failure/resume rules. Define recurring deliverables in a compact linked template; keep short output formats inline. Remove duplicated guidance and generic advice.

## Output templates

| Deliverable | Template |
| --- | --- |
| Feature plan | [Blueprint](skills/blueprint/references/blueprint-template.md) |
| Implementation report | [Build summary](skills/blueprint-build/references/summary-template.md) |
| Project instructions | [Project setup](skills/setup-project/references/setup-template.md) |
| Edge-case ledger and test plan | [What-if report](skills/what-if/references/report-template.md) |
| Reproduced UI bugs | [UI bug report](skills/break-ui/references/report-template.md) |
| Cross-layer bug hunt | [Bug hunt report](skills/bug-hunter/references/report-template.md) |
| Before-and-after verification | [Chat summary](skills/evidence-based-verification/references/report-template.md) |
| Change summary and commit message | [Commit output](skills/commit/references/commit-template.md) |

When revising a skill, check its default mode, each flag and its resume/failure path. Preserve invocation policy and authorization boundaries. A template makes the output shape repeatable; evidence requirements and explicit decision rules make its content more reliable.
