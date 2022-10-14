MARKET = "IL"
LOCALE = "en-US"
CURRENCY = "USD"

def generate_search_json(origin_iata, dest_iata, year, mon, day):
	create_search = f'''{{
	  "query": {{
	    "market": "{MARKET}",
	    "locale": "{LOCALE}",
	    "currency": "{CURRENCY}",
	    "queryLegs": [
	      {{
	        "originPlaceId": {{
	          "iata": "{origin_iata}"
	        }},
	        "destinationPlaceId": {{
	          "iata": "{dest_iata}"
	        }},
	        "date": {{
	          "year": {year},
	          "month": {mon},
	          "day": {day}
	        }}
	      }}
	    ],
	    "cabinClass": "CABIN_CLASS_ECONOMY",
	    "adults": 1,
	    "childrenAges": [
	      0
	    ],
	    "includeSustainabilityData": true,
	    "nearbyAirports": true
	  }}
	}}'''

	return create_search