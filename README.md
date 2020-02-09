# Optic-Shops-App

implementing an app that lists shops nearby.

### Logic Application :
the Application consist of give you the optic shops nearby,rely on your local public IP address.

but in production we must change that local IP address by the User public IP.

the Problem that in the development phase if we work with the Client IP, the result will give us always 127.0.0.1 because we are behind a proxy.
  

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
- Flask - The web framework used.
- Bootstrap - front-end framework. https://getbootstrap.com/

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
### TO DO:
- Create a Posgresql service for the database server instead of using SQLite

### Authors :
 
- **Ayoub El khallioui**
- Email : khaliayoub9@gmail.com