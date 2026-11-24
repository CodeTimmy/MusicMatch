import json
from spotify_scraper import SpotifyClient

def spotify_download(playlist_id: str, self):
    with SpotifyClient() as client:
        playlist_url = f"https://open.spotify.com/playlist/{playlist_id}"
        
        playlist = client.get_playlist(playlist_url)
        
        song_names = []
        for entry in playlist.tracks:
            track = entry.track
            artist = track.artists[0].name if track.artists else "Unknown Artist"
            song_names.append(f"{artist} - {track.name}")
        
        output_data = {"songs": song_names}
        
        with open(playlist_id, 'w', encoding='utf-8') as f:
            json.dump(output_data, f, indent=4, ensure_ascii=False)
        
        print(f"✔ {len(song_names)} Songs in '{output_file}' gespeichert.", flush=True)

        response = json.dumps().encode("utf-8")

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(response)))
        self.end_headers()
        self.wfile.write(response)
