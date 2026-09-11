# Security Review & Considerations

## 1. Public Website Security Architecture
The Phase 1 PEIS public website has been designed in strict accordance with the security directives:

1. **Complete Decoupling from PEIS Core**:
   - The website repository contains zero proprietary analytical algorithms, database credentials, or imports from `PEIS v0.1`.
   - The core frozen validation candidate is completely unexposed to public web traffic.

2. **Reduced Presentation-Tier Attack Surface**:
   - Because the public website tier serves static assets, common web application database injection vectors (such as SQL injection) and dynamic server-side template execution vulnerabilities are eliminated on this tier.
   - The presentation layer does not connect directly to the PEIS backend or analytical databases.

3. **HTTP Security Headers**:
   - The included `_headers`, `netlify.toml`, and `vercel.json` enforce:
     - `Content-Security-Policy`: Restricts resource execution to trusted local origins.
     - `X-Frame-Options: DENY`: Prevents clickjacking attacks.
     - `X-Content-Type-Options: nosniff`: Prevents MIME-type sniffing exploits.
     - `Referrer-Policy: strict-origin-when-cross-origin`: Protects referrer data.
     - `Permissions-Policy`: Disables camera, microphone, geolocation, and payment APIs.

4. **Public Form Data Minimization**:
   - The Founding Beta intake form explicitly forbids the submission of passwords, credentials, classified documents, CUI, PHI, or proprietary project records.
   - Client-side validation prevents accidental empty or malformed submissions.

5. **Automated Security Verification**:
   - The automated test suite (`tests/test_security.py`) audits the entire website directory to guarantee zero hardcoded API keys, secrets, or internal paths exist.
