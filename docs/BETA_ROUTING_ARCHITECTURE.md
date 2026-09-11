# Proposed Founding Beta Application Routing Architecture

> [!NOTE]
> **PROPOSED ARCHITECTURE ONLY — NOT YET DEPLOYED**
> In accordance with Owner Review Corrective Directive 001, this architecture is documented for Owner review and authorization prior to deployment.

---

## 1. Architectural Objectives
1. **Zero Exposure to PEIS Core**: Operates completely within an isolated serverless edge environment (Cloudflare Pages Functions). No database connection, API call, or network route connects to `PEIS v0.1`.
2. **Server-Side Verification**: Validates all business fields independently of client-side JavaScript.
3. **Spam & Abuse Protection**: Cloudflare Turnstile token verification + edge IP rate-limiting.
4. **Owner Notification**: Dispatches immediate notification via secure webhook or private email API upon valid submission.
5. **Secure, Minimal Retention**: Stores structured application metadata in an encrypted serverless store (Cloudflare D1 SQL) with strict field length limits and zero confidential project documents.
6. **$0.00 / Free-Tier Alignment**: Operates completely within Cloudflare Pages Functions free-tier limits (100,000 requests/day).

---

## 2. End-to-End Data Flow

```
[ Applicant Browser (founding-beta.html) ]
                   │
                   ▼  (1) POST /api/beta-apply (JSON < 64KB + Turnstile Token)
   [ Cloudflare Edge / Pages Function (functions/api/beta-apply.js) ]
                   │
                   ├──► (2) Rate Limiting & Turnstile Siteverify Check
                   │
                   ├──► (3) Server-Side Schema & Email Format Validation
                   │
                   ├──► (4) Strict Data Boundary Inspection (Rejects any binary blobs / credentials)
                   │
                   ├──► (5) Generate Cryptographic Reference Code (PEIS-BETA-XXXX-YYYY)
                   │
                   ├──► (6) Write Record to Cloudflare D1 Store (Encrypted at rest)
                   │
                   ├──► (7) Dispatch Webhook / Notification to Owner (Encrypted payload)
                   │
                   ▼
[ Return 200 OK with Reference Code ]
                   │
                   ▼
[ Applicant Screen Displays Confirmation Modal + JSON Download Option ]
```

---

## 3. Security Controls & Data Boundaries

| Control Layer | Implementation Mechanism |
| :--- | :--- |
| **Transport Encryption** | TLS 1.3 enforced by Cloudflare Edge with HSTS. |
| **Payload Restrictions** | Enforces JSON `Content-Type`, max size 64 KB, rejecting multi-part form file uploads. |
| **Data Boundary Enforcement** | Code automatically drops/errors if incoming payload contains `attachments`, `files`, `password`, or `api_key`. |
| **Spam Mitigation** | Cloudflare Turnstile CAPTCHA-less verification + IP rate-limiting window. |
| **PII Minimization** | Retains only applicant name, business email, organization, title, and high-level project metadata. Client IP is hashed with SHA-256 salt for privacy. |
| **Isolation Guarantee** | Cloudflare Function executes in an isolated V8 isolate sandbox with zero network ingress to internal PEIS repositories. |

---

## 4. Cost Breakdown for Proposed Routing

| Component | Provider / Service | Free Tier Limit | Estimated Monthly Cost |
| :--- | :--- | :--- | :--- |
| **Serverless Compute** | Cloudflare Pages Functions | 100,000 invocations / day | **$0.00** |
| **Anti-Spam Verification** | Cloudflare Turnstile | Unlimited verifications | **$0.00** |
| **Database Storage** | Cloudflare D1 (SQL) | 5M read / 100k write rows / day | **$0.00** |
| **Owner Notification Webhook** | Encrypted Discord / Slack / Teams Webhook | Unlimited | **$0.00** |
| **Owner Email Notification** | Cloudflare Email Routing / Resend | Free tier (3,000 emails/mo) | **$0.00** |
| **Total Routing Cost** | — | — | **$0.00 / month** |
