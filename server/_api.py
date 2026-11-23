from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
from _spotify_download import spotify_download

def start_api():
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            # self.path == "/download?id=abc123"
            if not self.path.startswith("/api"):
                self.send_response(301)                 # 302 = temporär, 301 = permanent
                self.send_header("Location", "https://codetimmy.github.io/MusicMatch")
                self.end_headers()
                return
                
            parsed = urlparse(self.path)
            params = parse_qs(parsed.query)   # {"id": ["abc123"]}

            if self.path.beginswith("/api/download"):
                # Einzelnen Wert holen (mit Default, falls nicht vorhanden)
                playlist_id = params.get("id", [None])[0]

                # Optional: fehlenden Parameter abfangen
                if playlist_id is None:
                    self.send_response(400)
                    self.send_header("Content-Type", "text/plain; charset=utf-8")
                    self.end_headers()
                    self.wfile.write(b"Missing 'id' parameter")
                    return

                url = f"https://open.spotify.com/playlist/{playlist_id}"
                response = str(spotify_download(url))

                self.send_response(200)
                self.send_header("Content-Type", "text/plain; charset=utf-8")
                self.send_header("Content-Length", str(len(response.encode())))
                self.end_headers()
                self.wfile.write(response.encode())

        def log_message(self, format, *args):
            pass
    
    server = HTTPServer(("0.0.0.0", 27021), Handler)

    print("✔ Webserver started", flush=True)
    
    server.serve_forever()
