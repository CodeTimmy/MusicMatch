from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse, parse_qs
import json
import threading, time #debug
from _spotify_load import spotify_load

def start_api():
    class Handler(BaseHTTPRequestHandler):
        def setup(self):
            print(threading.current_thread().name, "setup", time.time(), flush=True) #debug
            super().setup()
        def do_GET(self):
            print(threading.current_thread().name, time.time(), self.path, flush=True) #debug
            # self.path == "/download?id=abc123"
            if not self.path.startswith("/api"):
                self.send_response(301)                 # 302 = temporär, 301 = permanent
                self.send_header("Location", "https://codetimmy.github.io/MusicMatch")
                self.end_headers()
                return
                
            parsed = urlparse(self.path)
            params = parse_qs(parsed.query)   # {"id": ["abc123"]}

            if self.path.startswith("/api/download"):
                # Einzelnen Wert holen (mit Default, falls nicht vorhanden)
                playlist_id = params.get("id", [None])[0]

                # Optional: fehlenden Parameter abfangen
                if playlist_id is None:
                    self.send_response(400)
                    self.send_header("Content-Type", "text/plain; charset=utf-8")
                    self.end_headers()
                    self.wfile.write(b"Missing 'id' parameter")
                    return
                else:
                    spotify_load(playlist_id, self)

        def log_message(self, format, *args):
            pass
    
    server = ThreadingHTTPServer(("0.0.0.0", 27021), Handler)

    print("✔ Webserver started", flush=True)
    
    server.serve_forever()
