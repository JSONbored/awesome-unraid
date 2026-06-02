# Changelog

This repository tracks published Unraid template and icon updates for the
JSONbored AIO app fleet.

Notable changes are typically driven by:

- new app templates being added
- icon updates
- metadata or template corrections
- sync and maintenance cleanup

For app-specific release history, use the individual AIO repositories.
Some high-volume maintenance commits may be omitted here so this file stays readable.

This catalog is maintained continuously on `main` and does not require formal GitHub Releases.

## Unreleased

### CI

- Remove awesome-unraid release workflow
- Restore catalog changelog automation
- Auto-sync dify-aio assets
- Allow bot-token changelog PRs
- Add manual changelog trigger
- Publish Dify catalog template
- Sync dify-aio catalog assets
- Sync infisical-aio catalog assets
- Sync sure-aio catalog assets
- Sync sure-aio catalog assets
- Sync dify-aio catalog assets
- Sync security release templates
- Sync aio catalog templates
- Sync release template changes
- Sync simplelogin registration docs
- Sync simplelogin release notes
- Sync mem0 api bind address
- Sync mem0 release notes
- Sync sure alpha catalog package
- Sync sure alpha catalog template
- Update nanoclaw catalog template
- Update dify and infisical catalog templates
- Update nanoclaw catalog release notes
- Update infisical catalog release
- Update security release templates
- Sign Fleetbot catalog PRs
- Use Fleetbot client ID
- Verify existing Fleetbot PRs
- Sync security release templates
- Update release template changelogs
- Update Penpot template release notes
- Refresh released AIO catalog templates
- Refresh Khoj catalog history
- Sync CA template metadata
- Refresh release metadata catalog XML
- Refresh release catalog metadata
- Publish Sure referrer policy setting
- Publish Sure 0.7.1 catalog metadata
- Publish app release catalog metadata
- Centralize catalog automation
- Refresh catalog validation workflow

### Dependency Updates

- Update peter-evans/create-pull-request action to v8.1.1
- Update actions/checkout action to v6.0.3

### Documentation

- Update Sure-AIO description
- Add repository guidance
- Update maintainer profile metadata
- Add sure-aio screenshots
- Limit CA repo to sure-aio
- Sync mem0-aio template assets
- Sync mem0-aio template assets
- Sync infisical-aio template assets
- Sync mem0-aio template assets
- Sync mem0-aio template assets
- Sync infisical-aio template assets
- Refresh awesome-unraid README
- Add signoz agent template
- Add Dify icon asset
- Sync Dify setup guidance
- List dify template in catalog readme
- Sync sure-aio hotfix2 catalog changes
- Sync mem0 hardened template
- Document sure alpha customizations
- Note sure alpha revision tags
- Sync sure alpha shared image tag
- Validate readme template inventory
- Clarify sure alpha import wording
- Publish nanoclaw aio template
- Sync nanoclaw ca description
- Refresh nanoclaw template listing
- Sort AIO templates alphabetically
- List published image packages
- Sync infisical and nanoclaw templates

### Features

- Add SimpleLogin-AIO and SimpleLogin-Postfix CA templates
- Update to awesome-unraid
- Add 9 new production-quality templates
- Add all template builds from overnight session
- Add NanoClaw AIO template
- Add git-cliff release workflow
- Add sure alpha catalog template
- Add penpot-aio

### Fixes

- Correct repo references, rewrite README as proper awesome-list format, add star badges
- Point template Icon tags to raw GitHub master/main URLs
- Tighten changelog spacing
- Drop automated sync noise
- Use official SigNoz icon
- Hold Dify XML behind launch gate
- Sync simplelogin template name
- Prefer Docker Hub image metadata
- Normalize nanoclaw ca metadata

### Maintenance

- Sync local config drift for all modified AIO templates
- Cleanup repo, keep only confirmed complete AIO templates (SimpleLogin, Sure)
- Remove old title-cased xml files
- Standardize README, add FUNDING.yml, and clean up legacy files
- Standardize template
