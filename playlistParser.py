import json
from pprint import pprint


with open('top100.json') as data_file:
	data = json.load(data_file)

length = len(data['items'])
print length

ctr=0

for songs in data['items']:
	
	print songs['track']['name'] + ": " + str(ctr) +" "+ str(songs["track"]["id"])+" "+ str(songs["track"]["popularity"])
	ctr+=1
