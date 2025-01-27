from http.server import BaseHTTPRequestHandler, HTTPServer
import requests# Using requests library to fetch responses from servers

class CustomeRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/time":
            response = requests.get("http://localhost:8001/time")
            self.send_response(response.status_code)
            self.send_headers("content-type","text/plain")
            self.end_headers()
            self.wfile.write(response.content)
        elif self.path == "/ping":
            response = requests.get("http://localhost:8002/ping")
            self.send_response(response.status_code)
            self.send_headers("content-type","text/plain")
            self.end_headers()
            self.wfile.write(response.content)

if __name__ == "__main__":
    server_address = ('0.0.0.0', 8000)
    httpd = HTTPServer(server_address, CustomeRequestHandler)
    httpd.serve_forever()