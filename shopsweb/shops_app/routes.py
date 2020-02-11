import os
from shops_app import app, bcrypt, db
from flask import render_template, redirect, url_for, flash, request
from shops_app.Forms import RegistrationForm, LoginForm
from flask_login import current_user, login_user, logout_user, login_required
from shops_app.models import User, my_preferred_shops
from shops_app.app_logic import Neraby_Shops
import sqlite3


@app.route('/home', methods=['GET', 'POST'])
#  this decoration ensure that the current user is logged in and authenticated before calling the actual home page
@login_required
def home():
	nearby = Neraby_Shops()
	return render_template('home.html', title='Home', nearby=nearby)


# Making the Registration Form as the index Page for the App
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
		#  add the user to the database
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
		#  checkout if the user is already exists, by the email ans the password
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
	# the search option for a specific shop will be by his name or his address
	shop_searched = c.execute('SELECT * FROM Shops WHERE name=? or adresse=? or city=? or Email=?', (item_search, item_search, item_search, item_search)).fetchone()
	if not shop_searched:
		flash(f"Sorry!!! we don't found {item_search} in our Database", 'danger')
		return redirect(url_for('home'))
	return render_template('search.html', title='Search' ,search=shop_searched)


nearby_liked = Neraby_Shops()
@app.route('/Like/<int:shop_id>', methods=['GET', 'POST'])
def Like(shop_id):
	current_dir = os.path.dirname(__file__)
	path_to_base = os.path.join(current_dir, 'Shops_DataBase', 'shops.db')
	conn = sqlite3.connect(path_to_base)
	c = conn.cursor()
	# query the database based on the shop id liked by the current user
	liked_shop = c.execute('SELECT * FROM Shops WHERE id=?',(shop_id,)).fetchone()
	# filter the table by the name (the name is unique column)
	exit_in_database = my_preferred_shops.query.filter_by(name=liked_shop[1], author=current_user).first()
	# checkout if the shop is already in my_preferred_shops table
	if exit_in_database:
		flash('This shop is already exist in your Preferred Shops','danger')
	else:
		preferred_shop = my_preferred_shops(name=liked_shop[1],
											address=liked_shop[4],
											city=liked_shop[5],
											email=liked_shop[6],
											author=current_user)
		db.session.add(preferred_shop)
		db.session.commit()
		flash('The Shop has been added to your Preferred Shops', 'success')
	for item in nearby_liked:
		if item[1][1] == shop_id:
			nearby_liked.remove(item)
	return render_template('Like.html', nearby=nearby_liked)


@app.route('/PreferredShops')
def Preferred_Shops():
	page = request.args.get('page', 1, type=int)
	Shops = my_preferred_shops.query.filter_by(user_id=current_user.id).paginate(page=page, per_page=3)
	return render_template('my_preferred_shops.html',title='Preferred Shops',Shops=Shops)


@app.route('/Removed/<int:removed_id>',methods=['GET', 'POST'])
def Remove(removed_id):
	removed_shop = my_preferred_shops.query.get(removed_id)
	db.session.delete(removed_shop)
	db.session.commit()
	flash('The Shop has been deleted from your Preferred Shops','success')
	return redirect(url_for('Preferred_Shops'))


nearby_disliked = Neraby_Shops()
@app.route('/Dislike/<int:shop_id>')
def Dislike(shop_id):
	for item in nearby_disliked:
		if item[1][1] == shop_id:
			nearby_disliked.remove(item)

	return render_template('Dislike.html', nearby=nearby_disliked)