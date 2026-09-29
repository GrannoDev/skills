---
name: stop-project
description: Stop every service the project depends on, in reverse start order, using the setup that /setup-project saved to AGENTS.md. Keeps all data. Run only when the user invokes it by name.
argument-hint: "[service...] [-y]"
disable-model-invocation: true
---

# Stop Project

Stop the services from the setup in reverse start order: the frontend first, the database last. Stop processes that `/start-project` started, ones the user started, and the containers. Keep all data. Stopping is not resetting.

## Auto-approve with `-y`

If the user passes `-y` (`/stop-project -y`), stop processes that were started outside `/start-project` without asking. Everything else in this skill still applies.

## 1. Read the setup

Read the `setup-project` section of `AGENTS.md` at the repo root (between `<!-- setup-project:start -->` and `<!-- setup-project:end -->`). If it isn't there, check `CLAUDE.md`, where earlier runs put it.

If neither has it, tell the user to run `/setup-project` first and stop.

From **Running the app**, take the services in order with their URL (for the port) and stop command, and the **Never** list. Follow it for the whole run.

Also list `.agents/run/*.pid` at the repo root. These are the processes `/start-project` started.

## 2. Pick the services

If the user named services (`/stop-project frontend`), stop only those. Match names loosely against the Service column. If a name matches nothing, list the services and ask.

Otherwise stop them all, in reverse start order.

## 3. Stop each service

For each service, first check whether it's running: its container is up (`docker compose ps <service>`), or something listens on its port (`lsof -nP -iTCP:<port> -sTCP:LISTEN`). If not, mark it "not running" and move on.

**Containers and other services with a stop command** (`docker compose stop postgres`): run the command from the setup. If several rows share one command, run it once.

If the stop command would delete data (`docker compose down -v`, `docker volume rm`, dropping a database), don't run it. Stop without removing data (`docker compose stop <service>`) and tell the user what the setup says.

**Processes stopped with Ctrl+C** (a backend or frontend dev server):

1. **Started by `/start-project`:** if `.agents/run/<service>.pid` holds a live PID, stop it and its children. Build tools and `npm` start the real server as a child, so killing only the PID often leaves it running:

   ```bash
   kill_tree() { for c in $(pgrep -P "$1"); do kill_tree "$c"; done; kill -TERM "$1" 2>/dev/null; }
   kill_tree "$(cat .agents/run/backend.pid)"
   ```

   Then delete the PID file. Keep the log; the next start overwrites it.
2. **Started some other way** (from the IDE or a terminal, or a stale PID file): find what listens on the port and check its working directory (`lsof -a -p <pid> -d cwd -Fn`). If it's inside this repo, ask the user before stopping it, since it may be an IDE debug session. Skip the question with `-y`. If it's outside the repo, it isn't this project's: leave it and say so.

**Wait until it's stopped.** Give each service up to 20 seconds to free its port or stop its container. If a process is still running after that, send `kill -KILL` to the same processes and say you had to.

## 4. Check nothing is left

Once every service is handled:

- Every service's port is free, or its container is stopped.
- No PID from `.agents/run/` is still alive. Delete PID files whose process is gone.

Never stop containers or processes that aren't in the setup, even if they look related.

## 5. Report

```
## Project stopped

| Service | Status |
|---------|--------|
| Frontend | stopped |
| Backend | stopped (started from the IDE, you confirmed) |
| Keycloak | stopped |
| Postgres | not running |

Data is kept. Start again with /start-project.
```

Use "stopped", "stopped (forced)", "not running", "left running" (the user declined, or it isn't this project's) or "failed". Under the table, add one line for each service left running or failed, with the reason and the command the user can run to stop it themselves.
