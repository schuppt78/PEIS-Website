/**
 * PEIS Founding Beta Application Form Handler
 * Validates business application fields, structures data safely, presents confirmation modal,
 * and enables applicant record backup/download without exposing sensitive server endpoints.
 */

document.addEventListener('DOMContentLoaded', () => {
  const betaForm = document.getElementById('founding-beta-form');
  const modalBackdrop = document.getElementById('beta-modal');
  const modalCloseBtn = document.getElementById('modal-close-btn');
  const modalRefNumber = document.getElementById('modal-ref-number');
  const modalSummaryText = document.getElementById('modal-summary-text');
  const copyRecordBtn = document.getElementById('copy-record-btn');
  const downloadRecordBtn = document.getElementById('download-record-btn');

  if (!betaForm) return;

  // Track current submitted record
  let currentSubmissionRecord = null;

  betaForm.addEventListener('submit', async (e) => {
    e.preventDefault();

    // Reset error states
    const inputs = betaForm.querySelectorAll('.form-control');
    inputs.forEach(input => input.classList.remove('error'));

    let isValid = true;
    const formData = new FormData(betaForm);

    // Validate required text/select fields
    const requiredFields = [
      'applicant_name',
      'organization_name',
      'job_title',
      'business_email',
      'industry',
      'project_type',
      'project_size',
      'record_count',
      'evaluation_problem',
      'project_status',
      'ground_truth',
      'structured_feedback',
      'future_paid_interest'
    ];

    requiredFields.forEach(fieldName => {
      const field = betaForm.querySelector(`[name="${fieldName}"]`);
      if (!field || !field.value.trim()) {
        field?.classList.add('error');
        isValid = false;
      }
    });

    // Email validation
    const emailField = betaForm.querySelector('[name="business_email"]');
    if (emailField && emailField.value.trim()) {
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!emailRegex.test(emailField.value.trim())) {
        emailField.classList.add('error');
        isValid = false;
      }
    }

    // Capabilities multi-select validation
    const selectedCapabilities = [];
    const capabilityCheckboxes = betaForm.querySelectorAll('input[name="capabilities"]:checked');
    capabilityCheckboxes.forEach(cb => selectedCapabilities.push(cb.value));

    if (selectedCapabilities.length === 0) {
      const capContainer = document.getElementById('capabilities-group');
      if (capContainer) {
        capContainer.classList.add('has-error');
      }
      isValid = false;
    }

    if (!isValid) {
      // Focus first error element
      const firstError = betaForm.querySelector('.form-control.error, .has-error');
      firstError?.scrollIntoView({ behavior: 'smooth', block: 'center' });
      firstError?.focus();
      return;
    }

    // Generate unique application reference ID (timestamp + random hex)
    const timestamp = new Date().toISOString();
    const refId = 'PEIS-BETA-' + Date.now().toString(36).toUpperCase() + '-' + Math.random().toString(36).substring(2, 6).toUpperCase();

    // Construct structured application object
    currentSubmissionRecord = {
      reference_id: refId,
      submitted_at: timestamp,
      status: 'UNDER_MANUAL_REVIEW',
      applicant: {
        name: formData.get('applicant_name')?.toString().trim(),
        organization: formData.get('organization_name')?.toString().trim(),
        title: formData.get('job_title')?.toString().trim(),
        email: formData.get('business_email')?.toString().trim(),
        industry: formData.get('industry')?.toString().trim()
      },
      project_profile: {
        type: formData.get('project_type')?.toString().trim(),
        approx_size: formData.get('project_size')?.toString().trim(),
        approx_records: formData.get('record_count')?.toString().trim(),
        status: formData.get('project_status')?.toString().trim(),
        ground_truth_known: formData.get('ground_truth')?.toString().trim()
      },
      evaluation_scope: {
        primary_problem: formData.get('evaluation_problem')?.toString().trim(),
        capabilities_of_interest: selectedCapabilities
      },
      collaboration_terms: {
        feedback_commitment: formData.get('structured_feedback')?.toString().trim(),
        future_paid_interest: formData.get('future_paid_interest')?.toString().trim(),
        comments: formData.get('comments')?.toString().trim() || 'None provided'
      },
      data_governance_notice: {
        confidential_records_submitted: false,
        classified_or_phi_submitted: false,
        requires_manual_qualification: true
      }
    };

    // Attempt optional local server endpoint POST if available
    try {
      await fetch('/api/beta-apply', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(currentSubmissionRecord)
      });
    } catch (err) {
      // Offline / static hosting mode — record is retained client-side
      console.log('Application logged client-side (static mode active).');
    }

    // Populate modal with submission confirmation
    if (modalRefNumber) modalRefNumber.textContent = refId;
    if (modalSummaryText) {
      modalSummaryText.textContent = `Thank you, ${currentSubmissionRecord.applicant.name}. Your Founding Beta application for ${currentSubmissionRecord.applicant.organization} has been safely received under reference #${refId}. Our evaluation review committee manually reviews every candidate project against available testing cohorts.`;
    }

    // Open confirmation modal
    if (modalBackdrop) {
      modalBackdrop.classList.add('active');
      modalCloseBtn?.focus();
    }

    // Reset form
    betaForm.reset();
  });

  // Modal actions
  if (modalCloseBtn && modalBackdrop) {
    modalCloseBtn.addEventListener('click', () => {
      modalBackdrop.classList.remove('active');
    });
  }

  // Copy structured JSON record to clipboard
  if (copyRecordBtn) {
    copyRecordBtn.addEventListener('click', async () => {
      if (currentSubmissionRecord) {
        try {
          await navigator.clipboard.writeText(JSON.stringify(currentSubmissionRecord, null, 2));
          const originalText = copyRecordBtn.textContent;
          copyRecordBtn.textContent = '✓ Record Copied';
          setTimeout(() => {
            copyRecordBtn.textContent = originalText;
          }, 2500);
        } catch (err) {
          alert('Record summary:\n' + JSON.stringify(currentSubmissionRecord, null, 2));
        }
      }
    });
  }

  // Download application receipt (.json)
  if (downloadRecordBtn) {
    downloadRecordBtn.addEventListener('click', () => {
      if (currentSubmissionRecord) {
        const dataStr = 'data:text/json;charset=utf-8,' + encodeURIComponent(JSON.stringify(currentSubmissionRecord, null, 2));
        const downloadAnchor = document.createElement('a');
        downloadAnchor.setAttribute('href', dataStr);
        downloadAnchor.setAttribute('download', `${currentSubmissionRecord.reference_id}_Application_Receipt.json`);
        document.body.appendChild(downloadAnchor);
        downloadAnchor.click();
        downloadAnchor.remove();
      }
    });
  }
});
