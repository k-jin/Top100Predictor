import json
from pprint import pprint


with open('test.json') as data_file:
	data = json.load(data_file)

length = len(data['tracks']['items'])

print length

for songs in range (0, length):
	pprint(data['tracks']['items'][songs]['name'])
