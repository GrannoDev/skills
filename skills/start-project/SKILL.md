---
name: start-project
description: Start the project's services in order from the setup that /setup-project saved to AGENTS.md, wait until each one is ready, and report the URLs and log files. Run only when the user invokes it by name.
argument-hint: "[service...]"
disable-model-invocation: true
---

# Start Project

Start every service the project needs, in the order the setup lists them, and wait until each one is ready before starting the next. Skip what's already running. End with the URLs and where the logs are, so the user (or `/stop-project`) can find everything later.

## 1. Read the setup

Read the `setup-project` section of `AGENTS.md` at the repo root (between `<!-- setup-project:start -->` and `<!-- setup-project:end -->`). If it isn't there, check `CLAUDE.md`, where earlier runs put it.

If neither has it, tell the user to run `/setup-project` first and stop. Don't guess how to start the project from the repo.

From **Running the app**, take:

- **Services:** the table rows in order, with the start command and directory, ready check, URL and stop command.
- **Who starts it:** which services the agent starts and which the user runs from the IDE.
- **Prerequisites:** tool versions, env files and secrets.
- **Never:** off-limits actions. Follow them for the whole run.

## 2. Pick the services

If the user named services (`/start-project backend frontend`), start only those. Match names loosely against the Service column (`db` matches Postgres). If a name matches nothing, list the services and ask.

Otherwise start them all. When a named service comes after others in the start order that aren't running, say so in the report, since it may depend on them.

## 3. Check prerequisites

Before starting anything:

- **Env files and secrets:** the files the setup lists exist. If one is missing, say which and where the setup says to get it, and stop.
- **Tools:** the listed versions are what's on the path (`java -version`, `node -v`). Warn on a mismatch; don't stop.
- **Docker:** if any service is a container, `docker info` succeeds. If Docker isn't running, ask the user to start it, or offer to start it (`open -a Docker` on macOS) and wait for it.

## 4. Start each service

Set up the run folder once. It holds the PID and log of each process you start, and stays out of git:

```bash
root=$(git rev-parse --show-toplevel)
mkdir -p "$root/.agents/run"
git check-ignore -q "$root/.agents/run/" || echo ".agents/run/" >> "$(git rev-parse --git-common-dir)/info/exclude"
```

Then go through the services in order. For each one:

1. **Already running?** Run its ready check. If it passes, mark it "already running" and move on. If the port is taken but the ready check fails, something else is using it: show what (`lsof -nP -iTCP:<port> -sTCP:LISTEN`) and ask the user before going further.
2. **User starts it?** If the setup says the user runs this one from the IDE, ask them to start it and wait until the ready check passes. Offer to start it with the setup's command instead.
3. **Start it** with the command from the setup, in its directory:
   - **Commands that return** (`docker compose up -d postgres`): run them as they are. If several rows share one command, run it once.
   - **Long-running processes** (`./mvnw spring-boot:run`, `npm start`): start them detached so they outlive this session, log to `.agents/run/<service>.log`, and save the PID to `.agents/run/<service>.pid`. Use a short lowercase name for `<service>` (`backend`, `frontend`):

     ```bash
     cd "$root/backend" && SPRING_PROFILES_ACTIVE=local nohup ./mvnw spring-boot:run > "$root/.agents/run/backend.log" 2>&1 &
     echo $! > "$root/.agents/run/backend.pid"
     ```

4. **Wait until it's ready.** Poll the ready check every few seconds: a port check (`nc -z localhost 5432`), an HTTP check (`curl -sf http://localhost:8080/actuator/health`), or a log line (`grep -q "Compiled successfully" "$root/.agents/run/frontend.log"`). Give containers and frontends about 2 minutes and backends about 5. If your harness has a wait or monitor tool, use it instead of a sleep loop.
5. **If it fails** (the process exits, or the ready check times out): show the last 40 lines of its log (`docker compose logs --tail 40 <service>` for a container), say what went wrong if you can tell, and stop. Don't start the services after it, and leave the ones already started running.

Don't run migrations, seed or reset data unless the setup says starting does that. Starting never wipes data.

## 5. Fix the setup if it was wrong

If a command, directory, port or ready check in the setup turned out to be wrong and you found what works, tell the user and offer to update the `setup-project` section in `AGENTS.md`. Change only the lines that were wrong.

## 6. Report

```
## Project started

| Service | Status | URL | Logs |
|---------|--------|-----|------|
| Postgres | started | localhost:5432 | `docker compose logs postgres` |
| Keycloak | already running | http://localhost:8180 | `docker compose logs keycloak` |
| Backend | started (42s) | http://localhost:8080 | `.agents/run/backend.log` |
| Frontend | started (18s) | http://localhost:4200 | `.agents/run/frontend.log` |

Stop everything with /stop-project.
```

Use "started", "already running", "started by you", "skipped" (not named) or "failed". Under the table, add one line for each warning: a failed service and why, a tool version mismatch, or a named service whose dependencies aren't running.
