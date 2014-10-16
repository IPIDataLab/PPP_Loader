#!/usr/bin/python

import sys
from sys import argv
import traceback
from data_get import get_new_ppp_data
from data_norm import normalize
from data_load import mongo_load
from utils import validate

def main():

	# validation credentials and ETL date target
	username = raw_input('Enter your MongoDB username:')
	password = raw_input('Enter your MongoDB password:')
	in_date = raw_input('Enter the date you want to update (mm/yyyy):')

	# check to see if all three fields have input
	if len(username) < 1 or len(password) < 1 or len(in_date) < 1:
		print "You must enter a username, password and date"
		sys.exit()
	else:
		# validation check and str format
		update_date = validate(in_date)
		# grab target data from morph.io API
		update = get_new_ppp_data(update_date)

		# if data returned, proceed
		if len(update) == 0:
			print 'No data returned from API. Check for API status or whether DPKO has published new numbers.'
		else:
			# normalize data
			norm_data = normalize(update)
			# load data into mongodb
			mongo_load(norm_data, username, password)

if __name__ == '__main__':
	main()