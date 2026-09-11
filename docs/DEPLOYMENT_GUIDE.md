## 1. Overview & Cost Distinction
The PEIS Phase 1 public website is built as a static web property (HTML5, CSS3, Vanilla JS, SVG).

### Important Cost Distinction:
* **$0 Static Hosting Capability**: Distributes static HTML/CSS/JS assets globally on free-tier edge networks (Cloudflare Pages, GitHub Pages) without mandatory monthly hosting charges for static file delivery.
* **Total Operating Costs**: Operating a complete commercial web presence incurs separate discretionary or operational expenses:
  1. **Domain Registration**: Custom apex domain registration (`.ai`, `.com`, `.org`) typically costs **~$10.00 – $65.00 / year** depending on registry pricing.
  2. **Business Email Services**: Secure email hosting (e.g. Google Workspace, Microsoft 365, or Cloudflare Email Routing with private inbox) typically costs **$0.00** (forwarding) to **~$6.00 – $18.00 / user / month**.
  3. **Application Intake Routing**: Serverless notification delivery (e.g. Cloudflare Worker + Resend/Postmark webhook) operates within free tiers or incurs low per-thousand email costs.
  4. **Future PEIS SaaS Backend**: Hosting the actual PEIS analytical engine, database, and multi-tenant infrastructure in Phase 2+ will require dedicated cloud compute and will be budgeted separately under commercial authorization.

---

## 2. Deployment Options Comparison

### Option 1: Cloudflare Pages (Recommended Serverless Edge Option)
* **Static Hosting Cost**: **$0.00 / month** (Free tier includes global anycast CDN, automated TLS certificate renewal, DDoS mitigation, and 500 builds/month).
* **Setup**:
  1. Link repository to Cloudflare Pages.
  2. Build command: *(none)*; Output directory: `.`.
  3. Deploy. Security headers in `_headers` are applied automatically.
* **Advantages**:
  - Global edge CDN with low latency across worldwide points of presence.
  - Built-in edge DDoS mitigation and Web Application Firewall (WAF) controls.
  - Native integration with Cloudflare Functions (`functions/api/beta-apply.js`) for server-side form validation and routing without separate backend servers.
  - Zero local web server maintenance or operating system patching.
* **Disadvantages**:
  - Requires creating and administering a Cloudflare account.
* **Security & Architecture**:
  - Pure static asset delivery eliminates dynamic database queries and server-side script execution on the web presentation tier.

---

### Option 2: GitHub Pages
* **Static Hosting Cost**: **$0.00 / month**.
* **Setup**:
  1. Push website repository to GitHub.
  2. Navigate to Repository Settings → Pages → Source: Deploy from branch (`main` / `root`).
* **Advantages**:
  - Zero additional accounts required if already using GitHub.
  - Automatic deployment upon Git push.
* **Disadvantages**:
  - Less granular control over custom security headers compared to Cloudflare `_headers`.
  - Bandwidth usage guidelines apply.
* **Security & Architecture**:
  - Managed static hosting infrastructure suitable for public informational portals.

---

### Option 3: Netlify / Vercel
* **Static Hosting Cost**: **$0.00 / month** (Starter tier includes 100GB monthly bandwidth and automated TLS).
* **Setup**:
  - Connect repository; `netlify.toml` and `vercel.json` are pre-configured.
* **Advantages**:
  - Automated preview builds on pull requests.
* **Disadvantages**:
  - Commercial rate cards apply if bandwidth exceeds tier limits.
* **Security & Architecture**:
  - Global edge routing with automated TLS.

---

### Option 4: AWS S3 + CloudFront (Enterprise Cloud Storage & CDN)
* **Estimated Cost**: **~$1.00 – $3.00 / month** (AWS Free Tier covers initial 1TB CloudFront transfer; S3 storage < $0.05/mo).
* **Annual Cost**: **~$12.00 – $36.00 / year**.
* **Setup**:
  1. Create private S3 bucket and upload static files.
  2. Create CloudFront distribution with Origin Access Control (OAC).
  3. Attach AWS Certificate Manager (ACM) SSL certificate and Route 53 DNS.
* **Advantages**:
  - Can be provisioned inside an organization's existing AWS enterprise account.
  - Granular IAM access policies and KMS encryption configurations.
* **Disadvantages**:
  - Requires AWS console management and ongoing cloud account billing.
  - Note: Using AWS does not automatically convey FedRAMP authorization or government certification to PEIS; compliance authorizations apply to underlying cloud services, while the application itself requires separate authorization.
* **Security & Architecture**:
  - Highly configurable cloud infrastructure with origin access restrictions.

---

## 3. Publication Pre-Requisites (Owner Authorization Gate)

Before deploying to any public URL:
1. Confirmed official domain name: `peisintel.com`.
2. Confirm corporate entity registration and business email address for legal disclosures.
3. Review and execute formal legal review on `privacy.html`, `terms.html`, and `beta-terms.html`.
4. Configure domain DNS records (CNAME / ALIAS) for `peisintel.com` pointing to chosen edge provider.
