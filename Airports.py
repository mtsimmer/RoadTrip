'''
Reordering Dataset
'''
import json

Airports = []
continent_to_airport = {}
country_to_airport = {}


def load_airports(airport_dataset_path=r"Datasets\airport-codes_json.json"):
	"""
	writes all airports in the dataset and places it in Airports
	"""
	global Airports
	with open(airport_dataset_path) as f:
		Airports = json.load(f)
	return Airports

def get_continent_airports(Airports, continent):
	"""
	returns all airports in a continent
	"""
	global continent_to_airport
	if continent not in continent_to_airport.keys():
		continent_to_airport = dicitnarize_by_prop(Airports, 'continent', continent)
	try:
		return continent_to_airport[continent]
	except KeyError:
		print("No such continet \navailable continents:", continent_to_airport.keys())

def get_country_airports(Airports, country):
	"""
	returns country's airport
	"""
	global country_to_airport
	if country not in country_to_airport.keys():
		country_to_airport = dicitnarize_by_prop(Airports, 'iso_country', country)
	try:
		return country_to_airport[country]
	except KeyError:
		print("No such country \navailable countries:", country_to_airport.keys())

def get_all_IATAs(Airports):
	All_IATAs = []
	for air in Airports:
		if air['iata_code'] != None:
			All_IATAs.append(air['iata_code'])
	return All_IATAs



def dicitnarize_by_prop(Airports, prop, val):
	"""
	returns dict of the requested prop of an airport
	"""
	air_to_val = {}
	for air in Airports:
		if air[prop] == val:
			if val not in air_to_val.keys():
				air_to_val[val] = [air]
			else:
				air_to_val[val].append(air)
	return air_to_val
