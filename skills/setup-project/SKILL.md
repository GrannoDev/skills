---
name: setup-project
description: Interview the user about how to run a project's app, how to verify changes (including auth and test accounts) and which tests to write and run, then save the answers to AGENTS.md for every future agent session. Run only when the user invokes it by name.
argument-hint: "[-q]"
disable-model-invocation: true
---

# Setup Project

Find out how to run this project, how to check that a change works, and which tests the user wants. Save the answers to the project's `AGENTS.md` so later sessions, and skills like `/break-ui`, `/use-tdd` and `/blueprint-build`, can start the app, log in and run the right tests without asking again.

Detect everything you can from the repo first. Only ask about what the code doesn't answer, and ask the user to confirm what you found.

## Asking questions

If you have a question tool (such as `AskUserQuestion`), use it for every question in this skill instead of asking in plain text:

- Group related questions into one call, up to the tool's limit (4 for `AskUserQuestion`). Keep each call to one topic: services, auth or tests.
- Offer what you detected as the options and put the likeliest first, marked "(Recommended)". The user can always pick "Other" and type an answer.
- Use multi-select when several answers can be true, such as which services to run or which kinds of tests to write.
- Put the file or command an option came from in its description (`from docker-compose.yml`).
- Ask for values you can't offer as options, such as passwords, in plain text.

If you don't have a question tool, ask in plain text: a few numbered questions at a time, each with your detected guess, so the user can answer "yes" or correct it.

## Quick mode with `-q`

If the user passes `-q` (`/setup-project -q`), don't interview:

- **Decide:** fill in every section yourself from the repo, marking each answer you inferred with *(assumed)*.
- **Ask only for credentials:** if the app has auth and the repo has no test accounts, ask for them. You can't guess them.
- **Review:** show the whole draft once and ask for approval before writing it. Start with one line telling the user to check the *(assumed)* items first.

Everything else in this skill still applies.

## 1. Detect

Read what's there before asking anything:

- **Existing setup:** `AGENTS.md`, `CLAUDE.md` and any earlier `setup-project` section (between `<!-- setup-project:start -->` and `<!-- setup-project:end -->`). If one exists, offer to update it instead of starting over.
- **Services:** `docker-compose*.yml`, `compose*.yml`, Dockerfiles, `Makefile`, `justfile`, scripts in `package.json`, and the README.
- **Backend:** `pom.xml` or `build.gradle*`, `mvnw`/`gradlew`, `application*.yml`/`.properties` (profiles, ports, datasource, issuer URI), migrations (Flyway, Liquibase) and seed data.
- **Frontend:** `package.json`, `angular.json` or other framework config, proxy config, environment files, the Node version (`.nvmrc`, `engines`).
- **Auth:** Keycloak realm exports, OIDC/OAuth config, security config classes, login routes, seeded users.
- **Tests:** test folders and frameworks (JUnit, Mockito, Testcontainers, Jasmine/Karma, Jest, Vitest, Playwright, Cypress) and coverage config.
- **Env and prerequisites:** `.env.example`, required env vars, tool versions (`.sdkmanrc`, `.tool-versions`, `.java-version`).

Keep notes of what you found and where. You'll use them as the options in the questions below.

## 2. Running the app

Confirm the list of things to run, in start order. For a typical stack that's something like: Keycloak container, Postgres container, Spring Boot backend, Angular frontend. For each one, pin down:

- **Start:** the exact command and the directory to run it in, including profile or env (`SPRING_PROFILES_ACTIVE=local ./mvnw spring-boot:run`).
- **Ready when:** a port, a health URL (`/actuator/health`) or a log line, so the agent knows when to move on.
- **URL and port:** where it's reachable once it's up.
- **Stop:** how to stop it and, if different, how to wipe its data.

Then ask about the whole setup:

