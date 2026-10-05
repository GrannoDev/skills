---
name: stop-project
description: Stop saved project services in reverse order after verifying process ownership, preserving data. Run only when invoked by name.
argument-hint: "[service...] [-y]"
disable-model-invocation: true
---

# Stop project

Read the marked setup block in root `AGENTS.md`, with `CLAUDE.md` fallback, and `.agents/run/` records. If setup is absent, suggest `/setup-project` and stop. Never remove volumes, reset data, or stop unrelated services.

1. Select all listed services or only named ones, accepting unambiguous aliases. Clarify unknown names. Stop in reverse startup order.
2. Managed processes and project-scoped container stops are authorized by invocation. Confirm externally started services unless `-y` or prior authorization covers them.
3. Check state. For explicit stop commands, verify project scope and data preservation. Replace destructive commands with known data-preserving equivalents; otherwise leave running.
4. Before signaling, match recorded PID, command, cwd, and OS start identity. Use manager handles when present. Missing/stale/PID-only records mean externally started; inspect listener ownership. Processes outside this repo remain untouched, even with `-y`.
5. Send TERM to verified processes and verified descendants; wait up to 20 seconds. Recheck identity before KILL and report forced stops.
6. Verify containers stopped or ports freed. Remove PID/identity records only when the process is gone; retain logs. Report unselected services separately.

Report `Service | Status | Detail`, preserved data, and `/start-project`. Statuses are `stopped`, `stopped (forced)`, `not running`, `left running`, `failed`. Include a known project-scoped manual command for failures.
