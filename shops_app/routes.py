from shops_app import app, bcrypt, db
from flask import render_template, redirect, url_for, flash
from shops_app.Forms import RegistrationForm, LoginForm
from flask_login import current_user, login_user, logout_user
from shops_app.models import User

@app.route('/home', methods=['GET', 'POST'])
def home():
	return render_template('home.html', title='Home')

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





