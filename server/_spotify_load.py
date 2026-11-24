import json
import time
from spotify_scraper import SpotifyClient

def spotify_download(playlist_url, output_file="playlist_songs.json"):
    with SpotifyClient() as client:
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

        time.sleep(10)
        
        return output_data
