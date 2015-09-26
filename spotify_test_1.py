import spotipy

name = 'Heifetz'
spotify = spotipy.Spotify()
results = spotify.search(q='artist:' + name, type='artist')

print results