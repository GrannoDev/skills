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
| [break-ui](skills/break-ui/SKILL.md) | Exercises a UI in a browser, simulator or emulator and reports ranked, reproduced bugs; delegates when available. |
| [ca-release](skills/ca-release/SKILL.md) | Releases a Climbalong app: merges into main/master, bumps and tags the version, pushes, and merges back into develop and pushes it. |
| [commit](skills/commit/SKILL.md) | Reviews changes, proposes a conventional commit message and commits the authorized scope. |
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
| Edge-case ledger and test plan | [What-if report](skills/what-if/references/report-template.md) |
| Reproduced UI bugs | [UI bug report](skills/break-ui/references/report-template.md) |
| Change summary and commit message | [Commit output](skills/commit/references/commit-template.md) |

When revising a skill, check its default mode, each flag and its resume/failure path. Preserve invocation policy and authorization boundaries. A template makes the output shape repeatable; evidence requirements and explicit decision rules make its content more reliable.
