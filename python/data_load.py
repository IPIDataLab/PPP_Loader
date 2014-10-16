#!/usr/bin/python

import pymongo
from pymongo import MongoClient

#############################
#############################
# This file loads normalized
# data into the mongodb
#############################
#############################

def mongo_load(data,username,password):

	# Make db connection
	client = MongoClient('localhost',27017)
	db = client.pppDB
	collection = db.contributions

	try:
		db.authenticate(username,password)
		print "Authenticated Mongo connection."

		in_date = data[1]["date"]

		# check to see if date already inputed
		if collection.find({'date':in_date}).count() == 0:
			collection.insert(data)
			print str(len(data)) + " documents inserted into contributions collection."
		else:
			print "Data already up to date."

	except:
		print "Wrong username or password!"


if __name__ == '__main__':
	mongo_load(data,username,password)