"""
PEIS Security Review Test Suite
Verifies that no secrets, credentials, API keys, or proprietary analytical modules were leaked or copied.
"""

import os
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

FORBIDDEN_PATTERNS = [
    re.compile(r"sk-[a-zA-Z0-9]{20,}", re.IGNORECASE),
    re.compile(r"ghp_[a-zA-Z0-9]{20,}", re.IGNORECASE),
    re.compile(r"BEGIN (RSA|EC|DSA|OPENSSH) PRIVATE KEY", re.IGNORECASE),
    re.compile(r"password\s*=\s*['\"][^'\"]{8,}['\"]", re.IGNORECASE),
    re.compile(r"postgres://", re.IGNORECASE),
    re.compile(r"mysql://", re.IGNORECASE),
    re.compile(r"mongodb://", re.IGNORECASE),
]

def test_no_secrets_in_website_files():
    """Scan all files in website repository for secret patterns."""
    text_extensions = {".html", ".css", ".js", ".json", ".md", ".xml", ".txt", ".py", ".toml"}
    
    for root, _, files in os.walk(BASE_DIR):
        # Skip scratch log, .git, and test files defining regexes
        if "scratch" in root or ".git" in root or ".pytest_cache" in root or "tests" in root:
            continue
        for file in files:
            file_path = Path(root) / file
            if file_path.suffix.lower() in text_extensions or file in ("_headers", "robots.txt"):
                content = file_path.read_text(encoding="utf-8", errors="ignore")
                for pattern in FORBIDDEN_PATTERNS:
                    match = pattern.search(content)
                    assert match is None, f"Potential secret matched in {file_path.relative_to(BASE_DIR)}: {pattern.pattern}"

def test_no_proprietary_peis_modules_copied():
    """Verify that no proprietary PEIS backend Python modules were copied into this website."""
    forbidden_filenames = {
        "peis_server.py",
        "peis_dashboard.py",
        "peis_cli.py",
        "peis_admin.py",
        "peis_monte_carlo.py",
        "peis_schedule_dna.py",
        "peis_scorecard_gen.py",
        "peis_doc_ingest.py",
        "peis_saas_license.py",
        "peis_business_autopilot.py",
        "evaluation_engine.py",
    }
    
    found_files = []
    for root, _, files in os.walk(BASE_DIR):
        for file in files:
            if file.lower() in forbidden_filenames:
                found_files.append(file)
                
    assert len(found_files) == 0, f"Proprietary PEIS files found in website workspace: {found_files}"

def test_security_headers_configured():
    """Verify that modern security headers (CSP, X-Frame-Options, nosniff) are defined in deployment configs."""
    headers_file = BASE_DIR / "_headers"
    netlify_file = BASE_DIR / "netlify.toml"
    vercel_file = BASE_DIR / "vercel.json"
    
    assert headers_file.exists(), "Missing _headers configuration file"
    assert netlify_file.exists(), "Missing netlify.toml configuration file"
    assert vercel_file.exists(), "Missing vercel.json configuration file"
    
    headers_content = headers_file.read_text(encoding="utf-8")
    assert "X-Frame-Options: DENY" in headers_content
    assert "X-Content-Type-Options: nosniff" in headers_content
    assert "Content-Security-Policy" in headers_content
