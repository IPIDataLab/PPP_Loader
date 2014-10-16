#!/usr/bin/python

import datetime, calendar

#############################
#############################
# This file contains a number
# of utility functions used by
# the PPP data loading package
# for data validation and error 
# catching
#############################
#############################


def validate(date_str):
    try:
    	# validate either short year (2002) or long year (02)
    	if len(date_str) > 5:
    		date = datetime.datetime.strptime(date_str, '%m/%Y')
    	else:
    		date = datetime.datetime.strptime(date_str, '%m/%y')
    	# concatinate year, month with leading zero, and last day of month
    	return str(date.year) + str(date.month).zfill(2) + str(calendar.monthrange(date.year, date.month)[1])
    	
    except ValueError:
        raise ValueError("Incorrect data format, should be MM/YYYY")

# Convert to ISO date
def dateToISOString(fromDateObject):
    return fromDateObject.strftime("%Y%m%dT%H%M%S")