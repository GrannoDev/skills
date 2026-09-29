---
name: setup-project
description: Draft a project's setup from the repo (how to run the app, how to verify changes including auth and test accounts, and which tests to write and run), have the user confirm or change each section, then save it to AGENTS.md for every future agent session. Run only when the user invokes it by name.
argument-hint: "[-q]"
disable-model-invocation: true
---

# Setup Project

Find out how to run this project, how to check that a change works, and which tests the user wants. Save the answers to the project's `AGENTS.md` so later sessions, and skills like `/start-project`, `/stop-project`, `/break-ui`, `/use-tdd` and `/blueprint-build`, can start the app, log in and run the right tests without asking again.

Keep it fast: detect everything you can, fill in the gaps with sensible defaults, then walk the user through three sections (running the app, verifying changes, tests). For each one they either confirm your draft and you move on, or pick "Change" and you question them about just that section.

## Asking questions

**Show before you ask.** Never ask the user to confirm or change something they can't see. Before every question, write the section you're asking about in your message as a markdown snippet, then ask in a separate step. The same goes for follow-up questions after "Change": show the current draft of the parts you're asking about first. A question like "Confirm the running-the-app setup?" with no snippet above it is a bug.

If you have a question tool (such as `AskUserQuestion`), use it for every question in this skill instead of asking in plain text:

- For each section's confirmation, ask one question with two options: "Confirm (Recommended)" and "Change". Name the section in the question ("Running the app: confirm or change?"). If the tool supports option previews (the `preview` field in `AskUserQuestion`), also put the section's snippet in the "Confirm" option's preview.
- When the user picks "Change", group the follow-up questions into one call, up to the tool's limit (4 for `AskUserQuestion`).
- Offer what you detected as the options and put the likeliest first, marked "(Recommended)". The user can always pick "Other" and type an answer.
- Use multi-select when several answers can be true, such as which parts of a section to change or which services to run.
- Put the file or command an option came from in its description (`from docker-compose.yml`).
- Ask for values you can't offer as options, such as passwords, in plain text.

If you don't have a question tool, ask in plain text: "Confirm or change?" for each section, and a few numbered questions at a time when the user wants a change.

## Quick mode with `-q`

If the user passes `-q` (`/setup-project -q`), skip the per-section confirmations. Show the whole draft once as a markdown snippet and then ask the user to confirm or change it. Still ask for test credentials if the app has auth and the repo has none. You can't guess them.

Everything else in this skill still applies.

## 1. Detect

Read what's there before asking anything:

- **Existing setup:** `AGENTS.md`, `CLAUDE.md` and any earlier `setup-project` section (between `<!-- setup-project:start -->` and `<!-- setup-project:end -->`). If one exists, use it as the starting draft.
- **Services:** `docker-compose*.yml`, `compose*.yml`, Dockerfiles, `Makefile`, `justfile`, scripts in `package.json`, and the README.
- **Backend:** `pom.xml` or `build.gradle*`, `mvnw`/`gradlew`, `application*.yml`/`.properties` (profiles, ports, datasource, issuer URI), migrations (Flyway, Liquibase) and seed data.
- **Frontend:** `package.json`, `angular.json` or other framework config, proxy config, environment files, the Node version (`.nvmrc`, `engines`).
- **Auth:** Keycloak realm exports, OIDC/OAuth config, security config classes, login routes, seeded users.
- **Tests:** test folders and frameworks (JUnit, Mockito, Testcontainers, Jasmine/Karma, Jest, Vitest, Playwright, Cypress) and coverage config.
- **Env and prerequisites:** `.env.example`, required env vars, tool versions (`.sdkmanrc`, `.tool-versions`, `.java-version`).

## 2. Draft

Fill in every item in the three sections below, using [references/setup-template.md](references/setup-template.md) as the format. Where the repo doesn't answer something, pick a sensible default and mark it *(assumed)*:

- The agent starts the services itself, in dependency order.
- A change is done when it builds and the existing test suites pass.
- UI changes are checked in the harness's built-in browser, or the iOS Simulator or Android emulator for a mobile app.
- The agent writes new tests of the kinds the project already has, following the existing tests' style.
- Nothing is off-limits beyond production and shared environments.

Don't ask anything yet.

## 3. Confirm each section

Go through the sections in order. For each one:

1. Show the draft of that section in your message as a markdown snippet: a `###` heading with the section name, then its parts as a short list or table, with *(assumed)* items visible. Keep it short enough to read at a glance. Example:

   ```markdown
   ### Running the app

   | Service | Start | Ready when | URL |
   | --- | --- | --- | --- |
   | Postgres | `docker compose up -d postgres` | port 5432 open | localhost:5432 |
   | Backend | `./mvnw spring-boot:run` (`backend/`) | `/actuator/health` is UP | localhost:8080 |

   - **Who starts it:** the agent *(assumed)*
   - **Data:** Flyway runs on startup; reset with `docker compose down -v`
   - **Off-limits:** production and shared environments *(assumed)*
   ```

