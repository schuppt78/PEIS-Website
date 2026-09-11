"""
PEIS Public Website - Structural & Integrity Test Suite
Verifies HTML structure, link validity, form completeness, SEO metadata, and legal disclaimers.
"""

import os
import re
from pathlib import Path
from html.parser import HTMLParser

BASE_DIR = Path(__file__).resolve().parent.parent

EXPECTED_PAGES = [
    "index.html",
    "product.html",
    "how-it-works.html",
    "capabilities.html",
    "use-cases.html",
    "validation.html",
    "security.html",
    "founding-beta.html",
    "about.html",
    "contact.html",
    "privacy.html",
    "terms.html",
    "beta-terms.html",
    "404.html",
]

class LinkExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.images = []
        self.scripts = []
        self.stylesheets = []
        self.inputs = []
        self.text_content = []

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        if tag == "a" and "href" in attrs_dict:
            self.links.append(attrs_dict["href"])
        elif tag == "img" and "src" in attrs_dict:
            self.images.append(attrs_dict["src"])
        elif tag == "script" and "src" in attrs_dict:
            self.scripts.append(attrs_dict["src"])
        elif tag == "link" and attrs_dict.get("rel") == "stylesheet" and "href" in attrs_dict:
            self.stylesheets.append(attrs_dict["href"])
        elif tag in ("input", "select", "textarea") and "name" in attrs_dict:
            self.inputs.append(attrs_dict["name"])

    def handle_data(self, data):
        self.text_content.append(data)

def test_all_expected_pages_exist():
    """Verify that every required page exists in the website root."""
    for page in EXPECTED_PAGES:
        page_path = BASE_DIR / page
        assert page_path.exists(), f"Missing required page: {page}"
        assert page_path.stat().st_size > 500, f"Page {page} is too small / empty."

def test_internal_links_and_assets_validity():
    """Verify all internal links, stylesheet links, scripts, and image tags resolve to valid files."""
    for page in EXPECTED_PAGES:
        page_path = BASE_DIR / page
        content = page_path.read_text(encoding="utf-8")
        
        parser = LinkExtractor()
        parser.feed(content)

        # Check stylesheets
        for css in parser.stylesheets:
            css_path = BASE_DIR / css
            assert css_path.exists(), f"In {page}: Broken stylesheet link {css}"

        # Check scripts
        for js in parser.scripts:
            js_path = BASE_DIR / js
            assert js_path.exists(), f"In {page}: Broken script link {js}"

        # Check images
        for img in parser.images:
            if not img.startswith("data:") and not img.startswith("http"):
                img_path = BASE_DIR / img
                assert img_path.exists(), f"In {page}: Broken image link {img}"

        # Check internal links
        for link in parser.links:
            if link.startswith("#") or link.startswith("mailto:") or link.startswith("http"):
                continue
            clean_link = link.split("#")[0]
            if clean_link:
                target_path = BASE_DIR / clean_link
                assert target_path.exists(), f"In {page}: Broken internal link to '{link}'"

def test_seo_and_accessibility_meta():
    """Verify standard accessibility elements, viewports, titles, and descriptions."""
    for page in EXPECTED_PAGES:
        content = (BASE_DIR / page).read_text(encoding="utf-8")
        assert "<title>" in content, f"Missing <title> in {page}"
        assert 'name="viewport"' in content, f"Missing responsive viewport in {page}"
        assert 'name="description"' in content, f"Missing meta description in {page}"
        assert 'class="skip-link"' in content, f"Missing accessible skip-link in {page}"
        assert 'id="main-content"' in content, f"Missing main content landmark in {page}"

def test_founding_beta_form_fields():
    """Verify that all required beta application fields and controls are present."""
    beta_path = BASE_DIR / "founding-beta.html"
    content = beta_path.read_text(encoding="utf-8")
    
    parser = LinkExtractor()
    parser.feed(content)
    
    required_names = [
        "applicant_name",
        "organization_name",
        "job_title",
        "business_email",
        "industry",
        "project_type",
        "project_size",
        "record_count",
        "project_status",
        "ground_truth",
        "evaluation_problem",
        "capabilities",
        "structured_feedback",
        "future_paid_interest",
        "comments"
    ]
    
    for req in required_names:
        assert req in parser.inputs, f"Founding Beta form is missing input field: '{req}'"

def test_legal_pages_hardened_and_no_draft_markers():
    """Verify that privacy, terms, and beta terms are hardened and contain zero draft markers."""
    for page in EXPECTED_PAGES:
        content = (BASE_DIR / page).read_text(encoding="utf-8")
        assert "DRAFT — REQUIRES OWNER" not in content, f"Page {page} contains draft review banner"
        assert "LEGAL_DRAFT" not in content, f"Page {page} contains LEGAL_DRAFT badge"
        assert "(Draft)" not in content, f"Page {page} contains '(Draft)' label"

