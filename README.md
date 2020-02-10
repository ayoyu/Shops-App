# Nearby Optic Shops Application

Implementing an app that lists shops nearby with the Stack
Flask+Uwsgi+Nginx+docker+docker-compose+Postgresql+Bootstrap

### Logic Application :
the Application consist of give you the optic shops nearby, rely on the User public IP address.

**(you will find the explanation in the *app_logic.py* Script)**

for the calculation of the distance between two points in the earth based on the longitude and the latitude.I chose to work with Haversine distance

https://en.wikipedia.org/wiki/Haversine_formula 

https://andrew.hedges.name/experiments/haversine/

### Construction the Shops DATABASE : 
- [x] Construction of our Shops Database *base.db*.

I chose to construct my *Shops.db* basing on the information delivered by: https://kodaklens.ma/Admin/data, So i'm not responsible on the states of this data (About the latitude and Longitude of any shop) 

### Appilication :
- [x] Construction the Models (*User* and *my_prefrred_shops*) and Forms (*login* and *Registration* forms).
- [x] As a User, I can sign up using my email & password
- [x] As a User, I can sign in using my email & password and chose the *remember Me* Option,for the reason that i can sign in the next time without taping my password
- [x] As a User, I can like a shop, so it can be added to my preferred shops and also liked shops shouldn’t be displayed on the main page
- [x] As a User, I can dislike a shop, so it won’t be displayed within “Nearby Shops” list 
- [x] As a User, I can display the list of preferred shops
- [x] As a User, I can remove a shop from my preferred shops list
- [x] As a User, I can search a shop by his name or address or city or his Email

### Built With :
- Python 3.6.x
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [Bootstrap](https://getbootstrap.com/)
- [docker](https://www.docker.com/) && [docker-compose](https://docs.docker.com/compose/)
- [Uwsgi](https://uwsgi-docs.readthedocs.io/en/latest/)
- [Nginx](https://www.nginx.com/)
- [Postgresql](https://www.postgresql.org/)

### Requirements :
- Need to Install:
	- [docker](https://docs.docker.com/v17.09/engine/installation/#updates-and-patches)
	- [docker-compose](https://docs.docker.com/compose/install/) 

### Test in your localhost (http://localhost:8083/): 

- step 1: 
```
$ git clone https://github.com/ayoyu/Shops-App
```
- step2 (build the services): 

```
$ docker-compose build
```
- step 3 (launch the services):
```
$ docker-compose up -d
```
- step 4 (make sure the services are UP):
```
$ docker-compose ps

   Name            Command          State          Ports        
----------------------------------------------------------------
shopsnginx   nginx -g daemon off;   Up      0.0.0.0:8083->80/tcp
shopsweb     uwsgi shops_app.ini    Up      8080/tcp            

```
- step 5 (create tables for the database server)
```
$ docker-compose exec shopsweb python manage.py create_db
```
- step 6 (make sure tables are created):
```
$ docker exec -it shopsdb psql -U postgres

postgres=# \conninfo
You are connected to database "postgres" as user "postgres" via socket in "/var/run/postgresql" at port "5432".
postgres=# \c shops
You are now connected to database "shops" as user "postgres".
shops=# \dt
               List of relations
 Schema |        Name        | Type  |  Owner   
--------+--------------------+-------+----------
 public | my_preferred_shops | table | postgres
 public | user               | table | postgres
(2 rows)

```

### Authors :
 
- **Ayoub El khallioui**
- Email : khaliayoub9@gmail.com