# Commit output

## Change summary

```text
<Short title>

- <type>: <one logical behavior change>
```

Group related edits across files; describe behavior rather than listing paths. Types: `feat`, `fix`, `refactor`, `perf`, `docs`, `test`, `style`, `build`, `ci`, `chore`, `revert`. Mark breaking changes with `!`.

## Message

```text
<type>(<scope>): <imperative summary>

<Why the change was made and what it does.>

- <type>: <secondary logical change, if any>

<footers, if applicable>
```

Use the dominant type (`feat` before `fix` before the rest). Subject: lowercase after the colon, no trailing period, at most 72 characters. Scope: one lowercase module/feature word; omit it for repo-wide changes. Wrap body lines at 72 characters. Omit secondary bullets when the prose already covers the whole change.

Use `BREAKING CHANGE: <impact>` for breaking changes and `Refs: <issue>` only for a user-provided issue. No invented issue references.
