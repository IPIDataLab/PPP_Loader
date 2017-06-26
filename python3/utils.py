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

# Convert bollean values to numeric
def trueFalseConstructor(boolean):
    if boolean == True:
        return 1
    elif boolean == False:
        return 0

# Converts 0 numeric values to NA for R
def NACheck(data,key):
    if key in data:
        return data[key]
    else:
        return 'NA'

def genderNACheck(out,data, key):
    male = key + '_m'
    female = key + '_f'
    total = key

    if male not in data and female not in data:
        out.append('NA')
        out.append('NA')
        out.append('NA')
    else:
        if male not in data:
            out.append(0)
        else:
            out.append(data[male])
        if female not in data:
            out.append(0)
        else:
            out.append(data[female])
        if total not in data:
            out.append(0)
        else:
            out.append(data[total])