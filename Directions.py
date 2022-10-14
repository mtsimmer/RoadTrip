"""
Directions
"""
from math import sin, cos, sqrt, atan2, radians

def calc_air_dist(pt1,pt2):
	"""
	Calculates the air distance between 2 points
	"""
	R = 6373.0 # approximate radius of earth in km
	lat1, lon1 = [radians(num) for num in pt1]
	lat2, lon2 = [radians(num) for num in pt2]

	#lat1 = radians(lat1)
	#lon1 = radians(lon1)
	#lat2 = radians(lat2)
	#lon2 = radians(lon2)

	dlon = lon2 - lon1
	dlat = lat2 - lat1

	a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
	c = 2 * atan2(sqrt(a), sqrt(1 - a))
	distance = R * c

	return distance
