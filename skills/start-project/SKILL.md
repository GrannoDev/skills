---
name: start-project
description: Start saved project services in dependency order, verify readiness, and report URLs and logs. Run only when invoked by name.
argument-hint: "[service...]"
disable-model-invocation: true
---

# Start project

Read the marked setup block in root `AGENTS.md`, with `CLAUDE.md` fallback. If absent, suggest `/setup-project` and stop. Follow documented prerequisites, ownership, order, and restrictions.

1. Select all services or only named ones. Accept unambiguous aliases; clarify unknown names. Report missing dependencies without expanding the selection.
2. Stop for missing env/secrets, citing their documented source. Report version mismatches. Request unavailable Docker startup unless already authorized to start it.
3. Keep `.agents/run/` locally ignored. Use lowercase service slugs with `<service>.log`, `.pid`, and `.json`. Identity records contain `pid`, OS `started_at`, `command`, `cwd`, and any process-manager handle; PID alone is insufficient.
4. Check readiness first and reuse ready services. If a port is occupied but readiness fails, inspect the listener and clarify instead of replacing it. Request user/IDE startup unless authorized. Run shared returning commands once; launch long-running commands persistently, recording the actual managed PID and output.
5. Wait using documented checks/timeouts. Defaults are 2 minutes for containers/frontends and 5 for backends. On exit/timeout, show the last 40 log lines, stop starting services, and leave successful ones running.

Never wipe data. Run migrations/seeds only when documented startup includes them. Report corrected commands and offer to update those setup lines.

Report `Service | Status | URL | Logs`, warnings, and `/stop-project`. Statuses are `started`, `already running`, `started by you`, `skipped`, `failed`.
