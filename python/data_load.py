#!/usr/bin/python

import pymongo
from pymongo import MongoClient

#############################
#############################
# This file loads normalized
# data into the mongodb
#############################
#############################


def dateCheck(date,username,password):
	# Make db connection
	client = MongoClient('localhost',27017)
	db = client.pppDB
	collection = db.contributions

	try:
		db.authenticate(username,password)
		print "Authenticated Mongo connection."


		if collection.find({'date':date}).count() != 0:
			return 0
		else:
			return 1
	
	except:
		print "Wrong username or password!"

def mongoLoad(data,username,password):

	# Make db connection
	client = MongoClient('localhost',27017)
	db = client.pppDB
	collection = db.contributions

	collection.insert(data)
	print str(len(data)) + " documents inserted into contributions collection."