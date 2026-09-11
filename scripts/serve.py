#!/usr/bin/env python3
"""
PEIS Local Development Server & Beta Application Logger
Serves static website files and logs beta intake submissions locally.
"""

import http.server
import socketserver
import json
import os
import sys
from pathlib import Path
from datetime import datetime

PORT = 8000
BASE_DIR = Path(__file__).resolve().parent.parent
LOG_DIR = BASE_DIR / "scratch"
LOG_FILE = LOG_DIR / "beta_applications.log"

class PEISRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(BASE_DIR), **kwargs)

    def do_POST(self):
        if self.path == "/api/beta-apply":
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length)
            
            try:
                data = json.loads(post_data.decode('utf-8'))
                LOG_DIR.mkdir(parents=True, exist_ok=True)
                
                with open(LOG_FILE, "a", encoding="utf-8") as f:
                    f.write(json.dumps(data) + "\n")
                
                print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Logged application: {data.get('reference_id')} from {data.get('applicant', {}).get('organization')}")
                
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                response = {"status": "success", "message": "Application logged locally.", "ref": data.get("reference_id")}
                self.wfile.write(json.dumps(response).encode('utf-8'))
            except Exception as e:
                self.send_response(400)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"status": "error", "message": str(e)}).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()

    def end_headers(self):
        # Add basic dev security headers
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("X-Frame-Options", "DENY")
        super().end_headers()

def run():
    port = PORT
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        port = int(sys.argv[1])
    
    with socketserver.TCPServer(("", port), PEISRequestHandler) as httpd:
        print(f"==================================================")
        print(f" PEIS Local Development Server running on port {port}")
        print(f" http://localhost:{port}")
        print(f" Root Directory: {BASE_DIR}")
        print(f" Press Ctrl+C to stop.")
        print(f"==================================================")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")

if __name__ == "__main__":
    run()
