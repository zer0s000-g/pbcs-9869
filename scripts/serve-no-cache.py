#!/usr/bin/env python3
"""Serve Quartz public/ output locally with no-cache headers.

This avoids stale browser cache when checking local branding/content changes at
http://localhost:8080/.
"""
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import os

ROOT = Path(__file__).resolve().parents[1] / "public"
os.chdir(ROOT)


class NoCacheQuartzHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()

    def translate_path(self, path):
        raw = path.split("?", 1)[0].split("#", 1)[0]
        candidate = ROOT / raw.lstrip("/")
        if candidate.is_dir():
            index = candidate / "index.html"
            if index.exists():
                return str(index)
        if candidate.exists():
            return str(candidate)
        html = ROOT / (raw.lstrip("/") + ".html")
        if html.exists():
            return str(html)
        return str(ROOT / "index.html")


if __name__ == "__main__":
    httpd = ThreadingHTTPServer(("0.0.0.0", 8080), NoCacheQuartzHandler)
    print("Serving PBCS Quartz public output with no-cache headers at http://localhost:8080")
    httpd.serve_forever()
