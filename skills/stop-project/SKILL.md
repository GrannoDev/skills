---
name: stop-project
description: Stop project services from the saved setup in reverse order, preserving data. Run only when invoked by name.
argument-hint: "[service...] [-y]"
disable-model-invocation: true
---

# Stop Project

Read the marked `setup-project` block in root `AGENTS.md` (legacy fallback: `CLAUDE.md`) and `.agents/run/` records. If the setup is absent, stop and suggest `/setup-project`. Follow its off-limits rules. Never remove volumes, reset data, or stop services outside this project's setup.

## Scope and authorization

Stop all listed services by default, or only the named ones, in reverse startup order. Accept unambiguous aliases; ask about unmatched or ambiguous names. Managed processes and project-scoped container stop commands are covered by this invocation. Confirm before stopping a service started externally (for example an IDE debug session), unless `-y` or an earlier instruction already authorizes it.

## Workflow

1. Check each service's container state or port. If not running, report it and remove only runtime records whose process is gone.
2. For containers or services with explicit stop commands, verify the command targets this project and preserves data. Replace a documented destructive stop with its data-preserving equivalent; if none is known, leave it running and explain.
3. For Ctrl+C services, compare `<service>.pid` and `<service>.json` with the live command, working directory, and OS start identity. Treat missing/stale/unverifiable records (including older PID-only records) as externally started. Locate its listener and check ownership; leave processes outside this repo alone regardless of `-y`. Use a recorded process-manager handle when applicable.
4. Send TERM to the verified process and its verified descendants. Wait up to 20 seconds. If still running, recheck identity before sending KILL to those same project processes; report forced stops.
5. Verify the selected containers stopped or ports were freed. Delete PID/identity records only once the process is gone; keep logs. Report unselected services as outside this run's scope.

## Output

```markdown
| Service | Status | Detail |
| --- | --- | --- |
| <name> | <status> | <reason if forced, left running, or failed> |

Data is kept. Start with /start-project.
```

Statuses: `stopped`, `stopped (forced)`, `not running`, `left running`, `failed`. Include a project-scoped manual stop command for failures when known.
