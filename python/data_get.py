#!/usr/bin/python

import requests
import time, calendar
import json

#############################
#############################
# This file pulls data from
# the morph.io API, sends it  
# to be normalized and then 
# sends it to be loaded into 
# the mongodb.
#############################
#############################

def getNewData(date_str):
	# build query param based of user date input
	query = 'https://morph.io/IPINST/PPP_Scraper/data.json?key=P%2BC%2F7EFhx8IGx1ZW5N7D&query=select%20*%20from%20%22data%22%20where%20%22date%22%20%3D%20' + date_str

	# Requests http request collating custom header and query date
	r = requests.get(query)

	# Format data as json
	update = r.json()
	print "Morph.io API request returned " + str(len(update)) +" records."

	return update