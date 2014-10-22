#!/usr/bin/python

import json
import csv
from utils import trueFalseConstructor, NACheck, genderNACheck
from os import remove, rename

full_header_array = ['Date','Contributor','Contributor_ISO-3','Contributor_Capital','Contributor_Capital_Latitude','Contributor_Capital_Longitude','Contributor_Continent','Contributor_Region','Contributor UN_Bloc','Contributor_P5G4A3','Contributor_NAM','Contributor_G77','Contributor_AU','Contributor_Arab_League','Contributor_OIC','Contributor_CIS','Contributor_G20','Contributor_EU','Contributor_NATO','Contributor_G8','Contributor_OECD','Contributor_ASEAN','Contributor_OAS','Contributor_Shanghai','Contributor_GCC','Contributor_UMA','Contributor_COMESA','Contributor_CENSAD','Contributor_EAC','Contributor_ECCAS','Contributor_ECOWAS','Contributor_IGAD','Contributor_SADC','Mission','Mission_Country','Mission_Country_ISO-3','Mission_HQ','Mission_HQ_Longitude','Mission_HQ_Latitude','Mission_Continent','Mission_Region','Mission_UN_Bloc','Mission_P5G4A3','Mission_NAM','Mission_G77','Mission_AU','Mission_Arab_League','Mission_OIC','Mission_CIS','Mission_G20','Mission_EU','Mission_NATO','Mission_G8','Mission_OECD','Mission_ASEAN','Mission_OAS','Mission_Shanghai','Mission_GCC','Mission_UMA','Mission_COMESA','Mission_CENSAD','Mission_EAC','Mission_ECCAS','Mission_ECOWAS','Mission_IGAD','Mission_SADC','Experts_on_Mission','Formed_Police_Units','Inidividual_Police','Civilian_Police','Troops','Observers','Total']

gender_header_array = ['Date','Contributor','Contributor_ISO-3','Mission','Individual_Police_Male','Individual_Police_Female','Individual_Police_Total','Formed_Police_Units_Male','Formed_Police_Units_Female','Formed_Police_Units_Total','Experts_on_Mission_Male','Experts_on_Mission_Female','Experts_on_Mission_Total','Troops_Male','Troops_Female','Troops_Total','Total_Male','Total_Female','Total_Total']

def fullArrayConstructor(data):
	output = []
	date = data['cont_date'][0:4] + '-' + data['cont_date'][4:6] + '-' + data['cont_date'][6:8]
	output.append(date)
	output.append(data['tcc_country_string'])
	output.append(data['tcc_country_id'])
	output.append(data['tcc_capital'])
	output.append(data['tcc_capital_loc']['y'])
	output.append(data['tcc_capital_loc']['x'])
	output.append(data['tcc_continent'])
	output.append(data['tcc_un_region'])
	output.append(data['tcc_un_bloc'])
	output.append(data['tcc_p5g4a3'])

	output.append(trueFalseConstructor(data['tcc_nam']))
	output.append(trueFalseConstructor(data['tcc_g77']))
	output.append(trueFalseConstructor(data['tcc_au']))
	output.append(trueFalseConstructor(data['tcc_arabLeague']))
	output.append(trueFalseConstructor(data['tcc_oic']))
	output.append(trueFalseConstructor(data['tcc_cis']))
	output.append(trueFalseConstructor(data['tcc_g20']))
	output.append(trueFalseConstructor(data['tcc_eu']))
	output.append(trueFalseConstructor(data['tcc_nato']))
	output.append(trueFalseConstructor(data['tcc_g8']))
	output.append(trueFalseConstructor(data['tcc_oecd']))
	output.append(trueFalseConstructor(data['tcc_asean']))
	output.append(trueFalseConstructor(data['tcc_oas']))
	output.append(trueFalseConstructor(data['tcc_shanghai']))
	output.append(trueFalseConstructor(data['tcc_gcc']))
	output.append(trueFalseConstructor(data['tcc_uma']))
	output.append(trueFalseConstructor(data['tcc_comesa']))
	output.append(trueFalseConstructor(data['tcc_censad']))
	output.append(trueFalseConstructor(data['tcc_eac']))
	output.append(trueFalseConstructor(data['tcc_eccas']))
	output.append(trueFalseConstructor(data['tcc_ecowas']))
	output.append(trueFalseConstructor(data['tcc_igad']))
	output.append(trueFalseConstructor(data['tcc_sadc']))

	output.append(data['mission'])
	output.append(data['mission_country'])
	output.append(data['mission_country_id'])
	output.append(data['mission_hq'])
	output.append(data['mission_hq_loc']['y'])
	output.append(data['mission_hq_loc']['x'])
	output.append(data['mission_continent'])
	output.append(data['mission_un_region'])
	output.append(data['mission_un_bloc'])
	output.append(data['mission_p5g4a3'])

	output.append(trueFalseConstructor(data['mission_nam']))
	output.append(trueFalseConstructor(data['mission_g77']))
	output.append(trueFalseConstructor(data['mission_au']))
	output.append(trueFalseConstructor(data['mission_arabLeague']))
	output.append(trueFalseConstructor(data['mission_oic']))
	output.append(trueFalseConstructor(data['mission_cis']))
	output.append(trueFalseConstructor(data['mission_g20']))
	output.append(trueFalseConstructor(data['mission_eu']))
	output.append(trueFalseConstructor(data['mission_nato']))
	output.append(trueFalseConstructor(data['mission_g8']))
	output.append(trueFalseConstructor(data['mission_oecd']))
	output.append(trueFalseConstructor(data['mission_asean']))
	output.append(trueFalseConstructor(data['mission_oas']))
	output.append(trueFalseConstructor(data['mission_shanghai']))
	output.append(trueFalseConstructor(data['mission_gcc']))
	output.append(trueFalseConstructor(data['mission_uma']))
	output.append(trueFalseConstructor(data['mission_comesa']))
	output.append(trueFalseConstructor(data['mission_censad']))
	output.append(trueFalseConstructor(data['mission_eac']))
	output.append(trueFalseConstructor(data['mission_eccas']))
	output.append(trueFalseConstructor(data['mission_ecowas']))
	output.append(trueFalseConstructor(data['mission_igad']))
	output.append(trueFalseConstructor(data['mission_sadc']))

	output.append(NACheck(data,'eom'))
	output.append(NACheck(data,'fpu'))
	output.append(NACheck(data,'ip'))
	output.append(NACheck(data,'civpol'))
	output.append(NACheck(data,'troops'))
	output.append(NACheck(data,'observers'))
	output.append(NACheck(data,'total'))


	return output

