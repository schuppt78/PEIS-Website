# Local Development & Testing Guide

## 1. Prerequisites
- Python 3.10+ (Standard Python runtime)
- Any modern web browser (Edge, Chrome, Firefox, Safari)
- `pytest` for running automated verification tests

---

## 2. Launching the Local Development Server

### Option A: Enhanced Local Server with Submission Logger (Recommended)
This script serves the static site and logs beta applications submitted from the browser to `scratch/beta_applications.log` without requiring external services:

```powershell
python scripts/serve.py --port 8000
```
Open [http://localhost:8000](http://localhost:8000) in your web browser.

### Option B: Standard Python Built-in Server
```powershell
python -m http.server 8000
```
Open [http://localhost:8000](http://localhost:8000) in your web browser.

---

## 3. Running Automated Tests

Run the full automated test suite to verify HTML integrity, internal links, security posture, and PEIS isolation:

```powershell
pytest tests/ -v
```

### Specific Test Modules
- **Link & HTML Structure Validation**: `pytest tests/test_website.py -v`
- **Security & Secret Leakage Audit**: `pytest tests/test_security.py -v`
- **PEIS v0.1 Isolation Verification**: `pytest tests/test_isolation.py -v`

---

## 4. Capturing Automated Screenshots
To generate high-resolution PNG screenshots of all key desktop and mobile pages:

```powershell
python scripts/capture_screenshots.py
```
Output images are saved to `screenshots/` and copied to the review artifact directory.
