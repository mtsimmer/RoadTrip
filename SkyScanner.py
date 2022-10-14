'''
Searching using skyScanner
'''
import requests
import Airports
import SkyScanner_Templates

def create_search(src,dst,y,m,d):
	URL = 'https://partners.api.skyscanner.net/apiservices/v3/flights/live/search/create'
	HEADERS = {'x-api-key': 'prtl6749387986743898559646983194'}

	query = SkyScanner_Templates.generate_search_json("TLV","MXP",2022,10,15)
	search = requests.post(URL, data=query, headers=HEADERS)
	session_token = json.loads(search.text)['session_token']
	return session_token

def poll_search(sessionToken):
	URL = f'https://partners.api.skyscanner.net/apiservices/v3/flights/live/search/poll/{sessionToken}'
	poll = requests.post(URL, headers=HEADERS)