def genderArrayConstructor(data):
	output = []
	date = data['cont_date'][0:4] + '-' + data['cont_date'][4:6] + '-' + data['cont_date'][6:8]
	output.append(date)
	output.append(data['tcc_country_string'] + "'")
	output.append(data['tcc_country_id'] + "'")

	output.append(data['mission'] + "'")
	
	genderNACheck(output,data,'ip')
	genderNACheck(output,data,'fpu')
	genderNACheck(output,data,'eom')
	genderNACheck(output,data,'troops')
	genderNACheck(output,data,'total')

	return output


def csvCreator(data, update_date):
	# read in new month json to convert to csv
	new_data_in = open('../ppp_files/update_archive/json/' + update_date + '.json','rb')
	new_data = json.load(new_data_in)

	# Create new CSV archive file for input month
	archive_csv = open('../ppp_files/update_archive/csv/' + update_date + '.csv', 'wb')
	archive_writer = csv.writer(archive_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

	# replace 'current_month' csv for R monthly reports
	current_csv = open('../ppp_files/current_month/current_month.csv', 'wb')
	current_writer = csv.writer(current_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

	# open new full data csv write file
	new_full_csv = open('../ppp_files/new_full_data.csv', 'wb')
	new_full_writer = csv.writer(new_full_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

	# Read in old full data csv to add to new full data file
	full_csv = open('../ppp_files/full_data.csv','rb')
	full_csv_reader = csv.reader(full_csv, delimiter=',', quotechar="'")

	# open new gender data csv write file
	new_gender_csv = open('../ppp_files/new_full_gender_data.csv', 'wb')
	new_gender_writer = csv.writer(new_gender_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

	# Read in old gender data csv to add to new gender data file
	gender_csv = open('../ppp_files/full_gender_data.csv','rb')
	gender_csv_reader = csv.reader(gender_csv, delimiter=',', quotechar="'")
	
	# copy full data
	for line in gender_csv_reader:
		new_gender_writer.writerow(line)

	# copy full data
	for line in full_csv_reader:
		new_full_writer.writerow(line)

	# Write headers
	archive_writer.writerow(full_header_array)
	current_writer.writerow(full_header_array)

	for entry in data:
	    if entry['tcc_country_id'] == 'all' or entry['mission'] == 'all':
	    	pass
	    else:
	    	full_line_in = fullArrayConstructor(entry)
	    	gender_line_in = genderArrayConstructor(entry)

	    	archive_writer.writerow(full_line_in)
	    	current_writer.writerow(full_line_in)
	    	new_full_writer.writerow(full_line_in)
	    	new_gender_writer.writerow(gender_line_in)
	
	# remove and rename
	remove('../ppp_files/full_data.csv')
	rename('../ppp_files/new_full_data.csv','../ppp_files/full_data.csv')

	remove('../ppp_files/full_gender_data.csv')
	rename('../ppp_files/new_full_gender_data.csv','../ppp_files/full_gender_data.csv')