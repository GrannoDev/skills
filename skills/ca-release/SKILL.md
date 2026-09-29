---
name: ca-release
description: Release a Climbalong Maven app by merging, versioning, tagging, pushing, and syncing develop. Run only when invoked by name.
argument-hint: "[branch]"
disable-model-invocation: true
---

# CA Release

Release to `main`/`master`, then sync `develop` to the release version plus `-SNAPSHOT`. Finish on `develop`. Ask for the version choice and, once the release is locally prepared, approval for all pushes; pushing deploys to production. Reuse explicit approvals already provided.

**Failure rule:** stop on failed commands, rejected pushes, failing hooks, or conflicts other than project-version conflicts. Report the failed command and current step. Do not reset, force, retry, or switch branches after failure.

## Version-conflict exception

Resolve a merge conflict only when every conflicted hunk is the root project's `<version>` or a module's `<parent><version>` referencing that root. Keep the side specified below, edit only conflict hunks, stage the resolved poms, and finish with `git commit --no-edit`. Report the resolution. Any dependency-version or other conflict stops the release. Never replace a whole pom with ours/theirs.

## 1. Prepare

Run `git fetch origin`, `git branch --show-current`, and `git status --short`.

- Production: `main` if local or on origin, otherwise `master`; stop if neither exists.
- Source: the named branch, otherwise the starting feature/bug branch, otherwise `develop` when starting on production or develop. Report `Releasing <source> → <prod>`.
- Uncommitted work: list it; it is included in the release commit except local runtime data/secrets/build output described below.
- Maven: `./mvnw` when present, otherwise `mvn`.
- When source is develop, fast-forward it: `git pull --ff-only` if currently there, otherwise `git fetch origin develop:develop`.

## 2. Merge into production

Run `git checkout <prod>` and `git pull --ff-only`. Stop if dirty work prevents checkout; do not stash or discard it.

Before merging, read the root project's own version (not its parent version) from production `pom.xml` and `<source>:pom.xml`. Then `git merge --no-edit <source>`. For permitted version conflicts, keep the **source** side.

## 3. Choose and set the version

Compare the saved production/source versions without `-SNAPSHOT`. If different, ask which to bump from. Offer Patch, Minor, Major in that order with exact resulting versions; if equal, use that common base.

Check `release/<version>` against fetched/local and origin tags. If already present, choose another version before proceeding. Stop on an unsupported version format rather than guessing.

```bash
<mvn> -q versions:set -DnewVersion=<version> -DgenerateBackupPoms=false
```

If the versions plugin is unavailable, edit only root-project/module versions by hand. Other Maven failures follow the failure rule. Verify all project/module versions are consistent.

## 4. Commit locally

Stage the release changes, including eligible uncommitted work, while excluding local runtime data and secrets: Keycloak/Azurite data, `__blobstorage__`, `__queuestorage__`, `__tablestorage__`, logs, `.env*`, IDE files, and build output. Classify by purpose; do not exclude source/config files merely because “keycloak” appears in their path. Report excluded paths.

Use explicit paths or `git add -A -- . ':!<excluded path>' ...`; inspect the staged diff. Commit `chore(release): <version>`, then tag:

```bash
git tag -a release/<version> -m "Release <version>"
```

## 5. Approve and push

Show this concrete summary and wait for authorization unless already supplied:

```text
Release <version> → <prod>
Source: <branch>
Commit: <hash> chore(release): <version>
Files: <changed release files>
Excluded: <paths, or None.>
Tag: release/<version>
Then: merge production into develop, set <version>-SNAPSHOT, push develop.
```

Approval covers all three pushes. Run `git push origin <prod>`, then `git push origin release/<version>`.

## 6. Sync develop

Run `git checkout develop`, `git pull --ff-only`, and `git merge --no-edit <prod>`. For permitted version conflicts, keep the **production** side.

```bash
<mvn> -q versions:set -DnewVersion=<version>-SNAPSHOT -DgenerateBackupPoms=false
git add -- '*pom.xml'
git commit -m "chore(release): <version>-SNAPSHOT"
git push origin develop
```

Use the same narrowly scoped version-edit fallback if the plugin is unavailable. Verify the updated versions before committing. Report release version, production branch, tag, develop snapshot, and final `git log --oneline -3` / `git status --short`. For a feature/bug source, mention its changes are now in develop.
