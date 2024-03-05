from http.server import BaseHTTPRequestHandler, HTTPServer
import os

HOST = '0.0.0.0'
PORT = 8000

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            try:
                with open('index.html', 'rb') as f:
                    html_content = f.read()
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(html_content)
            except:
                self.send_error(404, "not found")
        else:
            self.send_error(404, "not found")

with HTTPServer((HOST, PORT), MyHandler) as server:
    print(f"Serving at http://{HOST}:{PORT}")
    server.serve_forever()
