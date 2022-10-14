'''
Searching using skyScanner
'''
import json
import requests
import Airports
import Directions
import SkyScanner_Templates

HEADERS = {'x-api-key': 'prtl6749387986743898559646983194'}
DESTINATIONS = {}

def create_search(src,dst,y,m,d):
	URL = 'https://partners.api.skyscanner.net/apiservices/v3/flights/live/search/create'
	# Destenation IDs instead of IATAs
	query = SkyScanner_Templates.generate_search_json(src,dst,y,m,d)
	search = requests.post(URL, data=query, headers=HEADERS)
	session_token = json.loads(search.text)['sessionToken']
	return session_token

def poll_search(sessionToken):
	URL = f'https://partners.api.skyscanner.net/apiservices/v3/flights/live/search/poll/{sessionToken}'
	poll = requests.post(URL, headers=HEADERS)
	poll = json.loads(poll.text)
	return poll

def get_destinations(DESTINATIONS=DESTINATIONS):
	"""
	returns and Loads into DESTINATIONS format {IATA : META...}
	"""
	URL = "https://partners.api.skyscanner.net/apiservices/v3/geo/hierarchy/flights/en-US"
	dests = json.loads(requests.get(URL,headers=HEADERS).text)['places']
	for dest_id in dests:
		if dests[dest_id]['iata'] not in DESTINATIONS.keys():
			DESTINATIONS[dests[dest_id]['iata']] = [dests[dest_id]]
		else:
			DESTINATIONS[dests[dest_id]['iata']].append(dests[dest_id])

def get_dest_id(unformated_sky_dests, unformated_wanted_dests):
	"""
	Matches according to cordinates dest ID to IATA
	excpects (lon,lat)
	"""
	# represents the maximal amount of KM allowed to be between two airports that are considered the same
	MAX_ALLOWED_DIST = 1
	wanted_dests = []
	for unformated_wanted_dest in unformated_wanted_dests:
		uformated_cords = unformated_wanted_dest['coordinates']
		wanted_dests.append([float(cord) for cord in uformated_cords.split(', ')])

	sky_dests = []
	for unformated_sky_dest in unformated_sky_dests:
		sky_dests.append((unformated_sky_dest['coordinates']['latitude'], unformated_sky_dest['coordinates']['longitude']))

	print('wanted : ',wanted_dests,'\nsky : ',sky_dests)
	dest_ids = []
	for wanted_dest in wanted_dests:
		for sky_dest in sky_dests:
			dist = Directions.calc_air_dist(sky_dest,wanted_dest)
			if dist < MAX_ALLOWED_DIST:
				print("The distance between the points :",dist) #Debug
				dest_ids.append(sky_dest)
	return dest_ids

