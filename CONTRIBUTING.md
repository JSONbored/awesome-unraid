# Contributing

This repo is intentionally small and distribution-focused.

## What Belongs Here

- published Unraid `*.xml` templates
- the repository-level `ca_profile.xml`
- shared icon assets referenced by those templates
- lightweight documentation about repo structure and maintenance

## What Usually Does Not Belong Here

- app runtime code
- upstream integration logic
- large app-specific setup guides that are better maintained in the source AIO repo

## Workflow

1. Make changes in the source AIO repo when the change is app-specific.
2. Sync or copy the final XML and icon asset into this repo.
3. Keep `TemplateURL`, `Icon`, and maintainer profile assets pointed at raw `awesome-unraid/main/...` URLs.
4. Avoid adding placeholder docs or stale catalog leftovers.
