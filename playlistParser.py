import json, csv, sys
from pprint import pprint
from urllib import urlopen


with open('top100.json') as data_file:
	data = json.load(data_file)

length = len(data['items'])
print length
tracks = {}


for songs in range (0, length):
	currentTrack = data['items'][songs]['track']

	tracks[currentTrack['name'].encode('utf-8')] = {'song_name':currentTrack['name'].encode('utf-8'),'album':currentTrack['album']['name'].encode('utf-8'), 'available_markets':currentTrack['available_markets'], 'duration_ms':currentTrack['duration_ms'], 'explicit':currentTrack['explicit'], 'popularity':currentTrack['popularity']}
	tracks[currentTrack['name'].encode('utf-8')]['artists'] = []

	artistLength = len(currentTrack['artists'])
	
	
	tracks[currentTrack['name'].encode('utf-8')]['artist_id']=currentTrack['artists'][0]['id'].encode('utf-8')

	artist_info=json.loads(urlopen("https://api.spotify.com/v1/artists/"+str(tracks[currentTrack['name'].encode('utf-8')]['artist_id'])).read())

	tracks[currentTrack['name'].encode('utf-8')]['artist_popularity']=artist_info['popularity']
	tracks[currentTrack['name'].encode('utf-8')]['num_of_artists']=artistLength 
	tracks[currentTrack['name'].encode('utf-8')]['num_artist_followers']=artist_info["followers"]["total"]



	for artists in range (0, artistLength):
		tracks[currentTrack['name'].encode('utf-8')]['artists'].append(currentTrack['artists'][artists]['name'].encode('utf-8'))
	#print tracks[currentTrack['name'].encode('utf-8')]['available_markets']
	for i in range (0,len(tracks[currentTrack['name'].encode('utf-8')]['available_markets'])):
		tracks[currentTrack['name'].encode('utf-8')]['available_markets'][i] = tracks[currentTrack['name'].encode('utf-8')]['available_markets'][i].encode('utf-8')

print len(tracks)
# with open('top100.csv', 'ab') as csvfile:
# 	fieldnames = ['song_name', 'artists', 'album', 'duration_ms', 'popularity', 'explicit', 'available_markets','artist_id','artist_popularity','num_of_artists', 'num_artist_followers']
# 	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
# 	for key in tracks:
# 		writer.writerow(tracks[key])
