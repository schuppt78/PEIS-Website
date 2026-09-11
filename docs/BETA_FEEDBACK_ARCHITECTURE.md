# PEIS Founding Beta — Structured Feedback Architecture & Schema

## 1. Overview
The PEIS Founding Beta Program incorporates a formal structured evaluation framework designed to capture quantitative and qualitative feedback from admitted participants upon completion of their benchmark or active project evaluation.

This document establishes the 15-point feedback schema and delivery architecture so future post-acceptance survey modules can be enabled without architectural redesign.

---

## 2. Feedback Schema (JSON Structure)

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "PEISBetaParticipantFeedback",
  "type": "object",
  "required": [
    "participant_id",
    "organization_name",
    "evaluation_use_case",
    "project_scale",
    "document_count",
    "processing_experience",
    "useful_findings",
    "provenance_accuracy_rating",
    "contradiction_utility_rating",
    "estimated_time_saved_hours",
    "overall_usefulness_score",
    "likelihood_of_reuse_score",
    "commercial_willingness_to_pay"
  ],
  "properties": {
    "participant_id": {
      "type": "string",
      "description": "Unique identifier assigned during Founding Beta admission (e.g., PEIS-BETA-2026-001)"
    },
    "organization_name": {
      "type": "string"
    },
    "evaluation_use_case": {
      "type": "string",
      "enum": [
        "Forensic Delay Claim Analysis",
        "Active Construction Management",
        "Project Controls & Float Audit",
        "Contract Notice Compliance",
        "Government Program Oversight",
        "Executive Decision Briefing",
        "Other"
      ]
    },
    "project_scale": {
      "type": "string",
      "enum": ["Under $10M", "$10M - $50M", "$50M - $150M", "$150M - $500M", "$500M+"]
    },
    "document_count": {
      "type": "integer",
      "minimum": 1
    },
    "processing_experience": {
      "type": "string",
      "enum": ["Seamless", "Minor Ingestion Friction", "Required Formatting Assistance", "Complex Ingestion"]
    },
    "useful_findings": {
      "type": "array",
      "items": { "type": "string" },
      "description": "Specific findings that provided actionable commercial or legal insight"
    },
    "incorrect_findings": {
      "type": "array",
      "items": { "type": "string" },
      "description": "Any findings flagged during human review as inaccurate or unsupported"
    },
    "missed_findings": {
      "type": "array",
      "items": { "type": "string" },
      "description": "Known project issues present in documents that the system failed to surface"
    },
    "provenance_accuracy_rating": {
      "type": "integer",
      "minimum": 1,
      "maximum": 5,
      "description": "1 (Poor citation grounding) to 5 (Flawless page/paragraph linkage)"
    },
    "contradiction_utility_rating": {
      "type": "integer",
      "minimum": 1,
      "maximum": 5,
      "description": "1 (Irrelevant conflicts) to 5 (Critical high-value discrepancies uncovered)"
    },
    "schedule_analysis_utility": {
      "type": "integer",
      "minimum": 1,
      "maximum": 5,
      "description": "Rating of CPM Schedule DNA logic and float analysis (where applicable)"
    },
    "estimated_time_saved_hours": {
      "type": "number",
      "minimum": 0,
      "description": "Estimated professional labor hours saved vs traditional manual review"
    },
    "overall_usefulness_score": {
      "type": "integer",
      "minimum": 1,
      "maximum": 10,
      "description": "1 (Not useful) to 10 (Indispensable for complex project evaluation)"
    },
    "likelihood_of_reuse_score": {
      "type": "integer",
      "minimum": 1,
      "maximum": 10,
      "description": "Net Promoter style score for future project adoption"
    },
    "commercial_willingness_to_pay": {
      "type": "string",
      "enum": [
        "Definite Commercial Interest (Per-Project Licensing)",
        "Definite Commercial Interest (Annual Enterprise Subscription)",
        "Conditional on Further Feature Expansion",
        "Not at this time"
      ]
    },
    "suggested_improvements": {
      "type": "string"
    }
  }
}
```

---

## 3. Data Collection Pipeline

1. **Intake Trigger**: Upon closing out an admitted beta evaluation run, an encrypted single-use evaluation link is dispatched to the lead participant contact.
2. **Review Session**: A 30-minute structured debrief is conducted with PEIS evaluation engineers to review findings and record structured feedback.
3. **Synthesis**: Responses are compiled into the central validation repository to drive analytical algorithm refinement and commercial feature prioritization.
