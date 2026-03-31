# AGENTS.md

This repository is the central Unraid catalog for the broader AIO portfolio.

## Repository intent

- Treat this repo as the source of truth for CA-facing XML and icon assets.
- Keep catalog content accurate, stable, and user-facing.
- Favor consistency and clarity over one-off exceptions.

## Engineering expectations

- External repo sync flows should create or update PRs rather than pushing directly to protected branches.
- Keep template, icon, and catalog metadata aligned with the app repos they represent.
- Avoid stale or placeholder catalog content.

## Release model

- This repo is a continuously updated catalog on `main`, not a formal release-managed artifact repo.
- `CHANGELOG.md` may still be refreshed automatically to summarize catalog history.
- Keep changelog-friendly Conventional Commit titles and PR titles so catalog history stays readable.

## Catalog expectations

- User-facing metadata must remain accurate:
  - `Project`
  - `Support`
  - `TemplateURL`
  - `Icon`
  - `Overview`
  - `Category`
- Support links should point to the intended public support destination.
- Icons and XML assets should remain in sync with the catalog README and docs.

## Community Apps expectations

- Maintain CA-readiness as a first-class concern.
- Keep repository content suitable for public review and moderation.
- Do not assume private operational context or unpublished internal tooling.
