from urllib import urlopen
import json, csv, sys
from pprint import pprint

audioSummary=json.loads(urlopen("http://developer.echonest.com/api/v4/song/profile?api_key=JPGIYQEE2JFVVQFIZ&track_id=spotify:track:4toSP60xmDNCFuXly8ywNZ&bucket=id:spotify&bucket=audio_summary").read())

audioDict={}
audioShortcut = audioSummary['response']['songs']
print audioShortcut[0]
audioDict['song_name'] = audioShortcut[5]
audioDict['artist_name'] = audioShortcut[2]
audioDict['danceability'] = audioShortcut[3]['danceability']
audioDict['energy'] =  audioShortcut[3]['energy']
audioDict['loudness'] = audioShortcut[3]['loudness']
audioDict['speechiness'] = audioShortcut[3]['speechiness']
audioDict['tempo'] = audioShortcut[3]['tempo']

# pprint(audioDict)