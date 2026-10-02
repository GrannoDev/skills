# Project setup template

Use the same structure for review and for the saved `AGENTS.md` block. Replace placeholders with detected/confirmed values, omit inapplicable rows, and use `None.` for empty lists. Commands include their working directory. Unknown values say `Unresolved: <what is needed>`; unchecked facts say *(unverified)*.

```markdown
<!-- setup-project:start -->
## Running the app

Prerequisites: <tool versions, env files, and secret sources; no secret values>

Services in dependency order:

| Service | Started by | Start (directory) | Ready when | URL | Stop (keeps data) |
| --- | --- | --- | --- | --- | --- |
| <name> | <agent / user> | `<command>` (`<dir>`) | <check and timeout> | <URL> | `<command>` or Ctrl+C |

Data:
- Migrations: <how and when they run>
- Seed: <command and directory, or None.>
- Reset (destructive; requires explicit authorization): <procedure, or None.>

Never: <off-limits environments/actions>

## Verifying changes

Required checks:
- `<command>` (`<dir>`) — <when required and what it checks>

UI verification: <when required, target (browser URL, simulator, emulator), affected-flow checks, what to do if it cannot be done; no agent-specific tool names>

### Auth

Type: <none / login method>
Test accounts: <existing source or local-only .agents/test-accounts.md>
Roles: <relevant roles>
API token: <enabled grant/command using credential placeholders, or None.>
Blockers: <missing accounts, MFA, external SSO, etc.; workaround or None.>

## Tests

| Kind | Write / run only / leave alone | Run all (directory) | Run one (directory) | Needs |
| --- | --- | --- | --- | --- |
| <kind> | <policy> | `<command>` (`<dir>`) | `<command>` (`<dir>`) | <dependencies> |

Conventions: <frameworks, locations, naming, boundaries to mock, reusable fixtures>
Skip by default: <suite and when to run it anyway, or None.>
<!-- setup-project:end -->
```

## Local test accounts

Only create `.agents/test-accounts.md` after confirming it is untracked and gitignored. Reference existing credentials instead when available.

```markdown
# Test accounts

Environment: <local/dev/staging URL>
Local only; not committed. Each developer keeps their own copy.

| Role | Username / email | Password | Notes |
| --- | --- | --- | --- |
| <role> | <test username> | <test password> | <restrictions> |
```
