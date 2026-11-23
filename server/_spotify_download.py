import json
from spotify_scraper import SpotifyClient

def spotify_download(playlist_url, output_file="playlist_songs.json"):
    with SpotifyClient() as client:
        # Die Bibliothek holt alle Tracks der Playlist
        playlist = client.get_playlist(playlist_url)
        
        # Nur die Songnamen extrahieren
        song_names = [entry.track.name for entry in playlist.tracks]
        
        output_data = {"songs": song_names}
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(output_data, f, indent=4, ensure_ascii=False)
        
        print(f"✅ {len(song_names)} Songs in '{output_file}' gespeichert.")
