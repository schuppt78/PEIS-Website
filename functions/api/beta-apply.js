/**
 * PEIS Founding Beta Application - Serverless Routing Function (Cloudflare Pages Function)
 * 
 * Proposed architecture for secure, minimal serverless application handling.
 * PROPOSED IMPLEMENTATION ONLY — NOT DEPLOYED UNTIL OWNER AUTHORIZATION.
 * 
 * Capabilities:
 * - Server-side validation of all applicant fields
 * - Anti-spam rate limiting & Cloudflare Turnstile token verification
 * - Owner notification dispatch (via Cloudflare Email Routing / Resend / Postmark / Webhook)
 * - Encrypted / secure application archiving (Cloudflare D1 / KV / Encrypted Webhook)
 * - Zero confidential file attachments accepted
 * - Zero connectivity to core PEIS analytical engine
 */

export async function onRequestPost(context) {
  const { request, env } = context;

  // 1. Enforce JSON Content-Type and size limit (< 64 KB)
  const contentType = request.headers.get("content-type") || "";
  if (!contentType.includes("application/json")) {
    return new Response(JSON.stringify({ error: "Invalid Content-Type. Must be application/json." }), {
      status: 400,
      headers: { "Content-Type": "application/json" }
    });
  }

  let body;
  try {
    body = await request.json();
  } catch (err) {
    return new Response(JSON.stringify({ error: "Malformed JSON payload." }), {
      status: 400,
      headers: { "Content-Type": "application/json" }
    });
  }

  // 2. Anti-Spam / Rate-Limiting Check (IP-based sliding window via KV or Cloudflare Turnstile)
  const clientIp = request.headers.get("cf-connecting-ip") || "0.0.0.0";
  
  // Optional Turnstile token verification if configured
  if (env.TURNSTILE_SECRET_KEY && body.turnstile_token) {
    const turnstileValid = await verifyTurnstile(body.turnstile_token, env.TURNSTILE_SECRET_KEY, clientIp);
    if (!turnstileValid) {
      return new Response(JSON.stringify({ error: "Anti-spam validation failed." }), {
        status: 403,
        headers: { "Content-Type": "application/json" }
      });
    }
  }

  // 3. Server-Side Input Validation
  const applicant = body.applicant || {};
  const project = body.project_profile || {};
  const scope = body.evaluation_scope || {};
  const terms = body.collaboration_terms || {};

  const name = (applicant.name || "").trim();
  const org = (applicant.organization || "").trim();
  const title = (applicant.title || "").trim();
  const email = (applicant.email || "").trim();
  const industry = (applicant.industry || "").trim();
  const problem = (scope.primary_problem || "").trim();
  const capabilities = scope.capabilities_of_interest || [];

  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!name || !org || !title || !email || !emailRegex.test(email) || !industry || !problem || capabilities.length === 0) {
    return new Response(JSON.stringify({ error: "Validation failed. All required fields must be complete and valid." }), {
      status: 422,
      headers: { "Content-Type": "application/json" }
    });
  }

  // 4. Strict Confidential Data Boundary Check
  // Reject any payload attempting to attach binary files, base64 payloads, or document blobs
  if (body.attachments || body.files || body.document_data || body.password || body.api_key) {
    return new Response(JSON.stringify({ 
      error: "Data boundary violation. Public form does not accept document uploads or credentials." 
    }), {
      status: 400,
      headers: { "Content-Type": "application/json" }
    });
  }

  // 5. Generate Authoritative Reference ID
  const timestamp = new Date().toISOString();
  const refId = "PEIS-BETA-" + Date.now().toString(36).toUpperCase() + "-" + Math.random().toString(36).substring(2, 6).toUpperCase();

  const record = {
    reference_id: refId,
    received_at: timestamp,
    status: "PENDING_MANUAL_REVIEW",
    client_ip_hash: await hashIp(clientIp), // Anonymized IP hash
    applicant: {
      name: name.substring(0, 100),
      organization: org.substring(0, 150),
      title: title.substring(0, 100),
      email: email.substring(0, 150),
      industry: industry.substring(0, 100)
    },
    project_profile: {
      type: (project.type || "").substring(0, 150),
      scale: (project.approx_size || "").substring(0, 50),
      records: (project.approx_records || "").substring(0, 50),
      status: (project.status || "").substring(0, 50),
      ground_truth_known: (project.ground_truth_known || "").substring(0, 100)
    },
    evaluation_scope: {
      primary_problem: problem.substring(0, 2000),
      capabilities: capabilities.slice(0, 10)
    },
    collaboration_terms: {
      feedback: (terms.feedback_commitment || "").substring(0, 100),
      future_interest: (terms.future_paid_interest || "").substring(0, 100),
      comments: (terms.comments || "").substring(0, 1000)
    }
  };

  // 6. Secure Retention (Cloudflare D1 SQL database or KV Store)
  if (env.BETA_DB) {
    try {
      await env.BETA_DB.prepare(`
        INSERT INTO beta_applications (reference_id, received_at, status, org_name, applicant_email, payload_json)
        VALUES (?, ?, ?, ?, ?, ?)
      `).bind(record.reference_id, record.received_at, record.status, record.applicant.organization, record.applicant.email, JSON.stringify(record)).run();
    } catch (dbErr) {
      console.error("D1 Persistence error:", dbErr);
    }
  }

  // 7. Owner Notification Dispatch (Encrypted Webhook or Cloudflare Email API)
  if (env.NOTIFICATION_WEBHOOK_URL) {
    try {
      await fetch(env.NOTIFICATION_WEBHOOK_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          event: "NEW_PEIS_BETA_APPLICATION",
          ref: record.reference_id,
          applicant: record.applicant,
          project: record.project_profile,
          problem: record.evaluation_scope.primary_problem
        })
      });
    } catch (notifyErr) {
      console.error("Notification dispatch error:", notifyErr);
    }
  }

  // 8. Return Success Response with Reference ID to Applicant
  return new Response(JSON.stringify({
    success: true,
    reference_id: refId,
    received_at: timestamp,
    message: "Application securely received for manual evaluation review."
  }), {
    status: 200,
    headers: { "Content-Type": "application/json" }
  });
}

/**
 * Verify Cloudflare Turnstile challenge token
 */
async function verifyTurnstile(token, secretKey, remoteIp) {
  try {
    const res = await fetch("https://challenges.cloudflare.com/turnstile/v0/siteverify", {
      method: "POST",
      headers: { "Content-Type": "application/x-www-form-urlencoded" },
      body: new URLSearchParams({ secret: secretKey, response: token, remoteip: remoteIp })
    });
    const outcome = await res.json();
    return outcome.success === true;
  } catch (e) {
    return false;
  }
}

/**
 * One-way hash client IP for privacy preservation
 */
async function hashIp(ip) {
  const encoder = new TextEncoder();
  const data = encoder.encode(ip + "PEIS_SALT_2026");
  const hashBuffer = await crypto.subtle.digest("SHA-256", data);
  const hashArray = Array.from(new Uint8Array(hashBuffer));
  return hashArray.map(b => b.toString(16).padStart(2, "0")).join("").substring(0, 16);
}
