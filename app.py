from http.server import BaseHTTPRequestHandler, HTTPServer
import socket, json

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','application/json')
        self.end_headers()
        res = {
            "mensaje": "Version 1.0 -Computacion Paralela","pod_id": socket.gethostname()
        }
        self.wfile.write(json.dumps(res).encode('utf-8'))

if __name__ == '__main__':
    HTTPServer(('0.0.0.0', 8081),Handler).serve_forever()
