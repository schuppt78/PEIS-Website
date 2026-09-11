# Technology Stack & Rationale

## 1. Core Stack Selection

| Layer | Technology | Version / Standard | Rationale |
| :--- | :--- | :--- | :--- |
| **Markup** | Semantic HTML5 | W3C Standard | Universal compatibility, zero build-step overhead, perfect SEO discoverability, native accessibility. |
| **Styling** | Custom CSS3 System | CSS Variables & Grid | High-performance, zero stylesheet bloat, bespoke enterprise palette, dark/light contrast compliance (WCAG AA). |
| **Scripting** | Vanilla JavaScript | ECMAScript 2022+ | Zero framework dependencies (no React/Vue churn), sub-millisecond execution, accessible DOM event listeners. |
| **Vector Graphics** | Scalable Vector Graphics | SVG 1.1 | Sharp rendering on all DPIs, ultra-small asset footprints (3-12 KB), no raster pixelation. |
| **Dev Server** | Python HTTP & FastAPI | Python 3.11+ | Native environment availability, lightweight local testing, integrated intake logger. |
| **Testing** | Pytest & Python Standard Lib | Pytest 8.0+ | Automated link checking, semantic structure assertions, zero-leakage security auditing, and PEIS isolation testing. |
| **Automation** | Microsoft Edge Headless | Chromium Engine | Native OS browser automation for deterministic screenshot capture across mobile and desktop viewports. |

---

## 2. Why No Heavy JavaScript Frameworks (e.g. React/Next.js/Angular)?

1. **Zero Vulnerability Attack Surface**: Heavy NPM dependency trees introduce hundreds of transitive dependencies, frequent CVE patch cycles, and complex build toolchains.
2. **Instant Global Edge Deployment**: Pure static HTML/CSS/JS can be deployed to any CDN worldwide without container orchestrators, serverless cold starts, or Node.js runtime servers.
3. **Absolute Long-Term Stability**: Pure standards-compliant HTML5 will render identically in 10 years without requiring npm upgrades or breaking webpack plugins.
4. **Decoupling from Core Product**: Ensures the marketing and recruitment website never creates accidental module bindings or import paths to `PEIS v0.1`.
