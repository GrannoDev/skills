# Commit output

Summarize logical behavior changes, then propose:

```text
<type>(<scope>): <imperative summary>

<Why and resulting behavior; omit redundant details>

<footers when applicable>
```

Types: `feat`, `fix`, `refactor`, `perf`, `docs`, `test`, `style`, `build`, `ci`, `chore`, `revert`. Use the dominant type, preferring feat then fix. Scope is one lowercase module/feature word; omit for repo-wide work. Subject is lowercase after the colon, has no final period, and is at most 72 characters. Wrap body at 72.

Mark breaking changes with `!` and `BREAKING CHANGE: <impact>`. Use `Refs: <issue>` only for a supplied issue. Secondary change bullets are optional when prose does not cover them.
