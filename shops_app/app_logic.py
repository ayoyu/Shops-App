import os
from urllib.request import urlopen
import requests
import math
import sqlite3

#  a Function to get your Public IP (server side)
def get_my_ip():
	my_ip = urlopen('http://ip.42.pl/raw').read()
	my_ip = my_ip.decode('utf-8')
	return my_ip

#  with the IP address we can request some location data from <freegeoip> api
def geo_info():
	my_local_ip = get_my_ip()
	#   go here : https://github.com/apilayer/freegeoip#readme to have your own free API Access Key
	ipstack_key_api = os.environ.get('GEO_KEY')
	#  request some geo_data
	d = requests.get('http://api.ipstack.com/'+str(my_local_ip)+'?access_key='+str(ipstack_key_api)).json()
	latitude, longitude, city, country = d['latitude'], d['longitude'], d['city'], d['country_name']
	return {'latitude': latitude, 'longitude': longitude, city: 'city', 'country': country}


def distance_Euclidienne(Point1, Point2):
	"""
	Point (x,y) tuple, it will be defined by x:longitude and y:latitude
	distance = sqrt((x1 - x2)² + (y1 - y2)²)
	"""
	distance = math.sqrt((Point1[0] - Point2[0])**2 + (Point1[1] - Point2[1])**2)
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
		#  make a custom identification for every shop
		key = ' '.join([str(shop[1]), str(shop[4]), str(shop[5]), str(shop[6])])
		#  calculate the distance between my_point and a shop position
		dist[key] = distance_Euclidienne(Point_shop, my_point)
	#  sorted the dictionary by the distance asc
	nearby = sorted(dist.items(), key=lambda x: x[1])
	return nearby




