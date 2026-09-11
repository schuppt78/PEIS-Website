#!/usr/bin/env python3
"""
PEIS Screenshot Capture Tool
Automates headless Edge screenshot generation across desktop and mobile viewports.
Saves PNGs to screenshots/ and copies to the artifact directory.
"""

import subprocess
import time
import socketserver
import http.server
import threading
import os
import shutil
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SCREENSHOT_DIR = BASE_DIR / "screenshots"
ARTIFACT_DIR = Path(r"C:\Users\schup\.gemini\antigravity\brain\5a6d4ae3-4d50-46b9-867d-c2216393961e")
EDGE_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
PORT = 8765

# Pages and sections to capture
PAGES = [
    # Standard Viewport Captures
    {"name": "desktop_home_1440x900", "file": "index.html", "width": 1440, "height": 900},
    {"name": "laptop_home_1280x800", "file": "index.html", "width": 1280, "height": 800},
    {"name": "tablet_home_768x1024", "file": "index.html", "width": 768, "height": 1024},
    {"name": "mobile_home_390x844", "file": "index.html", "width": 390, "height": 844},

    # Owner Corrective Pass Required Mobile Viewports
    {"name": "mobile_home_320px", "file": "index.html", "width": 320, "height": 600},
    {"name": "mobile_home_360px", "file": "index.html", "width": 360, "height": 740},
    {"name": "mobile_home_375px", "file": "index.html", "width": 375, "height": 667},
    {"name": "mobile_home_390px", "file": "index.html", "width": 390, "height": 844},
    {"name": "mobile_home_430px", "file": "index.html", "width": 430, "height": 932},

    # Full-Page Complete Captures (Header to Footer across viewports)
    {"name": "desktop_home_fullpage", "file": "index.html", "width": 1440, "height": 4800},
    {"name": "laptop_home_fullpage", "file": "index.html", "width": 1280, "height": 5200},
    {"name": "tablet_home_fullpage", "file": "index.html", "width": 768, "height": 6200},
    {"name": "mobile_home_320px_fullpage", "file": "index.html", "width": 320, "height": 9500},
    {"name": "mobile_home_360px_fullpage", "file": "index.html", "width": 360, "height": 9000},
    {"name": "mobile_home_375px_fullpage", "file": "index.html", "width": 375, "height": 8600},
    {"name": "mobile_home_390px_fullpage", "file": "index.html", "width": 390, "height": 8200},
    {"name": "mobile_home_430px_fullpage", "file": "index.html", "width": 430, "height": 7800},
    {"name": "mobile_home_fullpage", "file": "index.html", "width": 390, "height": 8200},

    # Section-Level Focused Captures
    {"name": "pipeline_flow", "file": "index.html#intelligence-flow", "width": 1440, "height": 900},
    {"name": "evaluation_chain", "file": "index.html#evaluation-chain", "width": 1440, "height": 900},
    {"name": "analytics_panels", "file": "index.html#capabilities", "width": 1440, "height": 900},
    {"name": "use_cases_section", "file": "index.html#use-cases", "width": 1440, "height": 900},
    {"name": "trust_section", "file": "index.html#trust", "width": 1440, "height": 900},

    # Secondary Pages & Legacy Aliases
    {"name": "desktop_home", "file": "index.html", "width": 1440, "height": 900},
    {"name": "laptop_home", "file": "index.html", "width": 1280, "height": 800},
    {"name": "tablet_home", "file": "index.html", "width": 768, "height": 1024},
    {"name": "mobile_home", "file": "index.html", "width": 390, "height": 844},
    {"name": "product_page", "file": "product.html", "width": 1440, "height": 900},
    {"name": "how_it_works_page", "file": "how-it-works.html", "width": 1440, "height": 900},
    {"name": "capabilities_page", "file": "capabilities.html", "width": 1440, "height": 900},
    {"name": "use_cases_page", "file": "use-cases.html", "width": 1440, "height": 900},
    {"name": "validation_page", "file": "validation.html", "width": 1440, "height": 900},
    {"name": "security_page", "file": "security.html", "width": 1440, "height": 900},
    {"name": "founding_beta_page", "file": "founding-beta.html", "width": 1440, "height": 900},
    {"name": "beta_application_form", "file": "founding-beta.html#founding-beta-form", "width": 1280, "height": 1000},
    {"name": "about_page", "file": "about.html", "width": 1440, "height": 900},
    {"name": "contact_page", "file": "contact.html", "width": 1440, "height": 900},
    {"name": "privacy_page", "file": "privacy.html", "width": 1440, "height": 900},
    {"name": "terms_page", "file": "terms.html", "width": 1440, "height": 900},
    {"name": "beta_terms_page", "file": "beta-terms.html", "width": 1440, "height": 900},
    {"name": "404_page", "file": "404.html", "width": 1440, "height": 900},
    
    # Secondary Full-Page Desktop Captures
    {"name": "product_fullpage", "file": "product.html", "width": 1440, "height": 3800},
    {"name": "capabilities_fullpage", "file": "capabilities.html", "width": 1440, "height": 4200},
    {"name": "how_it_works_fullpage", "file": "how-it-works.html", "width": 1440, "height": 4800},
    {"name": "use_cases_fullpage", "file": "use-cases.html", "width": 1440, "height": 4200},
    {"name": "validation_fullpage", "file": "validation.html", "width": 1440, "height": 3600},
    {"name": "security_fullpage", "file": "security.html", "width": 1440, "height": 3400},
    {"name": "founding_beta_fullpage", "file": "founding-beta.html", "width": 1440, "height": 3200},
    {"name": "about_fullpage", "file": "about.html", "width": 1440, "height": 2800},
    {"name": "contact_fullpage", "file": "contact.html", "width": 1440, "height": 2400},
    {"name": "privacy_fullpage", "file": "privacy.html", "width": 1440, "height": 2200},
    {"name": "terms_fullpage", "file": "terms.html", "width": 1440, "height": 2200},
    {"name": "beta_terms_fullpage", "file": "beta-terms.html", "width": 1440, "height": 2200},
    {"name": "404_fullpage", "file": "404.html", "width": 1440, "height": 1800},

    # Secondary Mobile Viewport Captures (390px)
    {"name": "product_mobile", "file": "product.html", "width": 390, "height": 844},
    {"name": "capabilities_mobile", "file": "capabilities.html", "width": 390, "height": 844},
    {"name": "how_it_works_mobile", "file": "how-it-works.html", "width": 390, "height": 844},
    {"name": "use_cases_mobile", "file": "use-cases.html", "width": 390, "height": 844},
    {"name": "validation_mobile", "file": "validation.html", "width": 390, "height": 844},
    {"name": "security_mobile", "file": "security.html", "width": 390, "height": 844},
    {"name": "founding_beta_mobile", "file": "founding-beta.html", "width": 390, "height": 844},
    {"name": "about_mobile", "file": "about.html", "width": 390, "height": 844},
    {"name": "contact_mobile", "file": "contact.html", "width": 390, "height": 844},
    {"name": "404_mobile", "file": "404.html", "width": 390, "height": 844},
]

