"""Local dev server for Ren'Py web build with required headers for SharedArrayBuffer."""
import http.server
import socketserver
import os

PORT = 8080

class RenPyHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cross-Origin-Opener-Policy", "same-origin")
        self.send_header("Cross-Origin-Embedder-Policy", "require-corp")
        self.send_header("Cross-Origin-Resource-Policy", "cross-origin")
        super().end_headers()

    def log_message(self, format, *args):
        print(f"[{self.log_date_time_string()}] {args[0]}")

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with socketserver.TCPServer(("", PORT), RenPyHandler) as httpd:
    print(f"Server running at http://localhost:{PORT}")
    print("Open this URL in your browser (Chrome/Edge recommended)")
    print("Press Ctrl+C to stop")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
