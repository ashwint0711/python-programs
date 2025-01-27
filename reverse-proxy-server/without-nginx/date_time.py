from http.server import BaseHTTPRequestHandler, HTTPServer
from datetime import datetime

class CustomeRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/time":
            self.send_response(200)
            self.end_headers()
            time = datetime.now().strftime("%H:%M")
            self.wfile.write((time+"\n").encode("utf-8"))
        else:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b'Invalid request!\n')


if __name__ == "__main__":
    server_address = ('0.0.0.0',8001)
    httpd = HTTPServer(server_address, CustomeRequestHandler)

    httpd.serve_forever()