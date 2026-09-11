# PEIS Public Website — PEIS Intelligence LLC

Welcome to the standalone public website repository for the **Project Evaluation Intelligence System (PEIS)**, developed and operated by **PEIS Intelligence LLC**.

This repository hosts the official marketing, informational, validation reporting, and Founding Beta recruitment platform at `https://peisintel.com`.

---

## 🔒 Configuration Control & Isolation
This project is strictly isolated from the core analytical software repository. In accordance with governing directives:
* Zero modifications have been or will be made to core analytical modules.
* Zero references to unrelated external applications or roadmaps are present in this repository.
* The website operates as an independent, lightweight, high-performance static web property with zero runtime dependencies on the PEIS backend.

---

## 📁 Repository Structure

```
PEIS Website/
├── index.html                     # Home page (Core problem, intelligence chain, CTAs)
├── product.html                   # Product overview (13 core analytical pillars)
├── how-it-works.html              # 8-stage evaluation pipeline & provenance
├── capabilities.html              # Operational vs planned capability matrix
├── use-cases.html                 # 7 domain use cases (Construction, Claims, Government, etc.)
├── validation.html                # Internal validation baseline & limitations
├── security.html                  # Enterprise security principles & data governance
├── founding-beta.html             # Application-based beta intake portal
├── about.html                     # Mission & development philosophy (PEIS Intelligence LLC)
├── contact.html                   # Professional contact channels (contact@peisintel.com)
├── privacy.html                   # Website Privacy Policy
├── terms.html                     # Website Terms of Use
├── beta-terms.html                # Founding Beta Participation Terms
├── sitemap.xml                    # Search engine sitemap
├── robots.txt                     # Crawler access rules
├── _headers                       # Cloudflare/Netlify security headers
├── netlify.toml                   # Netlify build configuration
├── vercel.json                    # Vercel deployment configuration
├── css/
│   └── styles.css                 # Enterprise design system (Navy/Steel/Teal, responsive)
├── js/
│   ├── main.js                    # Mobile nav, header elevation, tabs, accessibility
│   └── beta-form.js               # Client-side validation, JSON export & confirmation modal
├── img/
│   ├── logo.svg                   # Brand mark vector
│   ├── favicon.svg                # Browser favicon
│   ├── evaluation-chain.svg       # 8-stage evaluation chain diagram
│   └── provenance-graph.svg       # Provenance & revalidation diagram
├── docs/                          # Architecture, deployment, security & governance docs
├── tests/                         # Automated pytest test suites (HTML, links, security, isolation)
└── scripts/                       # Local development server & headless Edge screenshot tool
```

---

## 🚀 Quick Start (Local Development)

To run the website locally:

```powershell
# Option 1: Standard Python HTTP Server
python -m http.server 8000

# Option 2: Enhanced Local Dev Server with Application Logging
python scripts/serve.py
```

Then open your browser to `http://localhost:8000`.

---

## 🧪 Running Automated Tests

```powershell
# Run all automated website verification tests
pytest tests/test_website.py tests/test_security.py tests/test_isolation.py -v
```

---

## 📖 Documentation Index
* [Architecture Overview](docs/ARCHITECTURE.md)
* [Technology Stack & Rationale](docs/TECH_STACK.md)
* [Local Development Guide](docs/LOCAL_DEVELOPMENT.md)
* [Deployment Guide (Cloudflare, Netlify, S3, etc.)](docs/DEPLOYMENT_GUIDE.md)
* [Proposed Beta Application Routing Architecture](docs/BETA_ROUTING_ARCHITECTURE.md)
* [Environment Variables](docs/ENV_VARS.md)
* [Form Handling & Intake Protocols](docs/FORM_HANDLING.md)
* [Security Considerations](docs/SECURITY_CONSIDERATIONS.md)
* [Analytics Configuration](docs/ANALYTICS_CONFIGURATION.md)
* [Backup & Operational Continuity](docs/BACKUP_RECOVERY.md)
* [Founding Beta Feedback Architecture](docs/BETA_FEEDBACK_ARCHITECTURE.md)
* [Changelog](docs/CHANGELOG.md)
* [Version Info](docs/VERSION.md)
