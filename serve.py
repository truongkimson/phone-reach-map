"""Serve this folder on port 8000 with caching turned off, so a phone always loads the latest files.

Usage: python3 serve.py
"""
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import os


class NoCacheHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()


if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    server = ThreadingHTTPServer(("", 8000), partial(NoCacheHandler, directory=here))
    print("Serving on http://0.0.0.0:8000 (no caching)")
    server.serve_forever()
