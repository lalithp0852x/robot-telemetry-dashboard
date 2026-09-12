"""Simple URL shortener service using Python's standard library."""
from http.server import BaseHTTPRequestHandler,HTTPServer
from urllib.parse import urlparse,parse_qs
import secrets
links={}
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        code=self.path.strip('/'); self.send_response(302 if code in links else 200); self.send_header('Location',links[code]) if code in links else None; self.end_headers()
    def do_POST(self):
        url=parse_qs(urlparse(self.path).query).get('url',[None])[0]
        if not url: self.send_response(400); self.end_headers(); return
        code=secrets.token_urlsafe(4); links[code]=url; self.send_response(201); self.send_header('Content-Type','application/json'); self.end_headers(); self.wfile.write(f'{{"code":"{code}","url":"{url}"}}'.encode())
    def log_message(self,*_): pass
print('URL shortener: http://localhost:8001'); HTTPServer(('localhost',8001),Handler).serve_forever()
