import json, csv, sys, time
from pprint import pprint
from urllib import urlopen


with open('top100.json') as data_file:
	data = json.load(data_file)

length = len(data['items'])
print length
tracks = {}
apiKeys = ["JPGIYQEE2JFVVQFIZ", "EDTRTDL69QGI2KRW1", "LH8KBKRG97JTK8A2P"]

keyCounter = 1
currentKey = apiKeys[keyCounter]

ens1="http://developer.echonest.com/api/v4/song/profile?api_key="
ens2="&track_id=spotify:track:"
ens3="&bucket=id:spotify&bucket=audio_summary"


for songs in range(length):
	print songs
	if songs % 19 == 0:
		keyCounter = (keyCounter + 1)%3
		currentKey=apiKeys[keyCounter]
		time.sleep(60)
	currentTrack = data['items'][songs]['track']
	currentTrackID = currentTrack['id'].encode('utf-8')

	

	tracks[currentTrackID] = {'song_name':currentTrack['name'].encode('utf-8'),'album':currentTrack['album']['name'].encode('utf-8'), 'duration_ms':currentTrack['duration_ms'], 'explicit':currentTrack['explicit'], 'song_id':currentTrack['id'].encode('utf-8')}
	tracks[currentTrackID]['artists'] = []

	artistLength = len(currentTrack['artists'])
	
	
	tracks[currentTrackID]['artist_id']=currentTrack['artists'][0]['id'].encode('utf-8')

	artist_info=json.loads(urlopen("https://api.spotify.com/v1/artists/"+str(tracks[currentTrack['id'].encode('utf-8')]['artist_id'])).read())

	tracks[currentTrackID]['num_of_artists']=artistLength 

	for artists in range(artistLength):
		tracks[currentTrackID]['artists'].append(currentTrack['artists'][artists]['name'].encode('utf-8'))

	tracks[currentTrackID]['outcome']=1

	#echonest stuff below here

	enArtistURL = ens1 + currentKey + ens2 + str(currentTrackID) + ens3
	responseInfo = json.loads(urlopen(enArtistURL).read())
	if responseInfo['response']['status']['message']!="Success":
			continue

	
	audioSummary = responseInfo['response']['songs'][0]['audio_summary']

	tracks[currentTrackID]['danceability'] = audioSummary['danceability']
	tracks[currentTrackID]['energy'] = audioSummary['energy']
	tracks[currentTrackID]['loudness'] = audioSummary['loudness']
	tracks[currentTrackID]['speechiness'] = audioSummary['speechiness']
	tracks[currentTrackID]['tempo'] = audioSummary['tempo']
	tracks[currentTrackID]['acousticness']=audioSummary['acousticness']
	tracks[currentTrackID]['key']=audioSummary['key']
	tracks[currentTrackID]['liveness']=audioSummary['liveness']
	tracks[currentTrackID]['mode']=audioSummary['mode']
	tracks[currentTrackID]['time_signature']=audioSummary['time_signature']
	tracks[currentTrackID]['valence']=audioSummary['valence']

	tracks[currentTrackID]['song_title_en'] = responseInfo['response']['songs'][0]['title'].encode('utf-8')

	

print len(tracks)
with open('top100_testJ.csv', 'wb') as csvfile:
	fieldnames = ['song_name', 'song_id', 'artists', 'album', 'duration_ms', 'explicit', 'artist_id','num_of_artists', 'danceability','energy','loudness','speechiness','tempo','acousticness','key','liveness','mode','time_signature','valence','song_title_en','outcome']
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writeheader()
	for key in tracks:
		writer.writerow(tracks[key])
