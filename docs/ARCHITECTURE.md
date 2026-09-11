# PEIS Website Architecture & Information Design

## 1. System Philosophy
The Phase 1 PEIS public website is engineered as an **ultra-lightweight, zero-runtime-dependency static architecture**. This guarantees:
- Maximum page load speed (sub-100ms global TTFB on edge CDNs);
- Near-zero security attack surface (no runtime database, no unauthenticated compute containers);
- 100% decoupling from the frozen core PEIS analytical engine;
- Lowest possible operational cost ($0.00/mo on global edge networks).

---

## 2. Directory Layout & Roles

| Directory / File | Description | Purpose |
| :--- | :--- | :--- |
| `index.html` | Home Page | Primary brand introduction, core problem statement, 8-stage chain diagram, CTAs |
| `product.html` | Product Page | Detailed breakdown of the 13 functional pillars |
| `how-it-works.html` | Evaluation Chain | Visual walkthrough of the 8-stage evaluation pipeline & provenance |
| `capabilities.html` | Capability Matrix | Granular operational vs planned capabilities |
| `use-cases.html` | Domain Use Cases | 7 high-stakes industry applications (Construction, Claims, Govt, etc.) |
| `validation.html` | Validation Status | Authoritative internal regression baseline status, internal testing vs external review |
| `security.html` | Security Principles | Enterprise data integrity, RBAC, provenance, and configuration control |
| `founding-beta.html` | Beta Intake Portal | Application-based cohort intake form with client-side validation |
| `about.html` | About Page | Mission, development ethos, and engineering principles |
| `contact.html` | Contact Page | Professional inquiry routing and contact mechanisms |
| `privacy.html` | Privacy Policy | Draft privacy policy for legal review |
| `terms.html` | Terms of Use | Draft terms of website use for legal review |
| `beta-terms.html` | Beta Agreement | Draft Founding Beta participation terms for legal review |
| `css/styles.css` | Design System | Enterprise palette, responsive layout, accessible focus rings, dark accents |
| `js/main.js` | Interaction Engine | Accessible mobile navigation, scroll elevation, keyboard trapping |
| `js/beta-form.js` | Application Handler | Input validation, unique reference generation, JSON receipt export |
| `img/` | Vector Assets | Brand SVG logos, favicons, and architectural diagrams |
| `docs/` | Operational Docs | Complete architectural, deployment, security, and governance guides |
| `tests/` | Test Suites | Automated pytest verification of HTML, links, security, and PEIS isolation |
| `scripts/` | Tooling | Local development server with submission logging & headless Edge screenshot tool |

---

## 3. Information Architecture Flow

```
[ Visitor Landing (index.html) ]
        │
        ├──► [ Explore Capabilities (product.html / capabilities.html) ]
        │         └──► [ Evaluation Methodology (how-it-works.html) ]
        │                   └──► [ Industry Applications (use-cases.html) ]
        │
        ├──► [ Review Integrity (validation.html / security.html) ]
        │
        └──► [ Primary Conversion: Founding Beta Application (founding-beta.html) ]
                  │
                  ▼
         [ Client-Side Validation ]
                  │
                  ▼
         [ Unique Ref ID Generated ]
                  │
                  ├──► [ Confirmation Modal Display ]
                  ├──► [ Download Structured Application Receipt (.JSON) ]
                  └──► [ Optional Local/API Logger Post ]
```
