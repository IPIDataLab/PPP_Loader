import pymongo
from pymongo import MongoClient
import sys

try:
	uri = "mongodb://cperry:50Crat3s@localhost:27017/pppDB"
# 		# mongodb://[username:password@]host1[:port1][,host2[:port2],...[,hostN[:portN]]][/[database][?options]]
# # uri = "mongodb://user:password@example.com/?authSource=source_database"
	client = MongoClient(uri)
# 		# client = MongoClient('ec2-54-209-244-136.compute-1.amazonaws.com',27017)
# 		# client = MongoClient('localhost',27017)
# 	db = client.pppDB
# 	collection = db.contributions
except:
	print "error"


# ssh -N -L 27017:127.0.0.1:80 bitnami@ec2-54-209-244-136.compute-1.amazonaws.com