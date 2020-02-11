import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from dotenv import load_dotenv


current_dir = os.path.realpath(os.path.dirname(__file__))
env_path = os.path.join(current_dir, '../.env')
load_dotenv(env_path)
app = Flask(__name__)
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_DB = os.getenv('POSTGRES_DB')
HOST = os.getenv('HOST')
PORT = os.getenv('PORT')
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{HOST}:{PORT}/{POSTGRES_DB}'
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

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