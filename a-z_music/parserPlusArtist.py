from urllib import urlopen
import json, csv, sys
from pprint import pprint


print "This is the name of the script: ", sys.argv[0]
print "Number of arguments: ", len(sys.argv)
print "The arguments are: " , str(sys.argv)



with open(sys.argv[1]) as data_file:
	data = json.load(data_file)

dataItems  = data['tracks']['items']
tracks = {}


for i in range(0,len(dataItems)):

	currentTrack = dataItems[i]
	tracks[currentTrack['name'].encode('utf-8')] = {'song_name':currentTrack['name'].encode('utf-8'),'album':currentTrack['album']['name'].encode('utf-8'), 'duration_ms':currentTrack['duration_ms'], 'explicit':currentTrack['explicit'], 'song_id': currentTrack['id'].encode['utf-8']}
	
	tracks[currentTrack['name'].encode('utf-8')]['artists'] = []

	artistLength = len(currentTrack['artists'])
	
	tracks[currentTrack['name'].encode('utf-8')]['artist_id']=currentTrack['artists'][0]['id'].encode('utf-8')

	artist_info=json.loads(urlopen("https://api.spotify.com/v1/artists/"+str(tracks[currentTrack['name'].encode('utf-8')]['artist_id'])).read())
	
	tracks[currentTrack['name'].encode('utf-8')]['artist_popularity']=artist_info['popularity']
	tracks[currentTrack['name'].encode('utf-8')]['num_of_artists']=artistLength 
	tracks[currentTrack['name'].encode('utf-8')]['num_artist_followers']=artist_info["followers"]["total"]



	for artists in range (0, artistLength):
		tracks[currentTrack['name'].encode('utf-8')]['artists'].append(currentTrack['artists'][artists]['name'].encode('utf-8'))

# pprint(tracks)

print tracks['A Sky Full of Stars']
	#print tracks[currentTrack['name'].encode('utf-8')]

# csv_name = 'songs_' + str(sys.argv[1][0]) + '.csv'
# with open(csv_name, 'ab') as csvfile:
# 	fieldnames = ['song_name', 'song_id', 'artists', 'album', 'duration_ms', 'explicit', 'artist_id','artist_popularity','num_of_artists', 'num_artist_followers']
# 	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
# 	for key in tracks:
# 		writer.writerow(tracks[key])


	#url = urlopen('https://api.spotify.com/v1/tracks/{id}').read()

#JPGIYQEE2JFVVQFIZ

# http://developer.echonest.com/api/v4/song/profile?api_key=JPGIYQEE2JFVVQFIZ&track_id=spotify:track:4toSP60xmDNCFuXly8ywNZ&bucket=id:spotify&bucket=audio_summary

