import spotipy
import pyen

sp = spotipy.Spotify()
en = pyen.Pyen('ZEUOKB8IFS86JL28M')

name = 'Lady Gaga'

response = en.get('playlist/static', artist=name, 
	bucket=['id:spotify'])

for song in response['songs']:
	song = str(song)
	song = song[1:-1]
	info = song.split(",")
	for entry in info:
		if(entry.startswith(' u\'id\'')):
			song_id = entry[10:-1]
			print(song_id)
	