2. Only after the snippet is shown, ask: confirm or change?
3. **Confirm:** move on to the next section.
4. **Change:** ask which parts to change (multi-select from the section's parts below), then question the user about only those parts. Show the updated section and ask confirm or change again.

### Running the app

The services to run, in start order. For a typical stack: Keycloak container, Postgres container, Spring Boot backend, Angular frontend. Parts:

- **Services:** for each, the start command and directory (`SPRING_PROFILES_ACTIVE=local ./mvnw spring-boot:run` in `backend/`), a ready check (port, `/actuator/health`, or a log line), the URL, and how to stop it and wipe its data.
- **Who starts it:** the agent, or the user from the IDE. If the user does, how the agent checks it's running.
- **Prerequisites:** tool versions, env vars or `.env` files, secrets and where they come from.
- **Data:** how migrations run, how to seed test data, and how to reset to a clean state.
- **Off-limits:** anything the agent must never do, such as connecting to a shared database or resetting data without asking.

### Verifying changes

Parts:

- **Done checks:** the exact build, lint, format, type check and test commands that must pass.
- **UI verification:** how the agent checks a UI change by using the app. The default is whatever the harness comes with: its built-in browser for a web app, or the iOS Simulator or Android emulator for a mobile app. Other options: the user's own browser through an extension (it has their real logins, so be careful), browser automation such as a Playwright MCP server or Playwright scripts, only the end-to-end tests, or the user checks it by hand. Also pin down when to do it (after every UI change, or only when asked) and the fallback if the preferred tool isn't available in a session.
- **Auth type:** none, email and password on the app's own form, a Keycloak or other OIDC login page, SSO through Google or Microsoft, a magic link or email code, MFA or one-time codes, API keys, or basic auth.
- **Roles:** which roles matter (admin, regular user, read-only), one test account per role.
- **API access:** how to get a token for calling the backend directly, such as a Keycloak password grant against `/realms/<realm>/protocol/openid-connect/token` with a given client. Check in the realm config that the client allows it.
- **Blockers:** anything an agent can't get past on its own. SSO through a real provider, SMS codes and CAPTCHAs usually need a bypass in the local profile, a dev-only login, or the user's help.

Credentials are the one thing you can't assume. If the app has auth and the repo has no test accounts (a realm export, a seed file), ask for one set per role once the section is confirmed. Only accept test accounts for local, dev or staging environments. If the user offers what looks like a real personal account or production credentials, say why that's a problem and ask for test accounts instead.

### Tests

Some projects want only unit tests, others only integration tests, others both plus end-to-end. Parts:

- **Kinds:** which kinds the project uses, and for each whether the agent writes new ones for new code, only runs existing ones, or leaves them alone.
- **Scope:** what counts as this kind here (a unit test mocks the repository; an integration test uses Testcontainers with a real Postgres).
- **Commands:** to run all of them, and to run a single test or file (`./mvnw test -Dtest=OrderServiceTest`, `npx ng test --include=src/app/orders`).
- **Needs:** anything a kind depends on, such as Docker for Testcontainers or the full stack for end-to-end tests.
- **Conventions:** framework and assertion library, where tests live, naming, what to mock, fixtures or builders to reuse, and any coverage threshold.
- **Skip by default:** slow or flaky suites, and when to run them anyway.

## 4. Write it down

Once all three sections are confirmed, write them. Drop the *(assumed)* marks on items the user confirmed.

- **Setup:** write the sections from [references/setup-template.md](references/setup-template.md) into `AGENTS.md` at the repo root, between `<!-- setup-project:start -->` and `<!-- setup-project:end -->`. Create the file if it doesn't exist. Replace the old section if there is one, and leave the rest of the file untouched. If an earlier run left a `setup-project` section in `CLAUDE.md`, move it to `AGENTS.md`.
- **Claude Code:** Claude Code reads `CLAUDE.md`, not `AGENTS.md`. If the project has a `CLAUDE.md` that doesn't import `AGENTS.md`, offer to add an `@AGENTS.md` line to it.
- **Credentials:** never write passwords into a committed file. If the credentials already live in the repo, reference that file. Otherwise write them to `.agents/test-accounts.md` and keep it out of git:

  ```bash
  git check-ignore -q .agents/test-accounts.md || echo ".agents/test-accounts.md" >> "$(git rev-parse --git-common-dir)/info/exclude"
  ```

  This writes to `.git/info/exclude`, which is local and never committed. Tell the user you added it, and that teammates will need their own copy.

## 5. Try it

Offer to prove the setup works. If the user agrees:

1. Start each service in order, or check it's running, and wait for its ready check.
2. Log in with each test account, through the UI using the chosen UI verification method and through the token call if there is one.
3. Run one test of each kind the user wants, using the single-test command.
4. Run the done checks.

Fix anything in the written setup that turned out to be wrong, and tell the user what you changed. If a step fails for a reason you can't fix, such as a missing secret, say which step and why, and leave it marked as unverified in the file.

Ask before stopping services you started. End with the path of the file you wrote and a one-line summary of what's covered.
