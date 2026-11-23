print("Music Match - Server  Copyright (C) 2026  CodeTimmy")
print("This program comes with ABSOLUTELY NO WARRANTY.")
print("This is free software, and you are welcome to")
print("redistribute it under the GPL-3.0 conditions.")
print("-----------------------------------------------")
print("More information:")
print("https://github.com/CodeTimmy/MusicMatch/blob/main/LICENSE")
print("-----------------------------------------------")
print("Feel free to report bugs and suggest features at")
print("https://github.com/CodeTimmy/MusicMatch/issues")
print("")
print("")
print("")

import json
from spotify_scraper import SpotifyClient

# Playlist-URL oder ID hier einfügen
PLAYLIST_URL = "https://open.spotify.com/playlist/DEINE_PLAYLIST_ID"

def export_playlist_to_json(playlist_url, output_file="playlist_songs.json"):
    with SpotifyClient() as client:
        # Die Bibliothek holt alle Tracks der Playlist
        playlist = client.get_playlist(playlist_url)
        
        # Nur die Songnamen extrahieren
        song_names = [track.name for track in playlist.tracks]
        
        output_data = {"songs": song_names}
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(output_data, f, indent=4, ensure_ascii=False)
        
        print(f"✅ {len(song_names)} Songs in '{output_file}' gespeichert.")

if __name__ == "__main__":
    export_playlist_to_json(PLAYLIST_URL)
