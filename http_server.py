from http.server import SimpleHTTPRequestHandler, HTTPServer

host = "0.0.0.0"
port = 8080

class CustomHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello, World!")  # Trả về chuỗi "Hello, World!"

httpd = HTTPServer((host, port), CustomHandler)
print(f"Serving HTTP on {host}:{port}")
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    print("\nShutting down server...")
    httpd.server_close()
