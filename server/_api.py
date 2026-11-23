from http.server import BaseHTTPRequestHandler, HTTPServer
from _spotify_download import spotify_download

def start_api():
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            response = spotify_download("https://open.spotify.com/playlist/2KYHRYrmA7q3XMQFhIpUi6")

            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.send_header("Content-Length", str(len(response.encode())))
            self.end_headers()

            self.wfile.write(response.encode())

        def log_message(self, format, *args):
            pass  # Keine Logs
    
    server = HTTPServer(("0.0.0.0", 27021), Handler)

    print("✔ Webserver started", flush=True)
    
    server.serve_forever()
