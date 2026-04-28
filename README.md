# Awesome Unraid

![awesome-unraid](https://socialify.git.ci/JSONbored/awesome-unraid/image?custom_description=Production-grade+Unraid+CA+templates+for+self-hosters+tired+of+half-baked+XML+files+-+ideal+for+beginners+%2B+power+users+alike.&custom_language=Dockerfile&description=1&font=Raleway&forks=1&issues=1&language=1&logo=https%3A%2F%2Favatars.githubusercontent.com%2Fu%2F42099010%3Fs%3D200%26v%3D4&name=1&owner=1&pattern=Signal&pulls=1&stargazers=1&theme=Light)

Unraid Community Applications catalog for JSONbored AIO templates.

[At A Glance](#at-a-glance) | [Templates](#template-catalog) |
[Candidate Pipeline](#candidate-pipeline) | [Quick Start](#quick-start) |
[Contributing](CONTRIBUTING.md)

---

## What Is Awesome Unraid?

Awesome Unraid is the catalog layer for JSONbored's Unraid-first AIO app
templates. It stores the Community Applications-facing XML files, icons,
screenshots, and maintainer profile assets that Unraid users import or discover.

- Source AIO repos own Dockerfiles, runtime behavior, tests, release automation,
  and app-specific documentation.
- This repo owns the catalog copies: root `*.xml` files, `icons/`,
  `screenshots/`, and `ca_profile.xml`.
- AIO templates are beginner-friendly by default, but they keep advanced
  configuration paths visible for users who need external services, SMTP,
  identity providers, reverse proxies, or other power-user controls.

## At A Glance

- Available templates: `7`
- In progress: `1`
- Candidate pipeline: active research backlog.
- Catalog assets: root XML templates, shared icons, screenshots, and the CA
  maintainer profile.

## Quick Start

1. Open Unraid Community Applications.
2. Install the template you want from this catalog.
3. Keep the beginner defaults for first boot unless the source repo docs say a
   field is required.
4. Use Advanced View only when you need external databases, mail relays, identity
   providers, reverse-proxy tuning, telemetry settings, or other app-specific
   overrides.
5. Use each source repo for detailed setup, support, release notes, and runtime
   troubleshooting.

## Template Catalog

### Available Templates (7)

- **[sure-aio](https://github.com/JSONbored/sure-aio)** - Self-hosted personal
  finance in the Maybe Finance family. Bundles the Sure web app, background
  worker, PostgreSQL, and Redis for a simpler first boot on Unraid.
- **[simplelogin-aio](https://github.com/JSONbored/simplelogin-aio)** -
  Self-hosted email aliases for protecting real inbox addresses. Bundles the web
  UI, background jobs, inbound email handler, Postfix, PostgreSQL, and Redis
  while keeping DNS and deliverability tradeoffs explicit.
- **[infisical-aio](https://github.com/JSONbored/infisical-aio)** -
  Self-hosted secrets management for teams, infrastructure, and application
  credentials. Bundles Infisical with PostgreSQL, Redis, and a local Mailpit
  inbox for reliable first boot and local email-dependent flows.
- **[mem0-aio](https://github.com/JSONbored/mem0-aio)** - Self-hosted Mem0
  OpenMemory for AI memory retention. Bundles the OpenMemory UI/API with Qdrant
  so users can start without wiring a separate vector database.
- **[khoj-aio](https://github.com/JSONbored/khoj-aio)** - Self-hosted AI second
  brain for chatting with documents, the web, and local or hosted LLMs. Bundles
  Khoj with PostgreSQL and `pgvector` for a practical Unraid-first install.
- **[signoz-aio](https://github.com/JSONbored/signoz-aio)** - Self-hosted
  observability for traces, metrics, and logs. Bundles SigNoz UI/API,
  OpenTelemetry collector, ClickHouse, and ZooKeeper into one Unraid-oriented
  deployment.
- **[signoz-agent](https://github.com/JSONbored/signoz-aio)** - Companion
  OpenTelemetry collector for remote or separate Docker hosts. Receives OTLP,
  optionally collects host metrics, Docker metrics, Docker logs, and Prometheus
  targets, then forwards telemetry into `signoz-aio` or another SigNoz endpoint.

### In Progress (1)

- **[nanoclaw-aio](https://github.com/JSONbored/nanoclaw-aio)** -
  Telegram-first agent orchestration aimed at a single-container Unraid
  deployment with Docker socket access and persistent runtime state. This repo is
  still being modernized and should not be treated as part of the current
  available template set yet.

## Candidate Pipeline

These are not published templates. They are candidate AIO ideas being researched
for future source repos, with priority given to apps that are popular on Unraid,
missing from Community Applications, or currently require users to wire multiple
containers and support services by hand.

### Upcoming Candidates

- **paperless-aio** - Paperless-ngx document management with PostgreSQL, Redis,
  Tika, and Gotenberg bundled for OCR, document conversion, and import workflows.
- **authentik-aio** - Identity provider and SSO gateway with server, worker,
  PostgreSQL, Redis, and optional LDAP/outpost-oriented configuration paths.
- **firefly-aio** - Personal finance stack with Firefly III, the Data Importer,
  database storage, scheduled jobs, and import/callback configuration.
- **netbox-aio** - Homelab IPAM/DCIM and network source of truth with NetBox,
  PostgreSQL, Redis, worker, housekeeping, and plugin-ready persistence.
- **immich-aio** - Photo and video management with the Immich server, machine
  learning service, database, cache, and media persistence under one Unraid
  template.
- **karakeep-aio** - Bookmark, note, and read-it-later archiving with Karakeep,
  Browserless, MeiliSearch, and optional AI tagging/search integrations.
- **dify-aio** - AI app and agent workflow platform with Dify core services,
  PostgreSQL, Redis, Weaviate, sandbox, SSRF proxy, plugin daemon, and web UI.
- **tubearchivist-aio** - YouTube media archiving with Tube Archivist, Redis,
  Elasticsearch, download storage, cache storage, and scheduler controls.
- **librechat-aio** - Multi-provider AI chat platform with MongoDB, MeiliSearch,
  RAG API, vector storage, model-provider settings, and optional Ollama paths.
- **langfuse-aio** - LLM observability and prompt/eval platform with Langfuse
  web, worker, PostgreSQL, ClickHouse, Redis/Valkey, and S3-compatible storage.
- **plane-aio** - Linear/Jira-style project management with Plane web/API,
  workers, PostgreSQL, Redis/Valkey, RabbitMQ, MinIO/S3, optional OpenSearch,
  and integration settings.
- **usesend-aio** - Self-hosted Resend/Postmark-style sending infrastructure
  with the useSend dashboard, database, Redis queueing, SMTP/API support, SES
  credentials, webhooks, and marketing email workflows.
- **byterover-aio** - AI coding-agent memory utility built around ByteRover's
  CLI daemon and local web UI. This needs feasibility work because ByteRover is
  currently a local-first CLI rather than a published Docker/Compose service.

### Discovery Backlog

- **AI and agent tooling**: OpenHands, LiteLLM gateway, Flowise, LobeChat,
  Crawl4AI, OpenLIT, Helicone, local/remote MCP servers, agent-memory systems,
  model-gateway dashboards, and AI developer tools with missing or fragmented
  Unraid coverage.
- **Developer platforms**: Huly, Twenty, ToolJet, Appsmith, Baserow, Docmost,
  Outline, Chatwoot, Zammad, Unkey-like API-key platforms, PostHog, and other
  developer/business platforms that require databases, queues, search, object
  storage, or background workers.
- **Business and marketing tools**: Unsend/useSend alternatives, list/newsletter
  tools, CRM/support desks, analytics tools, email API gateways, SMTP relays,
  webhook processors, and workflow automation apps that need databases, queues,
  storage, or mail-provider configuration.
- **Media and library tools**: RomM, GameVault, Kometa-adjacent utility stacks,
  FileFlows, Tdarr-style worker stacks, and other media tooling where the AIO
  value is reducing multi-container setup friction without hiding resource cost.

### Evaluation Criteria

- The app solves a common Unraid, homelab, AI, media, developer, or business
  workflow problem.
- The upstream deployment normally needs multiple services, databases, caches,
  object storage, queues, search engines, browser workers, or background
  processors.
- Beginner defaults can boot safely with minimal required fields.
- Advanced users can still override databases, caches, SMTP, auth, storage,
  reverse-proxy settings, resource limits, and provider integrations where the
  upstream app supports them.
- The AIO packaging does not hide meaningful tradeoffs such as Docker socket
  access, mail deliverability, search/index memory use, GPU requirements,
  bundled database backups, or heavy media/AI workloads.

## Catalog Structure

- Root `*.xml` files are the published or publication-ready Unraid templates.
- `icons/` contains shared icon assets referenced by template metadata.
- `screenshots/` contains catalog screenshots where available.
- `ca_profile.xml` defines the repository maintainer profile shown by Community
  Applications.
- `.github/FUNDING.yml` keeps sponsorship links aligned with the source AIO
  repos.

## Maintenance Model

- Fix app-specific behavior in the source AIO repo first.
- Validate source XML before syncing it into this catalog.
- Keep `TemplateURL`, `Icon`, `Project`, `Support`, `Overview`, and `Category`
  metadata aligned with the source repo.
- Prefer raw `awesome-unraid/main/...` URLs for `TemplateURL` and `Icon`.
- Remove stale catalog assets instead of leaving placeholders.
- `CHANGELOG.md` may summarize catalog changes, but app-specific release history
  belongs in the individual AIO repositories.

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=JSONbored/awesome-unraid,JSONbored/sure-aio,JSONbored/simplelogin-aio,JSONbored/infisical-aio,JSONbored/mem0-aio,JSONbored/khoj-aio,JSONbored/signoz-aio,JSONbored/nanoclaw-aio&theme=dark)](https://star-history.com/#JSONbored/awesome-unraid&JSONbored/sure-aio&JSONbored/simplelogin-aio&JSONbored/infisical-aio&JSONbored/mem0-aio&JSONbored/khoj-aio&JSONbored/signoz-aio&JSONbored/nanoclaw-aio&Date)
