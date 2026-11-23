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
from _spotify_download import spotify_download
from _api import start_api

PLAYLIST_URL = "https://open.spotify.com/playlist/2KYHRYrmA7q3XMQFhIpUi6"

if __name__ == "__main__":
    start_api()
    spotify_download(PLAYLIST_URL)
