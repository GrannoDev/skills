---
name: ca-release
description: Release a Climbalong Maven application to production. Merges develop into main/master, bumps the pom version, tags release/x.y.z, pushes, then merges back into develop as the next -SNAPSHOT and pushes develop. Run only when the user invokes it by name.
argument-hint: "[branch]"
disable-model-invocation: true
---

# CA Release

Merge into the production branch, bump the version, tag, push, and bring develop back in sync. Ask about the version bump and ask once more before pushing. Do everything else without stopping.

The user can start from any branch: the production branch, `develop`, or a feature or bug branch. A successful release always ends on `develop`.

If any command fails (a merge conflict other than the version, a rejected push, a failing hook), stop where you are, show the output, and say which step you reached. Don't reset, force, retry or switch branches on your own.

## Version conflicts

Both merges (steps 2 and 6) often conflict on the pom version. Resolve these yourself when every conflicted hunk is the project version: the root `<version>`, or a module's `<parent><version>` pointing at the root project.

- In each hunk, keep the side named in that step. The version gets set right afterwards anyway.
- Edit the conflict markers by hand. Don't use `git checkout --ours/--theirs` on the whole file, because that throws away the other side's non-conflicting changes.
- Run `git add` on the resolved poms and `git commit --no-edit` to finish the merge. Tell the user in one line that you resolved a version conflict.

For any other conflict, such as dependency versions, other pom changes or other files, stop and hand over to the user.

## 1. Prepare

Run these in the repo root:

```bash
git fetch origin
git branch --show-current
git status --short
```

- **Production branch:** use `main` if it exists locally or on origin, otherwise `master`. If neither exists, stop.
- **Source branch:** what gets merged into production.

  | Starting on | Source |
  | --- | --- |
  | the production branch | `develop` |
  | `develop` | `develop` |
  | a feature or bug branch | that branch |

  A branch the user names overrides this.
- **Uncommitted changes:** they come along into the release commit (step 4). If there are any, list them briefly.
- **Maven:** use `./mvnw` if it exists, otherwise `mvn`.

If the source is `develop`, bring it up to date with origin first. When you're on `develop`, run `git pull --ff-only`. From any other branch, run `git fetch origin develop:develop`, which fast-forwards it without switching.

Tell the user the plan in one line, for example `Releasing develop → master`.

## 2. Merge into production

```bash
git checkout <prod>
git pull --ff-only
```

Before merging, read the project version from the root `pom.xml` (the project's own `<version>`, not the `<parent>` one). Read the source's version too, with `git show <source>:pom.xml`. Step 3 compares them. Then merge:

```bash
git merge --no-edit <source>
```

If the checkout refuses because of uncommitted changes, stop and hand over to the user. If the merge conflicts on the version, resolve it as described in [Version conflicts](#version-conflicts), keeping the source side.

## 3. Choose the version

Compare the two versions you read in step 2, both without `-SNAPSHOT`:

- **Production:** the production branch's version before the merge.
- **Source:** the source branch's version.

**If they match** (for example master `1.2.3`, develop `1.2.3-SNAPSHOT`), bump from that version.

**If they differ** (for example master `1.2.3`, develop `1.2.4-SNAPSHOT`), show both and ask which one to bump from:

```
The versions don't match: master is 1.2.3, develop is 1.2.4-SNAPSHOT.
Which version should the bump start from?

- master (1.2.3)
- develop (1.2.4)
```

Then ask which bump to make. Use a question tool if you have one, with the options in this order:

```
Bumping from 1.2.3

- Patch → 1.2.4
- Minor → 1.3.0
- Major → 2.0.0
```

Check that the tag doesn't already exist (`git tag -l release/<version>`). If it does, say so and ask again.

Set the version across all modules:

```bash
<mvn> -q versions:set -DnewVersion=<version> -DgenerateBackupPoms=false
```

If the versions plugin isn't available, edit the `<version>` in each `pom.xml` by hand.

## 4. Commit

Stage everything except scrap files: local runtime data and secrets that must never be released. These include:

- Keycloak and Azurite data (anything named `*keycloak*`, `*azurite*`, `__blobstorage__`, `__queuestorage__`, `__tablestorage__`)
- logs, `.env*` files, IDE files and build output

Only exclude scrap files that git would otherwise pick up. Files already covered by `.gitignore` are ignored anyway.

```bash
git add -A -- . ':!<scrap path>' ...
git commit -m "chore(release): <version>"
```

## 5. Tag and push

Tag the release:

```bash
git tag -a release/<version> -m "Release <version>"
```

Before pushing, show a short summary and wait for the user's go-ahead. Pushing deploys to production.

```
Release 1.5.0 → master
  merged: develop
  commit: chore(release): 1.5.0  (pom.xml, api/pom.xml, …)
  left out: azurite/, keycloak/realm-export.json
  tag: release/1.5.0
  then: develop → 1.5.0-SNAPSHOT, pushed
```

This one approval covers every push in the release, including `develop` in step 6.

On approval:

```bash
git push origin <prod>
git push origin release/<version>
```

## 6. Back to develop

```bash
git checkout develop
git pull --ff-only
git merge --no-edit <prod>
```

If the merge conflicts on the version, resolve it as described in [Version conflicts](#version-conflicts), keeping the production side. Then:

```bash
<mvn> -q versions:set -DnewVersion=<version>-SNAPSHOT -DgenerateBackupPoms=false
git add -- '*pom.xml'
git commit -m "chore(release): <version>-SNAPSHOT"
git push origin develop
```

Finish on `develop` with `git log --oneline -3` and `git status --short`. If the release started from a feature or bug branch, say that its changes are now in `develop` as well.
