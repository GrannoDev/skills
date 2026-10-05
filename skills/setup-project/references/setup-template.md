# Project setup template

Use for review and saved output. Include working directories; omit inapplicable rows. Unknown facts say `Unresolved`; unchecked facts say *(unverified)*. Use agent-neutral wording.

```markdown
<!-- setup-project:start -->
## Running the app

Prerequisites: <versions, env files, secret sources without values>

| Service, dependency order | Started by | Start (directory) | Ready check/timeout | URL | Stop, keeps data |
| --- | --- | --- | --- | --- | --- |
| <service> | <agent/user> | <command> | <check> | <URL> | <command> |

Migrations: <command and when>
Seed: <command or None>
Reset: <procedure requiring explicit authorization, or None>
Never: <off-limits environments/actions>

## Verifying changes

Required checks: <exact commands, directories, conditions>
Before commit/push: remove temporary files you created, preserving evidence awaiting review or supporting PR links; leave others' files alone. Temporary locations: <paths>.
UI verification: <when, target, affected flows, unavailable-tool fallback>
Auth: <method, account source, roles, enabled token command with placeholders>
Blockers: <missing accounts, MFA, SSO; workaround or None>

## Tests

| Kind | Write/run/leave alone | Run all (directory) | Run one (directory) | Needs |
| --- | --- | --- | --- | --- |
| <kind> | <policy> | <command> | <command> | <dependencies> |

Conventions: <framework, paths, naming, fixtures, mocks>
Skip by default: <suite and exception, or None>
<!-- setup-project:end -->
```

For new credentials, use an untracked, ignored `.agents/test-accounts.md` containing the environment URL and `Role | Username/email | Password | Notes` table. State that it is local only and each developer supplies their own copy.
