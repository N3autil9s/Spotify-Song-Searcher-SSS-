import webbrowser

#Song names here
songs = [
   "Kiss from a Rose Seal",
    "Aerodynamic Daft Punk",
    "Shinunoga E-Wa Fujii Kaze",
    "Fly Me to the Moon Frank Sinatra",
    "Nightcall Kavinsky"
]

# Searches each song on Spotify
for song in songs:
    query = song.replace(" ", "+")
    webbrowser.open(f"https://open.spotify.com/search/{query}")


