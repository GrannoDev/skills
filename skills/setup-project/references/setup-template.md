# Setup template

Write this into `AGENTS.md` at the repo root, between the markers. Fill in every placeholder, drop rows and sections that don't apply, and keep commands copy-pasteable. Mark anything that couldn't be verified with *(unverified)*.

```markdown
<!-- setup-project:start -->
## Running the app

Prerequisites: <tool versions, env files, secrets and where to get them>

Start in this order:

| Service | Start (from dir) | Ready when | URL | Stop |
| --- | --- | --- | --- | --- |
| Postgres | `docker compose up -d postgres` (repo root) | port 5432 accepts connections | localhost:5432 | `docker compose stop postgres` |
| Keycloak | `docker compose up -d keycloak` (repo root) | `http://localhost:8180/realms/<realm>` returns 200 | http://localhost:8180 | `docker compose stop keycloak` |
| Backend | `SPRING_PROFILES_ACTIVE=local ./mvnw spring-boot:run` (`backend/`) | `/actuator/health` is `UP` | http://localhost:8080 | Ctrl+C |
| Frontend | `npm start` (`frontend/`) | "Compiled successfully" in the log | http://localhost:4200 | Ctrl+C |

Who starts it: <the agent starts everything / the user runs it from the IDE; check with …>

Data: <how migrations run, how to seed, how to reset to a clean state>

Never: <off-limits actions, such as connecting to the shared dev database>

## Verifying changes

A change is done when these pass:

1. `<build command>`
2. `<lint / format / type check command>`
3. `<tests that must pass>`
4. UI changes are checked as described under UI verification

UI verification: <the harness's built-in browser / iOS Simulator / Android emulator / …>, <after every UI change / only when asked>. Open the changed screen, exercise it, and check the console for errors. If it isn't available: <fallback, such as Playwright scripts or asking the user>.

### Auth

Type: <email and password / Keycloak login page / SSO / magic link / …>

Test accounts: see `.agents/test-accounts.md` (local only, not committed; ask the user if it's missing). Roles: <admin, user, …>

API token: `<curl command for the token endpoint, with the password as a placeholder>`

Blockers: <anything the agent can't do alone, and the workaround>

## Tests

| Kind | Agent writes new ones? | Run all | Run one | Needs |
| --- | --- | --- | --- | --- |
| Unit | yes | `./mvnw test` | `./mvnw test -Dtest=<Class>` | nothing |
| Integration | yes | `./mvnw verify -Pintegration` | `./mvnw verify -Dit.test=<Class>` | Docker (Testcontainers) |
| Frontend unit | yes | `npm test -- --watch=false` | `npx ng test --include=<path>` | Chrome |
| End-to-end | run only | `npx playwright test` | `npx playwright test <file>` | full stack running |

Conventions: <frameworks, where tests live, naming, what to mock, fixtures and builders to reuse, coverage threshold>

Skip by default: <slow or flaky suites, and when to run them anyway>
<!-- setup-project:end -->
```

## Test accounts file

Write this to `.agents/test-accounts.md` when the credentials don't already live in the repo:

```markdown
# Test accounts

Local and dev only. Not committed; each developer keeps their own copy.

| Role | Username / email | Password | Notes |
| --- | --- | --- | --- |
| admin | admin@example.test | <password> | |
| user | user@example.test | <password> | |
```
