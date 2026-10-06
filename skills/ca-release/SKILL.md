---
name: ca-release
description: Release a Climbalong Maven app to main/master, tag and push it, then sync develop's snapshot version. Run only when invoked by name.
argument-hint: "[branch]"
disable-model-invocation: true
---

# CA release

On success, finish on `develop`. Reuse prior approvals; otherwise ask for version choice and, after local preparation, approval for all pushes. Pushing deploys production.

Use only the version-conflict exception below. Stop on other failed commands, hooks, or rejected pushes. Report the command/current step. Do not reset, force, retry, or switch branches after failure.

## Version-conflict exception

Resolve only conflicts where every hunk changes the root project's own `<version>` or a module `<parent><version>` referencing it. Edit conflict hunks only, stage resolved POMs, and `git commit --no-edit`. Keep incoming versions when merging into production and production versions when syncing develop. Dependency-version/other conflicts stop the release; never replace whole POMs with ours/theirs.

## POM version updates

Edit POM files directly with the usual file-editing tools. Do not run Maven or its wrapper to update versions. Update the root project's own version, module project versions that share it, and internal parent/dependency references between those released modules. If a property holds the release version, edit that property.

Preserve unrelated parent, dependency, and plugin versions and the existing formatting. Read the edited POMs and inspect their diff to verify version consistency.

## Release

1. Run `git fetch origin`, `git branch --show-current`, and `git status --short`. Choose production `main` if local/on origin, otherwise `master`; stop if neither exists. Source is the named branch, current feature/bug branch, or `develop` when starting on production/develop. Report source and production.
2. Starting on develop includes it automatically. Otherwise ask whether to include develop before merging, unless already answered. If declined, release only source; if source is develop, ask for another. List uncommitted work eligible for the release commit.
3. If including develop, fast-forward it with `git pull --ff-only` when there, otherwise `git fetch origin develop:develop`.
4. `git checkout <prod>` and `git pull --ff-only`; never stash/discard work to permit checkout. Save production/source POM project versions, excluding their parent versions. Merge develop first if included and distinct from source, then source, each once with `git merge --no-edit`.
5. Remove `-SNAPSHOT` from saved versions. If bases differ, ask which to bump. Offer Patch/Minor/Major with exact results. Reject unsupported formats and versions with existing local/origin `release/<version>` tags.
6. Set `<version>` by editing the POMs directly as described above, then verify version consistency.
7. Stage eligible release/uncommitted changes with explicit paths; inspect the staged diff. Exclude/report runtime data, Keycloak/Azurite stores, `__blobstorage__`, `__queuestorage__`, `__tablestorage__`, logs, `.env*`, IDE files, and build output. Classify by purpose, not names containing "keycloak".
8. Commit `chore(release): <version>` and `git tag -a release/<version> -m "Release <version>"`. Show version, production/source branches, develop inclusion, commit hash, files/exclusions, tag, and planned develop snapshot. Obtain approval for all three pushes unless already supplied.
9. Run `git push origin <prod>`, then `git push origin release/<version>`.

## Sync develop

Run `git checkout develop`, `git pull --ff-only`, and `git merge --no-edit <prod>`. Set `<version>-SNAPSHOT` by editing the POMs directly using the same rules, then verify versions. Stage POMs with `git add -- '*pom.xml'`, commit `chore(release): <version>-SNAPSHOT`, then `git push origin develop`.

Report release version, production branch, tag, develop snapshot, `git log --oneline -3`, and `git status --short`. For a feature/bug source, state that its changes are now in develop.