class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(BASE_DIR), **kwargs)
    def log_message(self, format, *args):
        pass

def start_server():
    server = socketserver.TCPServer(("127.0.0.1", PORT), QuietHandler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    return server

def capture_screenshots():
    SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)
    if ARTIFACT_DIR.exists():
        ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)

    print(f"Starting local server on port {PORT}...")
    server = start_server()
    time.sleep(0.5)

    captured = []

    for item in PAGES:
        name = item["name"]
        file_path = item["file"]
        width = item["width"]
        height = item["height"]
        
        target_url = f"http://127.0.0.1:{PORT}/{file_path}"
        output_file = SCREENSHOT_DIR / f"{name}.png"
        
        print(f"Capturing [{name}] ({width}x{height}) -> {output_file.name}...")
        
        cmd = [
            EDGE_PATH,
            "--headless",
            "--disable-gpu",
            "--hide-scrollbars",
            "--force-device-scale-factor=1",
            f"--window-size={width},{height}",
            f"--screenshot={str(output_file)}",
            target_url
        ]
        
        try:
            res = subprocess.run(cmd, capture_output=True, timeout=15)
            if output_file.exists() and output_file.stat().st_size > 0:
                print(f"  [OK] Captured {output_file.name} ({output_file.stat().st_size // 1024} KB)")
                captured.append(output_file)
                # Copy to artifact directory
                if ARTIFACT_DIR.exists():
                    shutil.copy2(output_file, ARTIFACT_DIR / output_file.name)
            else:
                print(f"  [FAIL] Failed to capture {name}: {res.stderr.decode('utf-8', errors='ignore')}")
        except Exception as e:
            print(f"  [ERROR] Error capturing {name}: {e}")

    try:
        server.server_close()
    except Exception:
        pass
    print(f"\nCompleted capturing {len(captured)} screenshots.")
    return len(captured)

if __name__ == "__main__":
    capture_screenshots()
