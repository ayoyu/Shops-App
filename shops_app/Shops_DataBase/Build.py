import requests
import sqlite3

"""
Some Optic Shops data in Morrocco with geo_data(latitude, longitude...)
I am not responsible on the states of this data (About the latitude and Longitude of any shop)
I chose it just for the demonstration

"""
data = requests.get('https://kodaklens.ma/Admin/data').json()
# make the connection to Shops.db
conn = sqlite3.connect('shops.db')
c = conn.cursor()

def build_table():
	# Create the Shops Table
	c.execute('CREATE TABLE IF NOT EXISTS Shops(id INTEGER PRIMARY KEY,'
			  'name TEXT ,longitude FLOAT not null,'
			  'latitude FLOAT not null,'
			  'adresse TEXT,city TEXT,Email TEXT)')
	conn.commit()

def insert_into():
	for shop in data:
		try:
			#  insert into the Shops Table the values in the list data
			c.execute('INSERT INTO Shops VALUES (?,?,?,?,?,?,?)', (int(shop['id']),
																   shop['nom'],
																   float(shop['longitude']),
																   float(shop['latitude']),
																   shop['Adresse'],
																   shop['ville'],
																   shop['email']))
			conn.commit()
		except KeyError:
			continue
	return True

if __name__ == '__main__':
	build_table()
	insert_into()


