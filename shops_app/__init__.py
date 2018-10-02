from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = '4b9826ffe47fde764229508d00b141d5928b4a27'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///base.db'
db = SQLAlchemy(app) # our database
bcrypt = Bcrypt(app) # for generation password_hash for User

from shops_app import routes



