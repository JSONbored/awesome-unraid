# awesome-unraid

> Production-grade Unraid CA templates for self-hosters tired of half-baked XML files — every env var documented, sane defaults, working init scripts, and actually maintained.

![Image]()
![Image]()
![Image]()
![Image]()

## Add to Unraid Community Applications

Apps → Settings → Template Repositories → add:

https://github.com/JSONbored/awesome-unraid

## Templates

### 📧 Email & Communication

| Template | Image | Replaces | Annual Savings |
|---|---|---|---|
| SimpleLogin-AIO | ghcr.io/jsonbored/simplelogin-aio | SimpleLogin SaaS / Proton Unlimited | $36–$156/yr |
| SimpleLogin-Postfix | simplelogin/postfix | — | — |

### 📊 Analytics

| Template | Image | Replaces | Annual Savings |
|---|---|---|---|
| Umami | ghcr.io/umami-software/umami | Google Analytics / Fathom | $168/yr |

### 🔐 Security & Secrets

| Template | Image | Replaces | Annual Savings |
|---|---|---|---|
| Infisical | infisical/infisical | Doppler / HashiCorp Vault Cloud | $156/yr |

### 📋 Productivity & Project Management

| Template | Image | Replaces | Annual Savings |
|---|---|---|---|
| Listmonk | listmonk/listmonk | Mailchimp / Brevo | $300+/yr |
| Formbricks | ghcr.io/formbricks/formbricks | Typeform / SurveyMonkey | $600/yr |
| Vikunja | vikunja/vikunja | Todoist / Asana | $48/yr |

### 💰 Finance & Subscriptions

| Template | Image | Replaces | Annual Savings |
|---|---|---|---|
| Actual Budget | actualbudget/actual-server | YNAB | $99/yr |
| Wallos | ellite/wallos | Rocket Money / Truebill | $48/yr |

### 🏠 Homelab & Infrastructure

| Template | Image | Replaces | Annual Savings |
|---|---|---|---|
| Glance | glanceapp/glance | Paid dashboards | — |
| Stirling-PDF | ghcr.io/stirling-tools/s-pdf | Adobe Acrobat / SmallPDF | $180/yr |

### 🔖 Bookmarks & Read Later

| Template | Image | Replaces | Annual Savings |
|---|---|---|---|
| Hoarder | ghcr.io/hoarder-app/hoarder | Pocket Premium / Instapaper | $45/yr |

## Requirements

All templates require:
- Unraid 6.12 or newer
- A Docker network (create with: docker network create homelab_net)

Most templates also require one or both of:
- PostgreSQL — any postgres container works. Recommended: postgres-shared from CA
- Redis — any redis container works. Recommended: redis-shared from CA

## Setup Guides

| Template | Setup Guide |
|---|---|
| SimpleLogin-AIO | Full Setup Guide · Manual Install |
| Umami | Setup Guide |
| Infisical | Setup Guide |
| Listmonk | Setup Guide |
| Formbricks | Setup Guide |
| Vikunja | Setup Guide |
| Actual Budget | Setup Guide |
| Wallos | Setup Guide |
| Glance | Setup Guide |
| Stirling-PDF | Setup Guide |
| Hoarder | Setup Guide |

## Roadmap

Templates currently in research or development:

- Formbricks — survey and feedback platform replacing Typeform
- Twenty CRM — open source CRM replacing HubSpot (complex, future)
- Karakeep — read-it-later replacing Instapaper
- SigNoz — observability platform replacing Datadog

## Standards

Every template in this repo meets these requirements before inclusion:

- Every environment variable from the upstream app is documented
- Sensitive variables are masked
- Tested end-to-end on a real Unraid installation
- Actively maintained and updated when upstream releases new versions
- Setup guide included

## Contributing

Found a bug or want to add a template? Open an issue or PR. Templates must meet the standards above before merging.

## License

MIT — see LICENSE

---

Built by @JSONbored