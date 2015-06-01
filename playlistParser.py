import json, csv, sys
from pprint import pprint
from urllib import urlopen


with open('top100.json') as data_file:
	data = json.load(data_file)

length = len(data['items'])
print length
tracks = {}



for songs in range(length):
	currentTrack = data['items'][songs]['track']

	tracks[currentTrack['id'].encode('utf-8')] = {'song_name':currentTrack['name'].encode('utf-8'),'album':currentTrack['album']['name'].encode('utf-8'), 'duration_ms':currentTrack['duration_ms'], 'explicit':currentTrack['explicit'], 'song_id':currentTrack['id'].encode('utf-8')}
	tracks[currentTrack['id'].encode('utf-8')]['artists'] = []

	artistLength = len(currentTrack['artists'])
	
	
	tracks[currentTrack['id'].encode('utf-8')]['artist_id']=currentTrack['artists'][0]['id'].encode('utf-8')

	artist_info=json.loads(urlopen("https://api.spotify.com/v1/artists/"+str(tracks[currentTrack['id'].encode('utf-8')]['artist_id'])).read())

	tracks[currentTrack['id'].encode('utf-8')]['num_of_artists']=artistLength 

	for artists in range(artistLength):
		tracks[currentTrack['id'].encode('utf-8')]['artists'].append(currentTrack['artists'][artists]['name'].encode('utf-8'))

print len(tracks)
with open('top100.csv', 'wb') as csvfile:
	fieldnames = ['song_name', 'song_id', 'artists', 'album', 'duration_ms','explicit', 'artist_id','num_of_artists']
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writeheader()
	for key in tracks:
		writer.writerow(tracks[key])