def test_corporate_identity_and_copyright():
    """Verify legal entity PEIS Intelligence LLC and standard copyright attribution sitewide."""
    copyright_str = "&copy; 2026 PEIS Intelligence LLC. All rights reserved."
    for page in EXPECTED_PAGES:
        content = (BASE_DIR / page).read_text(encoding="utf-8")
        assert copyright_str in content, f"Page {page} is missing authoritative copyright: {copyright_str}"
    
    # Verify entity name on core governance pages
    entity_pages = ["about.html", "privacy.html", "terms.html", "beta-terms.html", "contact.html"]
    for page in entity_pages:
        content = (BASE_DIR / page).read_text(encoding="utf-8")
        assert "PEIS Intelligence LLC" in content, f"Page {page} missing legal entity 'PEIS Intelligence LLC'"

def test_scope_isolation_and_forbidden_products():
    """Verify complete product scope isolation (0 Contractor Exam Prep, 0 LUCEVIA sitewide)."""
    forbidden_terms = [
        "contractor exam",
        "exam prep",
        "lucevia",
        "e07",
    ]
    for page in EXPECTED_PAGES:
        content = (BASE_DIR / page).read_text(encoding="utf-8").lower()
        for term in forbidden_terms:
            assert term not in content, f"Page {page} contains forbidden product term '{term}'"

def test_authoritative_statements():
    """Verify the conceptual chain, internal validation baseline statement, human-in-the-loop presence, and validation boundaries."""
    home_content = (BASE_DIR / "index.html").read_text(encoding="utf-8")
    val_content = (BASE_DIR / "validation.html").read_text(encoding="utf-8")
    beta_content = (BASE_DIR / "founding-beta.html").read_text(encoding="utf-8")
    contact_content = (BASE_DIR / "contact.html").read_text(encoding="utf-8")
    
    # Directive PEIS-WEB-PRH-002-CA01: preferred public wording
    assert "PEIS has completed internal regression and acceptance testing against its governing validation baseline" in val_content
    assert "PEIS has completed internal regression and acceptance testing against its governing validation baseline" in home_content
    assert "Source" in home_content and "Decision" in home_content
    assert "Human" in home_content

    # Directive 001/002 specific assertions
    assert "Independent external validation has not yet been completed" in val_content
    assert "Internal Validation Baseline Frozen" in val_content
    assert "Frozen Validation Baseline Verified" not in val_content
    assert "Founding Beta Program is intended in part to obtain additional real-world performance" in val_content
    assert "separate controlled onboarding" in beta_content

def test_no_historical_numerical_test_counts():
    """Verify that unsupported historical test counts (e.g. 54/54) are absent across all public HTML pages."""
    forbidden_counts = ["54/54", "54 / 54", "54 internal"]
    for page in EXPECTED_PAGES:
        content = (BASE_DIR / page).read_text(encoding="utf-8")
        for count in forbidden_counts:
            assert count not in content, f"Page {page} contains historical test count '{count}'"


def test_no_absolute_or_unsubstantiated_claims():
    """Verify that forbidden absolute claim strings are completely absent across all pages."""
    forbidden_terms = [
        "total auditability",
        "zero ungrounded",
        "cannot be silently tampered",
        "immune to",
        "federal grade",
    ]
    for page in EXPECTED_PAGES:
        content = (BASE_DIR / page).read_text(encoding="utf-8").lower()
        for term in forbidden_terms:
            assert term not in content, f"Page {page} contains forbidden claim term '{term}'"

def test_standardized_sitewide_navigation():
    """Verify that all pages have the standardized commercial navigation IA."""
    required_nav_labels = ["Product", "Solutions", "How PEIS Works", "Use Cases", "Trust", "Company", "Apply for Founding Beta"]
    for page in EXPECTED_PAGES:
        content = (BASE_DIR / page).read_text(encoding="utf-8")
        assert 'class="main-nav"' in content, f"Page {page} missing main-nav"
        for label in required_nav_labels:
            assert label in content, f"Page {page} missing standard nav label '{label}'"

def test_email_normalization():
    """Verify that only contact@peisintel.com is exposed as a public contact email address in HTML pages."""
    forbidden_emails = [
        "beta@peisintel.com",
        "inquiries@peisintel.com",
        "privacy@peisintel.com",
        "support@peisintel.com",
        "beta@peis.ai",
        "inquiries@peis.ai",
        "contact@peis.ai",
        "todd@",
        "rossy@",
    ]
    for page in EXPECTED_PAGES:
        content = (BASE_DIR / page).read_text(encoding="utf-8").lower()
        for bad_email in forbidden_emails:
            assert bad_email not in content, f"Page {page} contains unconfirmed or forbidden email address '{bad_email}'"
    
    # Verify contact@peisintel.com is present on contact.html and privacy.html
    contact_content = (BASE_DIR / "contact.html").read_text(encoding="utf-8")
    privacy_content = (BASE_DIR / "privacy.html").read_text(encoding="utf-8")
    assert "contact@peisintel.com" in contact_content
    assert "contact@peisintel.com" in privacy_content


