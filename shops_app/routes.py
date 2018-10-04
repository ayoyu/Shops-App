import os
from shops_app import app, bcrypt, db
from flask import render_template, redirect, url_for, flash, request
from shops_app.Forms import RegistrationForm, LoginForm
from flask_login import current_user, login_user, logout_user, login_required
from shops_app.models import User
from shops_app.app_logic import Neraby_Shops
import sqlite3

@app.route('/home', methods=['GET', 'POST'])
#  this decoration ensure that the current user is logged in and authenticated before calling the actual home page
@login_required
def home():

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
			next_page = request.args.get('next')
			return redirect(next_page) if next_page else redirect(url_for('home'))
		else:
			flash('Login Unsuccessful. Please check Email and password','danger')
	return render_template('login.html', form=form, title='Login')

@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('login'))


@app.route('/search', methods=['GET'])
def search():
	item_search = request.args.get('item')
	current_dir = os.path.dirname(__file__)
	path_to_base = os.path.join(current_dir,'Shops_DataBase','shops.db')
	conn = sqlite3.connect(path_to_base)
	c = conn.cursor()
	#  the search option for a specific shop will be by his name or his address
	query = c.execute('SELECT * FROM Shops WHERE name=? or adresse=?',(item_search, item_search)).fetchall()
	return render_template('search.html', title='Search' ,search=query)


