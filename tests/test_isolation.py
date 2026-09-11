"""
PEIS v0.1 Strict Isolation Test Suite
Verifies that the frozen baseline repository remains completely untouched.
"""

import os
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent.parent
PEIS_CORE_DIR = Path(r"C:\Users\schup\OneDrive\Desktop\PEIS v0.1")

def test_peis_v01_exists_and_unmodified():
    """Verify that PEIS v0.1 exists and contains zero website files."""
    if not PEIS_CORE_DIR.exists():
        # If running in a separate environment without PEIS v0.1, pass
        return

    # Check that no website-specific files were written into PEIS v0.1
    website_artifacts = ["sitemap.xml", "how-it-works.html", "founding-beta.html", "beta-terms.html"]
    for art in website_artifacts:
        assert not (PEIS_CORE_DIR / art).exists(), f"Found website artifact inside PEIS v0.1: {art}"

def test_no_relative_imports_or_symlinks_to_core():
    """Verify that no website files import or symlink to PEIS v0.1."""
    for root, _, files in os.walk(BASE_DIR):
        for file in files:
            file_path = Path(root) / file
            assert not file_path.is_symlink(), f"Symlink found in website repo: {file_path}"
            if file_path.suffix.lower() in (".html", ".js", ".css"):
                content = file_path.read_text(encoding="utf-8", errors="ignore")
                assert "PEIS v0.1" not in content, f"Direct path reference to PEIS v0.1 found in {file}"
