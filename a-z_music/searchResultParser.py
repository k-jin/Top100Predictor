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
	tracks[currentTrack['name']] = {'song_name':currentTrack['name'],'album':currentTrack['album']['name'], 'available_markets':currentTrack['available_markets'], 'duration_ms':currentTrack['duration_ms'], 'explicit':currentTrack['explicit'], 'popularity':currentTrack['popularity']}
	tracks[currentTrack['name']]['artists'] = []
	artistLength = len(currentTrack['artists'])
	for artists in range (0, artistLength):
		tracks[currentTrack['name']]['artists'].append(currentTrack['artists'][artists]['name'])

pprint(tracks)


# with open('names.csv', 'w') as csvfile:
    # fieldnames = ['first_name', 'last_name']
    # writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # writer.writeheader()
    # writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    # writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    # writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})
with open(sys.argv[1][0:-5]+'.csv', 'w') as csvfile:
	fieldnames = ['song_name', 'artists', 'album', 'duration_ms', 'popularity', 'explicit', 'available_markets']
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)