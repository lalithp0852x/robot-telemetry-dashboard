"""Tiny in-memory task API demo. Run with: python task_api.py"""
from http.server import BaseHTTPRequestHandler,HTTPServer
import json
tasks=[{"id":1,"title":"Connect telemetry stream","done":False}]
class Handler(BaseHTTPRequestHandler):
    def send_json(self,payload,status=200):
        body=json.dumps(payload).encode(); self.send_response(status); self.send_header('Content-Type','application/json'); self.send_header('Content-Length',str(len(body))); self.end_headers(); self.wfile.write(body)
    def do_GET(self): self.send_json(tasks if self.path=='/api/tasks' else {'error':'not found'},200 if self.path=='/api/tasks' else 404)
    def do_POST(self):
        if self.path!='/api/tasks': return self.send_json({'error':'not found'},404)
        data=json.loads(self.rfile.read(int(self.headers.get('Content-Length',0)))); task={'id':len(tasks)+1,'title':data.get('title','Untitled'),'done':False}; tasks.append(task); self.send_json(task,201)
    def log_message(self,*_): pass
print('Task API: http://localhost:8000/api/tasks'); HTTPServer(('localhost',8000),Handler).serve_forever()
