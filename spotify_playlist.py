import spotipy
import pyen

sp = spotipy.Spotify()
en = pyen.Pyen('ZEUOKB8IFS86JL28M')

name = 'Lady Gaga'

response = en.get('playlist/static', artist=name, 
	bucket=['id:spotify'])

for song in response['songs']:
	print(song['id'])