import json
from pprint import pprint


with open('top100.json') as data_file:
	data = json.load(data_file)

#length = len(data['tracks']['items'])
length = len(data['items'])
print length

#for songs in range (0, length):
#	pprint(data['tracks']['items'][songs]['name'])
ctr=0

for songs in data['items']:
	pprint(str(ctr) +" "+ str(songs["track"]["id"])+" "+ str(songs["track"]["popularity"]))
	ctr+=1
