import os
import sqlite3
from shops_app import app, bcrypt, db
from flask import render_template, redirect, url_for, flash, request
from shops_app.Forms import RegistrationForm, LoginForm
from flask_login import current_user, login_user, logout_user
from shops_app.models import User
from shops_app.app_logic import Neraby_Shops

@app.route('/home', methods=['GET', 'POST'])
def home():
	"""
	>>> ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
	
	provide the IP User address but in the localhost you will get 127.0.0.1, not helpful
	so to provide the result and see the final app, i will work with the local IP
	but in the production we must change our Public IP by the Client IP,then request the Freegeo api
	to have some geo_information about the User (latitude, longitude,...):

	>>> requests.get('http://api.ipstack.com/'+str(ip)+'?access_key=YOUR_KEY_API').json()
	
	"""

	nearby = Neraby_Shops()

	return render_template('home.html', title='Home', nearby=nearby)

#  I make the Registration Form as the index Page for the App
@app.route('/', methods=['GET', 'POST'])
def Registration():
	#  checkout if the user is already autenticated
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = RegistrationForm()
	if form.validate_on_submit():
		# generation password_hash for a new User
		hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user = User(email=form.email.data, password=hashed_password)
		#  add this user into base.db
		db.session.add(user)
		db.session.commit()
		flash('Your Acoount has been created!.Your now able to login','success')
		return redirect(url_for('login'))
	return render_template('register.html', form=form, title='Register')

@app.route('/login', methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		#  checkout if the user is already in database by the email ans the password
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			login_user(user, remember=form.remember.data)
			return redirect(url_for('home'))
		else:
			flash('Login Unsuccessful. Please check Email and password','danger')
	return render_template('login.html', form=form, title='Login')

@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('login'))





