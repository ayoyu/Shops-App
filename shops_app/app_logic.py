import os
import requests
from math import sin, cos, sqrt, atan2, radians
import sqlite3
import ipgetter

"""
a Function to get your Public IP (server side)
ipgetter module : picks your IP randomly from a server list to minimize request overhead on a single server.
				  https://github.com/phoemur/ipgetter
"""
def get_my_ip():
	my_ip = ipgetter.myip()
	return my_ip

"""
The production method to get the User Public IP:

	from flask import request
		
	>>> ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
	
	provide the IP User address but in the localhost you will get 127.0.0.1, not helpful
	so to provide the result and see the final app, i will work with the local IP
	but in the production we must change our Public IP by the Client IP (By changing the get_my_ip function)
	then request the Freegeo api to have some geo_information about the User (latitude, longitude,...):
	
	>>> requests.get('http://api.ipstack.com/'+str(ip)+'?access_key=YOUR_KEY_API').json()

"""
#  with the IP address we can request some location data from <freegeoip> api
def geo_info():
	my_local_ip = get_my_ip()
	#   go here : https://github.com/apilayer/freegeoip#readme to have your own free API Access Key
	#ipstack_key_api = os.environ.get('GEO_KEY')
	#  request some geo_data that contain (latitude,longitude,...)
	d = requests.get('http://api.ipstack.com/'+str(my_local_ip)+'?access_key=51c91e768ef431fd90283b4da4739e91').json()
	latitude, longitude, city, country = d['latitude'], d['longitude'], d['city'], d['country_name']
	return {'latitude': latitude, 'longitude': longitude, city: 'city', 'country': country}


def haversine_distance(Point1, Point2):
	"""
	Point (x,y) tuple, it will be defined by x:longitude and y:latitude
	This uses the ‘haversine’ formula to calculate the great-circle distance between two points – that is
	the shortest distance over the earth’s surface.
	https://en.wikipedia.org/wiki/Haversine_formula
	https://andrew.hedges.name/experiments/haversine/
	a = sin²(Δφ/2) + cos φ1 ⋅ cos φ2 ⋅ sin²(Δλ/2)
	c = 2 ⋅ atan2( √a, √(1−a) )
	d = R ⋅ c
	R = 6373 km : The value used for the radius of the Earth
	"""
	R = 6373
	lat1 = radians(Point1[1])
	lat2 = radians(Point2[1])
	dlong = radians(Point2[0] - Point1[0])
	dlat = lat2 - lat1
	a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlong/2)**2
	c = 2 * atan2(sqrt(a), sqrt(1 - a))
	distance = R * c
	return distance

def Neraby_Shops():
	#  get my position ( local IP )
	my_position = geo_info()
	current_dir = os.path.dirname(__file__)
	shops_base_path = os.path.join(current_dir, 'Shops_DataBase', 'shops.db')
	#  make a connection to shops.db
	conn = sqlite3.connect(shops_base_path)
	c = conn.cursor()
	cursor_iterator = c.execute('SELECT * FROM Shops')
	dist = {}
	my_point = (my_position['longitude'], my_position['latitude'])
	for shop in cursor_iterator:
		Point_shop = (shop[2], shop[3])
		#  index: 1=> name  4=> address  5=> city  6=> Email
		key = ' '.join([str(shop[1]), str(shop[4]), str(shop[5]), str(shop[6])])
		#  calculate the distance between my_point and a shop position
		dist[key] = (round(haversine_distance(Point_shop, my_point),2),shop[0])
	#  sorted the dictionary by the distance asc
	nearby = sorted(dist.items(), key=lambda x: x[1][0])
	return nearby




