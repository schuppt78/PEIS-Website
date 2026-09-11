# Founding Beta Form Handling & Intake Workflow

## 1. Intake Philosophy
The Phase 1 Founding Beta intake is **application-based and strictly manual**.

There is:
- **No automated account creation**;
- **No public project document upload portal**;
- **No unreviewed access to PEIS systems**.

---

## 2. Client-Side Submission Workflow

```
[ User Completes Form on founding-beta.html ]
                    │
                    ▼
       [ HTML5 & JS Form Validation ]
  (Checks required fields, email format, capabilities)
                    │
                    ▼
     [ Generate Unique Reference ID ]
    (e.g., PEIS-BETA-LM8XYZ-9A4B)
                    │
                    ▼
     [ Populate Structured JSON Object ]
                    │
       ┌────────────┴────────────┐
       ▼                         ▼
[ Render Confirmation Modal ]  [ Attempt /api/beta-apply Post ]
       │                                  │
       ├──► [ User Downloads Receipt .JSON ] └──► (Logged locally if dev server is running)
       └──► [ User Copies Structured Record ]
```

---

## 3. Production Form Routing Options (Pending Owner Authorization)

In accordance with Owner Review Corrective Directive 001, the proposed production routing architecture has been created and documented in:
* [`docs/BETA_ROUTING_ARCHITECTURE.md`](BETA_ROUTING_ARCHITECTURE.md)
* [`functions/api/beta-apply.js`](../functions/api/beta-apply.js)

### Routing Summary:
1. **Cloudflare Pages Function (`/api/beta-apply`)**:
   - Executes server-side input validation and anti-spam verification (Cloudflare Turnstile);
   - Rejects any attempted file attachments or sensitive credentials;
   - Generates an authoritative reference code (`PEIS-BETA-XXXX-YYYY`);
   - Persists application metadata to encrypted Cloudflare D1 SQL store;
   - Dispatches an encrypted webhook notification to the Owner's management channel;
   - Returns a structured confirmation JSON payload to the client.
2. **Zero Deployment Gate**: This serverless function will remain dormant until explicit Owner authorization and environment binding setup.
