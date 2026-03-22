# awesome-unraid
Production-grade Unraid CA templates for self-hosters tired of half-baked XML files — every env var documented, sane defaults, working init scripts, and actually maintained.

![Build Status](https://img.shields.io/github/actions/workflow/status/JSONbored/awesome-unraid/build.yml?branch=main)
![License](https://img.shields.io/github/license/JSONbored/awesome-unraid)
![Stars](https://img.shields.io/github/stars/JSONbored/awesome-unraid)

## Add to Unraid Community Applications
Apps → Settings → Template Repositories → add:
https://github.com/JSONbored/awesome-unraid

## Templates

### 📧 Email & Communication 
| Template | Image | Replaces | Description |
|---|---|---|---|
| SimpleLogin-AIO | ghcr.io/jsonbored/simplelogin-aio | SimpleLogin SaaS | Self-hosted email alias service — full stack in one container |
| SimpleLogin-Postfix | simplelogin/postfix | — | MTA companion for SimpleLogin |

### 🛠 Utilities 
| Template | Image | Replaces | Description |
|---|---|---|---|
| Stirling-PDF | ghcr.io/stirling-tools/s-pdf | Adobe Acrobat / SmallPDF | Local PDF manipulation — merge, split, compress, convert |
| Wallos | ellite/wallos | Truebill / Rocket Money | Self-hosted subscription tracker |

## Setup Guides
- [SimpleLogin Setup Guide](docs/simplelogin-setup.md)
- [SimpleLogin Manual Install Guide](docs/manual-install-guide.md)
- [Stirling-PDF Setup Guide](docs/stirling-pdf-setup.md)
- [Wallos Setup Guide](docs/wallos-setup.md)

## Contributing
Templates must meet these standards before inclusion: every environment variable documented, tested end-to-end, actively maintained, proper defaults set, sensitive variables masked.

## License
MIT — see LICENSE

---
Built by @JSONbored
