---
name: start-project
description: Start services from the saved project setup, check readiness, and report URLs and logs. Run only when invoked by name.
argument-hint: "[service...]"
disable-model-invocation: true
---

# Start Project

Use the marked `setup-project` block in root `AGENTS.md`, falling back to `CLAUDE.md` for older setups. If absent, stop and suggest `/setup-project`; do not guess commands. Follow its prerequisites, ownership, service order, and off-limits rules.

## Workflow

1. **Select services.** Start all by default, or only those named. Accept unambiguous aliases (`db` for Postgres); ask about unmatched or ambiguous names. Report missing dependencies of a selected service; do not silently expand the requested list.
2. **Check prerequisites.** Stop on missing env files/secrets and report the documented source. Report tool-version mismatches. If containers need Docker and it is unavailable, request that it be started; start it yourself only when authorized.
3. **Prepare runtime records.** Keep `.agents/run/` locally gitignored. Use lowercase service slugs. Store each managed process's log at `<service>.log`, PID at `<service>.pid`, and identity at `<service>.json` with `pid`, `started_at` (from the OS), `command`, and `cwd`. Record process-manager handles there when applicable. A PID alone may be reused.
4. **Start in setup order.** First run the ready check; reuse a service already ready. If the port is occupied but readiness fails, inspect the listener and stop for clarification rather than replacing it. For a user/IDE-owned service, request startup or use its command if authorized. Run returning commands directly, once per shared command. Launch long-running commands with a supported persistent process manager or detached process, capturing the actual managed PID and logging output.
5. **Wait for readiness.** Use the documented check and timeout; if none is specified, allow about 2 minutes for containers/frontends and 5 for backends. Poll briefly and keep progress visible. On process exit or timeout, show the last 40 log lines, stop starting further services, and leave successful services running.

Starting never wipes data. Run migrations or seeds only if the documented startup procedure includes them. If a setup command is wrong and a correction works, report it and offer to update only those lines.

## Output

```markdown
| Service | Status | URL | Logs |
| --- | --- | --- | --- |
| <name> | <status> | <URL> | <log path or command> |

Warnings: <failed checks, version mismatches, missing dependencies, or None.>
Stop with /stop-project.
```

Statuses: `started`, `already running`, `started by you`, `skipped`, `failed`. Report partial startup accurately.
