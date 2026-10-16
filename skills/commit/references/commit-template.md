# Commit output

Summarize logical behavior changes, then propose a [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/) message:

```text
<type>[(<scope>)][!]: <description>

[body: why and resulting behavior; omit redundant details]

[footers]
```

Header: type, optional `(scope)`, optional `!`, then `: ` and the description with nothing between. Keep the header at most 72 characters; description is imperative, lowercase, with no final period.

Types: `feat`, `fix`, `refactor`, `perf`, `docs`, `test`, `style`, `build`, `ci`, `chore`, `revert`. Use `feat` whenever the commit adds a feature and `fix` whenever it fixes a bug. If changes fit several types, propose separate commits; when one commit is required, use the highest-impact type (`feat`, then `fix`). Scope is one lowercase noun naming a codebase section; omit for repo-wide work.

Body and footers are optional; each starts after one blank line. Wrap body at 72. Body is free-form paragraphs; secondary change bullets are optional when prose does not cover them. Never start a body line with `Word: ` or `Word #`, which parsers read as a footer.

Footers follow git trailer format: a token using `-` for spaces (`Reviewed-by`, `Refs`), then `: ` or ` #`, then the value. Use `Refs: <issue>` only for a supplied issue. For `revert`, describe what is reverted and add `Refs: <sha>[, <sha>]`.

Breaking changes, in any type: add `!` before the colon and a `BREAKING CHANGE: <impact>` footer (uppercase, exactly this token).
