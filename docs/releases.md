# Releases

`awesome-unraid` should use normal semver releases such as `v0.1.0`.

This repository is the catalog and distribution layer for shared XML templates and icons, so its releases represent catalog milestones rather than upstream application versions.

## What a catalog release means

A catalog release can include:

- new app templates
- icon additions or replacements
- metadata and support-link corrections
- README and documentation improvements
- sync and catalog automation changes

## Release flow

1. Trigger the **Release / Awesome Unraid** workflow from `main`.
2. The workflow computes the next semver version with `git-cliff --bumped-version`.
3. It opens a release PR that updates `CHANGELOG.md`.
4. Merge that PR into `main`.
5. After merge, the workflow creates the Git tag and GitHub Release automatically.
