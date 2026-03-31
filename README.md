# Awesome Unraid

Published Unraid XML templates and shared icons for the JSONbored AIO app repos.

This repo is the distribution layer for Community Applications style templates. The
source of truth for app behavior, CI, Dockerfiles, and detailed app docs lives in
the individual AIO repos. This repo stores the synced XML and icon assets that
Unraid users actually import.

It also contains the repository-level Community Applications maintainer profile
used by CA when showing repository and author information.

## Included Templates

- [sure-aio](https://github.com/JSONbored/sure-aio)
- [signoz-aio](https://github.com/JSONbored/signoz-aio)
- [khoj-aio](https://github.com/JSONbored/khoj-aio)
- [simplelogin-aio](https://github.com/JSONbored/simplelogin-aio)
- [nanoclaw-aio](https://github.com/JSONbored/nanoclaw-aio)
- [mem0-aio](https://github.com/JSONbored/mem0-aio)

## How This Repo Fits Together

- Root `*.xml` files are the published Unraid templates.
- `ca_profile.xml` defines the repository maintainer profile for Community Applications.
- `icons/` contains the shared icon assets referenced by those templates.
- The app repos sync their XML and icon updates here.
- The sync model is intentionally simple: app repos should only need the
  `SYNC_TOKEN` secret. Target paths should be hardcoded per repo rather than
  relying on GitHub repository variables.

## Maintenance Notes

- Keep template metadata aligned with the source AIO repos.
- Prefer raw `awesome-unraid/main/...` URLs for `TemplateURL` and `Icon`.
- Remove stale templates, docs, and icons instead of leaving placeholders behind.

## Catalog History

This repository is intended to be a continuously updated catalog on `main`, not a formal release-managed artifact repository.

For app-specific release history, use the individual AIO repositories.

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=JSONbored/awesome-unraid,JSONbored/sure-aio,JSONbored/signoz-aio,JSONbored/khoj-aio,JSONbored/simplelogin-aio,JSONbored/nanoclaw-aio,JSONbored/mem0-aio&theme=dark)](https://star-history.com/#JSONbored/awesome-unraid&JSONbored/sure-aio&JSONbored/signoz-aio&JSONbored/khoj-aio&JSONbored/simplelogin-aio&JSONbored/nanoclaw-aio&JSONbored/mem0-aio&Date)
