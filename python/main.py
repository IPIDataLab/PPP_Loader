#!/usr/bin/python

import sys
from sys import argv
import traceback
from data_get import getNewData
from data_norm import normalize
from data_csv import csvCreator
from data_load import mongoLoad, dateCheck
from utils import validate
import json
import subprocess
from s3_connect import s3LoadFiles
import rpy2.robjects as robjects

def main():
	
	# If arguemnts given but not enough throw and error
	if len(argv) != 1 and len(argv) != 4:
		print "Please enter authentication adn update target as arguments or at the prompt"
		sys.exit()
	else:
		# if no arguments, prompt for user, password, and in date
		if len(argv) == 1:
			# validation credentials and ETL date target
			username = raw_input('Enter your MongoDB username:')
			password = raw_input('Enter your MongoDB password:')
			in_date = raw_input('Enter the date you want to update (mm/yyyy):')
		# if validation args given, pass
		elif len(argv) == 4:
			username = argv[1]
			password = argv[2]
			in_date = argv[3]
		
		# check to see if all three fields have input
		if len(username) < 1 or len(password) < 1 or len(in_date) < 1:
			print "You must enter a username, password and date"
			sys.exit()
		else:
			# validation check and str format
			update_date = validate(in_date)
			# grab target data from morph.io API
			update = getNewData(update_date)

			# if data returned, proceed
			if len(update) == 0:
				print 'No data returned from API. Check for API status or whether DPKO has published new numbers.'
			else:
				# normalize data
				norm_data = normalize(update, update_date)

				status_check = dateCheck(norm_data[1]['date'],username,password)

				if status_check == 1:
					# Creat csv files for R script and for archive 
					csvCreator(norm_data, update_date)

					# Run reporting script
					r = robjects.r
					r.source("../r/reporting.R")

					# load data into mongodb
					mongoLoad(norm_data, username, password)

					# Load generated files to s3 bucket
					s3LoadFiles()

				elif status_check == 0:
					print "Data already up to date."
			

if __name__ == '__main__':
	main()