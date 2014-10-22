#!/usr/bin/python

import pymongo
from pymongo import MongoClient
import sys

#############################
#############################
# This file loads normalized
# data into the mongodb
#############################
#############################


def dateCheck(date,username,password):
	# Make db connection
	try:
		client = MongoClient('localhost',27017)
		db = client.pppDB
		collection = db.contributions
	except pymongo.errors.ConnectionFailure:
		print '****************************************'
		print 'Your mongo DB instance is not connected. Either initiate mongod or install mongodb and initialize ppp data.'
		print '****************************************'
		sys.exit()

	try:
		db.authenticate(username,password)
		print "Authenticated Mongo connection."


		if collection.find({'cont_date':date}).count() != 0:
			return 0
		else:
			return 1
	except:
		print '****************************************'
		print "Wrong username or password!"
		print '****************************************'
		sys.exit()

def mongoLoad(data,username,password):

	# Make db connection
	client = MongoClient('localhost',27017)
	db = client.pppDB
	collection = db.contributions

	collection.insert(data)
	print str(len(data)) + " documents inserted into contributions collection."