# Privacy-Conscious Analytics Configuration

## 1. Analytics Philosophy
In alignment with the Phase 1 build directive:
- **No invasive advertising trackers** (No Facebook Pixel, No LinkedIn Insight Tag, No Google Ads conversion trackers).
- **No personally identifiable tracking** (No cross-site tracking, fingerprinting, or session recording).
- **Privacy-first metrics**: Page views, referrers, device categories (Desktop/Mobile), and general country-level geographic aggregation without cookies.

---

## 2. Recommended Zero-Cookie Privacy Analytics Options

### Option A: Cloudflare Web Analytics (Recommended — 100% Free & Cookieless)
- **Cost**: $0.00 / month.
- **Features**: Measures web performance and visitor counts without using cookies or collecting personal data. Fully GDPR, CCPA, and PECR compliant out-of-the-box.
- **Implementation**: Enable with a single toggle in the Cloudflare Pages dashboard.

### Option B: Plausible Analytics / Fathom Analytics (Self-Hosted or SaaS)
- **Cost**: $0 (if self-hosted) or ~$9/mo (hosted).
- **Features**: Lightweight (< 1 KB script), open source, fully privacy-focused.

---

## 3. Current Phase 1 Status
In Phase 1 development, **no external analytics scripts are embedded**. The site is ready for plug-and-play insertion of cookieless analytics upon Owner approval.
