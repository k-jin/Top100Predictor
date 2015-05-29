
import json, csv, sys
from pprint import pprint


print "This is the name of the script: ", sys.argv[0]
print "Number of arguments: ", len(sys.argv)
print "The arguments are: " , str(sys.argv)



with open(sys.argv[1]) as data_file:
	data = json.load(data_file)

pprint(data)