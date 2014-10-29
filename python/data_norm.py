#!/usr/bin/python

import csv
import json
import datetime
import time
from utils import dateToISOString

#############################
#############################
# This file normalizes incoming
# data from the morph.io API 
# to conform with the Mongo 
# data model.
#############################
#############################

# Normalie data function
def normalize(data, update_date):

	# Load in mission object to add mission location data elements
	missions_in = open('../python/json/missions.json','rb')
	missions = json.load(missions_in)

	# Load in country object to add country location data elements
	countries_in = open('../python/json/countries.json','rb')
	countries = json.load(countries_in)

	# Output data array of objects to load into mongo
	data_out = []

	# Iterators to keep track of what has been entered
	dates = {}
	country_date = {}
	country_date_mission = {}

	# Dictionary to convert string type input to data base type conventions
	type_dict = {'Individual Police':'ip', 'Experts on Mission':'eom', 'Contingent Troop':'troops', 'Formed Police Units':'fpu'}

	# loop through incoming dat
	for entry in data:

		# Check to see if all mission all country object has been created for that date
		if str(entry['date']) not in dates:
			# create all mission all country object dont include numeric fields
			data_out.append({
				'cont_date':dateToISOString(datetime.datetime.strptime(str(entry['date']), '%Y%m%d').date()), 
				'tcc_country_id': 'all',
				'mission': 'all',
				'total': 0,
				'total_m': 0,
				'total_f': 0
			})
			# Add key (date) value (data_out index number) pair to dates object
			dates[str(entry['date'])] = len(data_out)-1

		# Check to see if all mission object has been created for that date country
		if (entry['tcc'] + '-' + str(entry['date'])) not in country_date:
			# Create all mission object for country date combo dont include numeric fields
			data_out.append({
				'cont_date':dateToISOString(datetime.datetime.strptime(str(entry['date']), '%Y%m%d').date()), 
				'tcc_country_id': entry['tccIso3Alpha'],
				'tcc_country_string': entry['tcc'],
				'tcc_au': countries[entry['tccIso3Alpha']]['au'],
				'tcc_eu': countries[entry['tccIso3Alpha']]['eu'],
				'tcc_ecowas': countries[entry['tccIso3Alpha']]['ecowas'],
				'tcc_cis': countries[entry['tccIso3Alpha']]['cis'],
				'tcc_gcc': countries[entry['tccIso3Alpha']]['gcc'],
				'tcc_g20': countries[entry['tccIso3Alpha']]['g20'],
				'tcc_eccas': countries[entry['tccIso3Alpha']]['eccas'],
				'tcc_shanghai': countries[entry['tccIso3Alpha']]['shanghai'],
				'tcc_nam': countries[entry['tccIso3Alpha']]['nam'],
				'tcc_oecd': countries[entry['tccIso3Alpha']]['oecd'],
				'tcc_uma': countries[entry['tccIso3Alpha']]['uma'],
				'tcc_nato': countries[entry['tccIso3Alpha']]['nato'],
				'tcc_igad': countries[entry['tccIso3Alpha']]['igad'],
				'tcc_sadc': countries[entry['tccIso3Alpha']]['sadc'],
				'tcc_eac': countries[entry['tccIso3Alpha']]['eac'],
				'tcc_oic': countries[entry['tccIso3Alpha']]['oic'],
				'tcc_g8': countries[entry['tccIso3Alpha']]['g8'],
				'tcc_comesa': countries[entry['tccIso3Alpha']]['comesa'],
				'tcc_p5g4a3': countries[entry['tccIso3Alpha']]['p5g4a3'],
				'tcc_oas': countries[entry['tccIso3Alpha']]['oas'],
				'tcc_censad': countries[entry['tccIso3Alpha']]['cen_sad'],
				'tcc_asean': countries[entry['tccIso3Alpha']]['asean'],
				'tcc_g77': countries[entry['tccIso3Alpha']]['g77'],
				'tcc_arabLeague': countries[entry['tccIso3Alpha']]['arab_league'],
				'tcc_capital': countries[entry['tccIso3Alpha']]['capital'],
				'tcc_capital_loc': countries[entry['tccIso3Alpha']]['capital_loc'],
				'tcc_continent': countries[entry['tccIso3Alpha']]['continent'],
				'tcc_un_region': countries[entry['tccIso3Alpha']]['un_region'],
				'tcc_un_bloc': countries[entry['tccIso3Alpha']]['un_bloc'],
				'mission': 'all',
				'total': 0,
				'total_m': 0,
				'total_f': 0
			})

			# Add key (country-date) value (data_out index number) pair to dates object
			country_date[(entry['tcc'] + '-' + str(entry['date']))] = len(data_out)-1

		if (entry['tcc'] + '-' + str(entry['date']) + '-' + entry['mission']) not in country_date_mission:
			# create new country-mission-date object
			data_out.append({
				'cont_date':dateToISOString(datetime.datetime.strptime(str(entry['date']), '%Y%m%d').date()), 
				'tcc_country_id': entry['tccIso3Alpha'],
				'tcc_country_string': entry['tcc'],
				'tcc_au': countries[entry['tccIso3Alpha']]['au'],
				'tcc_eu': countries[entry['tccIso3Alpha']]['eu'],
				'tcc_ecowas': countries[entry['tccIso3Alpha']]['ecowas'],
				'tcc_cis': countries[entry['tccIso3Alpha']]['cis'],
				'tcc_gcc': countries[entry['tccIso3Alpha']]['gcc'],
				'tcc_g20': countries[entry['tccIso3Alpha']]['g20'],
				'tcc_eccas': countries[entry['tccIso3Alpha']]['eccas'],
				'tcc_shanghai': countries[entry['tccIso3Alpha']]['shanghai'],
				'tcc_nam': countries[entry['tccIso3Alpha']]['nam'],
				'tcc_oecd': countries[entry['tccIso3Alpha']]['oecd'],
				'tcc_uma': countries[entry['tccIso3Alpha']]['uma'],
				'tcc_nato': countries[entry['tccIso3Alpha']]['nato'],
				'tcc_igad': countries[entry['tccIso3Alpha']]['igad'],
				'tcc_sadc': countries[entry['tccIso3Alpha']]['sadc'],
				'tcc_eac': countries[entry['tccIso3Alpha']]['eac'],
				'tcc_oic': countries[entry['tccIso3Alpha']]['oic'],
				'tcc_g8': countries[entry['tccIso3Alpha']]['g8'],
				'tcc_comesa': countries[entry['tccIso3Alpha']]['comesa'],
				'tcc_p5g4a3': countries[entry['tccIso3Alpha']]['p5g4a3'],
				'tcc_oas': countries[entry['tccIso3Alpha']]['oas'],
				'tcc_censad': countries[entry['tccIso3Alpha']]['cen_sad'],
				'tcc_asean': countries[entry['tccIso3Alpha']]['asean'],
				'tcc_g77': countries[entry['tccIso3Alpha']]['g77'],
				'tcc_arabLeague': countries[entry['tccIso3Alpha']]['arab_league'],
				'tcc_capital': countries[entry['tccIso3Alpha']]['capital'],
				'tcc_capital_loc': countries[entry['tccIso3Alpha']]['capital_loc'],
				'tcc_continent': countries[entry['tccIso3Alpha']]['continent'],
				'tcc_un_region': countries[entry['tccIso3Alpha']]['un_region'],
				'tcc_un_bloc': countries[entry['tccIso3Alpha']]['un_bloc'],
				'mission': entry['mission'],
				'mission_country_id': missions[entry['mission']]['country_id'],
				'mission_country': missions[entry['mission']]['country'],
				'mission_hq': missions[entry['mission']]['hq'],
				'mission_hq_loc': missions[entry['mission']]['mission_loc'],
				'mission_continent': countries[missions[entry['mission']]['country_id']]['continent'],
				'mission_un_region': countries[missions[entry['mission']]['country_id']]['un_region'],
				'mission_un_bloc': countries[missions[entry['mission']]['country_id']]['un_bloc'],
				'mission_au': countries[missions[entry['mission']]['country_id']]['au'],
				'mission_eu': countries[missions[entry['mission']]['country_id']]['eu'],
				'mission_ecowas': countries[missions[entry['mission']]['country_id']]['ecowas'],
				'mission_cis': countries[missions[entry['mission']]['country_id']]['cis'],
				'mission_gcc': countries[missions[entry['mission']]['country_id']]['gcc'],
				'mission_g20': countries[missions[entry['mission']]['country_id']]['g20'],
				'mission_eccas': countries[missions[entry['mission']]['country_id']]['eccas'],
				'mission_shanghai': countries[missions[entry['mission']]['country_id']]['shanghai'],
				'mission_nam': countries[missions[entry['mission']]['country_id']]['nam'],
				'mission_oecd': countries[missions[entry['mission']]['country_id']]['oecd'],
				'mission_uma': countries[missions[entry['mission']]['country_id']]['uma'],
				'mission_nato': countries[missions[entry['mission']]['country_id']]['nato'],
				'mission_igad': countries[missions[entry['mission']]['country_id']]['igad'],
				'mission_sadc': countries[missions[entry['mission']]['country_id']]['sadc'],
				'mission_eac': countries[missions[entry['mission']]['country_id']]['eac'],
				'mission_oic': countries[missions[entry['mission']]['country_id']]['oic'],
				'mission_g8': countries[missions[entry['mission']]['country_id']]['g8'],
				'mission_comesa': countries[missions[entry['mission']]['country_id']]['comesa'],
				'mission_p5g4a3': countries[missions[entry['mission']]['country_id']]['p5g4a3'],
				'mission_oas': countries[missions[entry['mission']]['country_id']]['oas'],
				'mission_censad': countries[missions[entry['mission']]['country_id']]['cen_sad'],
				'mission_asean': countries[missions[entry['mission']]['country_id']]['asean'],
				'mission_g77': countries[missions[entry['mission']]['country_id']]['g77'],
				'mission_arabLeague': countries[missions[entry['mission']]['country_id']]['arab_league'],
				'total': 0,
				'total_m': 0,
				'total_f': 0
			})
			# Add key (country-date-mission) value (data_out index number) pair to dates object
			country_date_mission[(entry['tcc'] + '-' + str(entry['date']) + '-' + entry['mission'])] = len(data_out)-1
		
		# Get insertion indexes for current entry
		country_date_mission_index = country_date_mission[(entry['tcc'] + '-' + str(entry['date']) + '-' + entry['mission'])]
		country_date_index = country_date[(entry['tcc'] + '-' + str(entry['date']))]
		dates_index = dates[str(entry['date'])]

		# Convert type to correct convention
		type_abbr = type_dict[entry['type']]
		type_abbr_m = type_dict[entry['type']] + '_m'
		type_abbr_f = type_dict[entry['type']] + '_f'

		# Insert country_date_mission data
		data_out[country_date_mission_index][type_abbr] = entry['T']
		data_out[country_date_mission_index][type_abbr_m] = entry['M']
		data_out[country_date_mission_index][type_abbr_f] = entry['F']
		data_out[country_date_mission_index]['total'] += entry['T']
		data_out[country_date_mission_index]['total_m'] += entry['M']
		data_out[country_date_mission_index]['total_f'] += entry['F']

		# Check to see if there is an entry in country_date entry and add accordingly
		if type_abbr in data_out[country_date_index]:
			data_out[country_date_index][type_abbr] += entry['T']
			data_out[country_date_index][type_abbr_m] += entry['M']
			data_out[country_date_index][type_abbr_f] += entry['F']
		else:
			data_out[country_date_index][type_abbr] = entry['T']
			data_out[country_date_index][type_abbr_m] = entry['M']
			data_out[country_date_index][type_abbr_f] = entry['F']

		# Check to see if there is an entry in dates entry and add accordingly
		if type_abbr in data_out[dates_index]:
			data_out[dates_index][type_abbr] += entry['T']
			data_out[dates_index][type_abbr_m] += entry['M']
			data_out[dates_index][type_abbr_f] += entry['F']
		else:
			data_out[dates_index][type_abbr] = entry['T']
			data_out[dates_index][type_abbr_m] = entry['M']
			data_out[dates_index][type_abbr_f] = entry['F']

		# Add to totals for tcc and total aggregates
		data_out[country_date_index]['total'] += entry['T']
		data_out[country_date_index]['total_m'] += entry['M']
		data_out[country_date_index]['total_f'] += entry['F']
		data_out[dates_index]['total'] += entry['T']
		data_out[dates_index]['total_m'] += entry['M']
		data_out[dates_index]['total_f'] += entry['F']

		# Observer corner case
		if type_abbr == 'eom':
			
			data_out[country_date_mission_index]['observers'] = entry['T']
			
			if 'observers' in data_out[country_date_index]:
				data_out[country_date_index]['observers'] += entry['T']
			else:
				data_out[country_date_index]['observers'] = entry['T']
			
			if 'observers' in data_out[dates_index]:
				data_out[dates_index]['observers'] += entry['T']
			else:
				data_out[dates_index]['observers'] = entry['T']

		else:
			pass

		# civpol corner case
		if type_abbr == 'ip' or type_abbr == 'fpu':
			if 'civpol' in data_out[country_date_mission_index]:
				data_out[country_date_mission_index]['civpol'] += entry['T']
			else:
				data_out[country_date_mission_index]['civpol'] = entry['T']

			if 'civpol' in data_out[country_date_index]:
				data_out[country_date_index]['civpol'] += entry['T']
			else:
				data_out[country_date_index]['civpol'] = entry['T']

			if 'civpol' in data_out[dates_index]:
				data_out[dates_index]['civpol'] += entry['T']
			else:
				data_out[dates_index]['civpol'] = entry['T']



	print "Converted " + str(len(data)) + " records into " + str(len(data_out)) + " documents."

	# test for double entries in normalization process
	test_array = []
	double_array = []
	for point in data_out:
		test_param = point['cont_date'] + ' ' + point['tcc_country_id'] + ' ' + point['mission']
		if test_param in test_array:
			double_array.append(test_param)
		else:
			test_array.append(test_param)

	if double_array == []:
		print 'No double entries!'
	else:
		for param in double_array:
			print param

	# write out archive of update into archive folder 
	print_out = open('../ppp_files/update_archive/json/' + update_date + '.json', 'w')
	print_out.write(json.dumps(data_out, indent=4, separators=(',', ':')))

	print_out.close()

	return data_out