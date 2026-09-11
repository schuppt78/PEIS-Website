# Environment Variables Reference

## 1. Overview
The Phase 1 PEIS public website is designed with **zero mandatory runtime environment variables**.

All public marketing and recruitment pages render completely statically without server-side environment secrets.

---

## 2. Optional Environment Variables (For Future / Enhanced Backends)

If a serverless form endpoint or local development server is configured, the following optional variables can be utilized:

| Variable | Default Value | Description |
| :--- | :--- | :--- |
| `PEIS_WEBSITE_PORT` | `8000` | Port for the local development server (`scripts/serve.py`). |
| `PEIS_BETA_LOG_PATH` | `scratch/beta_applications.log` | Local destination for JSON beta application logs during testing. |
| `PEIS_ANALYTICS_ID` | `""` | Optional privacy-preserving analytics site identifier (e.g. Plausible / Cloudflare Web Analytics). |
| `PEIS_PUBLIC_URL` | `https://peisintel.com` | Canonical URL used for sitemap generation and Open Graph tags. |

---

## 3. Security Guarantee
- No credentials, API keys, or database secrets are included in this repository.
- Do not commit `.env` files containing sensitive keys to version control.