- **Who starts it:** should the agent start the services itself, or does the user usually have them running already (for example from the IDE)? If already running, how can the agent check?
- **Prerequisites:** tool versions, env vars or `.env` files, secrets the agent needs and where they come from.
- **Data:** how migrations run, how to seed test data, and how to reset to a clean state.
- **Off-limits:** anything the agent must never do, such as connecting to a shared or production database or running a destructive reset without asking.

## 3. Verifying changes

Ask how the user wants a change checked before it counts as done: build, lint, format, type check, tests, a manual check in the browser, or a mix. Get the exact command for each.

Then ask whether the app has auth. If it does:

- **Type:** email and password on the app's own form, a Keycloak or other OIDC login page, SSO through Google or Microsoft, a magic link or email code, MFA or one-time codes, API keys, or basic auth.
- **Roles:** which roles matter (admin, regular user, read-only). Ask for one account per role the agent will need.
- **Credentials:** ask the user for a set of test credentials per role. If they're already in the repo (a realm export, a seed file), confirm them and note where they live instead.
- **API access:** how to get a token for calling the backend directly, such as a Keycloak password grant against `/realms/<realm>/protocol/openid-connect/token` with a given client. Check that the client allows it.
- **Blockers:** anything an agent can't get past on its own. SSO through a real provider, SMS codes and CAPTCHAs usually need a bypass in the local profile, a dev-only login, or the user's help. Say so and ask which applies.

Only accept test accounts for local, dev or staging environments. If the user offers credentials that look like a real personal account or production, say why that's a problem and ask for test accounts instead.

## 4. Tests

Ask which kinds of tests the project wants. Some projects want only unit tests, others only integration tests, others both plus end-to-end. For each kind:

- **Write or run:** should the agent write new tests of this kind for new code, only run existing ones, or leave it alone?
- **Scope:** what counts as this kind here (a unit test mocks the repository; an integration test uses Testcontainers with a real Postgres).
- **Commands:** to run all of them, and to run a single test or file (`./mvnw test -Dtest=OrderServiceTest`, `npx ng test --include=src/app/orders`).
- **Needs:** anything it depends on, such as Docker for Testcontainers or the full stack running for end-to-end tests.
- **Conventions:** framework and assertion library, where tests live, naming, what to mock, test data builders or fixtures to reuse, and any coverage threshold.

Also ask which tests must pass before the agent calls a change done, and whether any are slow or flaky enough to skip by default.

## 5. Write it down

Show the full draft and ask the user to confirm or change it. Then write it:

- **Setup:** write the sections from [references/setup-template.md](references/setup-template.md) into `AGENTS.md` at the repo root, between `<!-- setup-project:start -->` and `<!-- setup-project:end -->`. Create the file if it doesn't exist. Replace the old section if there is one, and leave the rest of the file untouched. If an earlier run left a `setup-project` section in `CLAUDE.md`, move it to `AGENTS.md`.
- **Claude Code:** Claude Code reads `CLAUDE.md`, not `AGENTS.md`. If the project has a `CLAUDE.md` that doesn't import `AGENTS.md`, offer to add an `@AGENTS.md` line to it.
- **Credentials:** never write passwords into a committed file. If the credentials already live in the repo, reference that file. Otherwise write them to `.agents/test-accounts.md` and keep it out of git:

  ```bash
  git check-ignore -q .agents/test-accounts.md || echo ".agents/test-accounts.md" >> "$(git rev-parse --git-common-dir)/info/exclude"
  ```

  This writes to `.git/info/exclude`, which is local and never committed. Tell the user you added it, and that teammates will need their own copy.

## 6. Try it

Offer to prove the setup works. If the user agrees:

1. Start each service in order, or check it's running, and wait for its ready check.
2. Log in with each test account, through the UI if you have a browser tool and through the token call if there is one.
3. Run one test of each kind the user wants, using the single-test command.
4. Run the "done" checks from step 3.

Fix anything in the written setup that turned out to be wrong, and tell the user what you changed. If a step fails for a reason you can't fix, such as a missing secret, say which step and why, and leave it marked as unverified in the file.

Ask before stopping services you started. End with the path of the file you wrote and a one-line summary of what's covered.
