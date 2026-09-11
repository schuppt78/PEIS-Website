## [1.0.4-pub-release-hardened] - 2026-09-11
### Public Release Hardening & Corporate Identity Alignment (Directive PEIS-WEB-PRH-002)
- **Corporate Entity Alignment**: Established `PEIS Intelligence LLC` clearly as the legal and business entity developing the `Project Evaluation Intelligence System (PEIS)`.
- **Copyright Attribution Update**: Sitewide update of legal attribution across all 14 pages to `© 2026 PEIS Intelligence LLC. All rights reserved.`.
- **Privacy Policy Hardening**: Removed all pre-release "Draft", "Placeholder", and internal review warning banners from `privacy.html`. Accurately documented data handling practices, zero confidential data ingestion on public forms, and user rights via `contact@peisintel.com`.
- **Terms & Beta Terms Hardening**: Removed draft banners and placeholder labels from `terms.html` and `beta-terms.html`. Codified intellectual property ownership under PEIS Intelligence LLC, professional advice disclaimers, and bilateral NDA requirements.
- **Footer Navigation Normalization**: Cleaned all 14 footer navigation blocks, removing `(Draft)` parentheticals from `Privacy Policy`, `Terms of Use`, and `Beta Program Terms`.
- **Strict Scope Isolation**: Verified absolute product scope separation with zero references to unrelated company applications or external product roadmaps, and zero modifications to core analytical repositories.
- **Sitemap & SEO Synchronization**: Updated `sitemap.xml` timestamps to 2026-09-11 across all 13 canonical HTTPS endpoints.

## [1.0.3-pub-readiness] - 2026-09-07
### Publication Readiness Administrative Corrections
- **Public Email Address Normalization**: Standardized all public-facing contact channels and policy references to the established public company address `contact@peisintel.com`. Functional aliases (`beta@`, `inquiries@`, `privacy@`, `support@`) are suppressed from public UI until confirmed provisioned by the Owner.

## [1.0.2-phase1-rev2] - 2026-09-07
### Official Domain Configuration
- **Designated Official Domain**: Updated canonical URLs, sitemap, robots.txt, and metadata across all 13 pages to `https://peisintel.com/`.

## [1.0.1-phase1-rev1] - 2026-09-04
### Corrective Directive 001 Actions
- **Infrastructure Claims Hardening**: Removed all claims regarding "immunity to server-side exploits" and "Federal Grade" certifications, substituting precise technical descriptions.
- **Cost Clarification**: Explicitly distinguished "$0 static hosting capability" from total operating costs (domain registration, email hosting, notifications, future SaaS hosting).
- **Validation Language Alignment**: Refined `validation.html` to clearly state that internal testing is complete, independent external validation has not yet occurred, and the Founding Beta is intended to gather real-world performance evidence.
- **Domain/Email Placeholder Labeling**: Explicitly marked `beta@peis.ai`, `inquiries@peis.ai`, and `contact@peis.ai` as deployment placeholders pending Owner domain setup.
- **Strict Data Boundary Fortification**: Enhanced `founding-beta.html` and `beta-form.js` to forbid submission of project documents, confidential records, proprietary customer info, CUI, classified info, PHI, credentials, passwords, or API keys, specifying separate controlled onboarding.
- **Proposed Serverless Routing Architecture**: Designed `functions/api/beta-apply.js` and `docs/BETA_ROUTING_ARCHITECTURE.md` for Cloudflare Pages Functions with server-side validation, anti-spam, and $0 cost routing.

## [1.0.0-phase1] - 2026-09-04
### Added
- **Initial Public Website Release**: Phase 1 static web property for Project Evaluation Intelligence System (PEIS).
- **Core Informational Pages**:
  - `index.html`: Professional overview, core problem statement, 8-stage evaluation chain, metric highlights.
  - `product.html`: Comprehensive explanation of the 13 core functional pillars.
  - `how-it-works.html`: Detailed 8-stage evaluation pipeline breakdown and dependency-aware revalidation model.
  - `capabilities.html`: Granular capability matrix with operational vs planned status indicators.
  - `use-cases.html`: 7 in-depth capital project industry use cases.
  - `validation.html`: Transparent reporting of internal master regression status, internal vs external validation boundaries, and documented limitations.
  - `security.html`: High-level enterprise security principles, cryptographic provenance, and configuration governance.
  - `founding-beta.html`: Structured application intake portal with client-side validation, unique reference ID generation, and structured JSON receipt download.
  - `about.html`: Mission, engineering philosophy, and development trajectory.
  - `contact.html`: Professional contact channels and general inquiry routing.
- **Legal Draft Placeholders**:
  - `privacy.html`: Draft Website Privacy Policy (Marked: *REQUIRES OWNER / LEGAL COUNSEL REVIEW*).
  - `terms.html`: Draft Website Terms of Use (Marked: *REQUIRES OWNER / LEGAL COUNSEL REVIEW*).
  - `beta-terms.html`: Draft Founding Beta Participation Terms (Marked: *REQUIRES OWNER / LEGAL COUNSEL REVIEW*).
- **Design System & Vector Assets**:
  - `css/styles.css`: Enterprise Navy/Steel/Teal responsive design system with accessible focus states.
  - `img/logo.svg`, `img/favicon.svg`: Brand vector marks.
  - `img/evaluation-chain.svg`: Visual 8-stage evaluation chain diagram.
  - `img/provenance-graph.svg`: Visual provenance and revalidation graph.
- **Client Scripts**:
  - `js/main.js`: Accessible mobile navigation and scroll interactions.
  - `js/beta-form.js`: Beta application intake validation and JSON receipt generator.
- **Technical & SEO Assets**:
  - `sitemap.xml`, `robots.txt`, `_headers`, `netlify.toml`, `vercel.json`.
- **Automated Test Suites**:
  - `tests/test_website.py`: Full HTML and internal link validation suite.
  - `tests/test_security.py`: Security and secret leakage audit.
  - `tests/test_isolation.py`: PEIS v0.1 read-only isolation verification.
- **Local Tooling**:
  - `scripts/serve.py`: Lightweight development server with intake logging.
  - `scripts/capture_screenshots.py`: Automated headless browser screenshot generator.
