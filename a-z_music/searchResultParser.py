import json
import sys, csv
from pprint import pprint

with open(sys.argv[1]) as data_file:
	data = json.load(data_file)

dataItems  = data['tracks']['items']
length = len(dataItems)

tracks = {}

for songs in range (0, length):
	currentTrack = dataItems[songs]
	tracks[currentTrack['name'].encode('utf-8')] = {'song_name':currentTrack['name'].encode('utf-8'),'album':currentTrack['album']['name'].encode('utf-8'), 'available_markets':currentTrack['available_markets'], 'duration_ms':currentTrack['duration_ms'], 'explicit':currentTrack['explicit'], 'popularity':currentTrack['popularity']}
	tracks[currentTrack['name'].encode('utf-8')]['artists'] = []
	artistLength = len(currentTrack['artists'])
	for artists in range (0, artistLength):
		tracks[currentTrack['name'].encode('utf-8')]['artists'].append(currentTrack['artists'][artists]['name'].encode('utf-8'))
	#print tracks[currentTrack['name'].encode('utf-8')]['available_markets']
	for i in range (0,len(tracks[currentTrack['name'].encode('utf-8')]['available_markets'])):
		tracks[currentTrack['name'].encode('utf-8')]['available_markets'][i] = tracks[currentTrack['name'].encode('utf-8')]['available_markets'][i].encode('utf-8')
# pprint(tracks)


# with open('names.csv', 'w') as csvfile:
#     fieldnames = ['first_name', 'last_name']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

#     writer.writeheader()
#     writer.writerow({'first_name': 'lol', 'last_name': 'mom'})
#     writer.writerow({'first_name': 'hey', 'last_name': 'Spam'})
#     writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})
with open('songs.csv', 'ab') as csvfile:
	fieldnames = ['song_name', 'artists', 'album', 'duration_ms', 'popularity', 'explicit', 'available_markets']
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	for key in tracks:
		writer.writerow(tracks[key])

