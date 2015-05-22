import json
import sys
from pprint import pprint

with open(sys.argv[1]) as data_file:
	data = json.load(data_file)

dataItems  = data['tracks']['items']
length = len(dataItems)

tracks = {}

for songs in range (0, length):
	currentTrack = dataItems[songs]
	tracks[currentTrack['name']] = {'album':currentTrack['album']['name'], 'available_markets':currentTrack['available_markets'], 'duration_ms':currentTrack['duration_ms'], 'explicit':currentTrack['explicit'], 'popularity':currentTrack['popularity']}
	tracks[currentTrack['name']]['artists'] = []
	artistLength = len(currentTrack['artists'])
	for artists in range (0, artistLength):
		tracks[currentTrack['name']]['artists'].append(currentTrack['artists'][artists]['name'])

pprint(tracks)