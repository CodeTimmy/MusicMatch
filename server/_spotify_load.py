import json
from spotify_scraper import SpotifyClient
from _to_youtube import to_youtube

def spotify_load(playlist_id: str, self):
    with SpotifyClient() as client:
        playlist_url = f"https://open.spotify.com/playlist/{playlist_id}"
        output_file = f"spotify/{playlist_id}.json"
        
        playlist = client.get_playlist(playlist_url)
        
        song_names = []
        for entry in playlist.tracks:
            track = entry.track
            artist = track.artists[0].name if track.artists else "Unknown Artist"
            song_names.append(f"{artist} - {track.name}")
        
        output_data = {"songs": song_names}
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(output_data, f, indent=4, ensure_ascii=False)
        
        print(f"✔ {len(song_names)} Songs in '{output_file}' gespeichert.", flush=True)

        converted_data = output_json(output_file, playlist_id)
        
        response = json.dumps(converted_data).encode("utf-8")

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(response)))
        self.end_headers()
        self.wfile.write(response)
