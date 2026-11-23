from http.server import BaseHTTPRequestHandler, HTTPServer

def start_api():
    print("4")
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            response = "<Hello Wo"

            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.send_header("Content-Length", str(len(response.encode())))
            self.end_headers()

            self.wfile.write(response.encode())

        def log_message(self, format, *args):
            pass  # Keine Logs

    print("19")
    
    server = HTTPServer(("0.0.0.0", 27021), Handler)

    print("✔ Webserver started")
    
    server.serve_forever()
