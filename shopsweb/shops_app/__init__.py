from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///base.db'
app.config['SECRET_KEY'] = '4b9826ffe47fde764229508d00b141d5928b4a27'

db = SQLAlchemy(app)  # our database
bcrypt = Bcrypt(app)  # for generation password_hash for User
login_manager = LoginManager(app)  # It handles the common tasks of logging in, logging out
# and remembering your users’ sessions over extended periods of time

#  set the login view to login page,to avoid the 401 error.
login_manager.login_view = 'login'
#  Customize the login message
login_manager.login_message_category = 'info'
#  to use the zip function : iterate through two lists together on the same time
#app.jinja_env.filters['zip'] = zip

from shops_app import models
from shops_app import routes



