import requests
import sqlite3

data = requests.get('https://kodaklens.ma/Admin/data').json() # Some Shops data in our country
conn = sqlite3.connect('shops.db') # make the connection to Shops.db
c = conn.cursor()

def build_table():
	c.execute('CREATE TABLE IF NOT EXISTS Shops(id INTEGER PRIMARY KEY,'
			  'name TEXT ,longitude FLOAT not null,'
			  'latitude FLOAT not null,'
			  'adresse TEXT,city TEXT,Email TEXT)') # Create the Shops Table
	conn.commit()

def insert_into():
	for shop in data:
		try:
			c.execute('INSERT INTO Shops VALUES (?,?,?,?,?,?,?)', (int(shop['id']), shop['nom'],
																   float(shop['longitude']),
																   float(shop['latitude']),
																   shop['Adresse'],
																   shop['ville'],
																   shop['email'])) # inserto into the Shops Table the values in the list data
			conn.commit()
		except:
			continue
	return True

if __name__ == '__main__':
	build_table()
	insert_into()


