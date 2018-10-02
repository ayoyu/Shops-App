from shops_app import db, login_manager, app
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(120), unique=True, nullable=False)
	password = db.Column(db.String(60), nullable=False)
	shops = db.relationship('my_preferred_shops', backref='author', lazy=True)  #one-to-many a user can have a lot of preferred shops

	def __repr__(self):
		return f'User({self.id},{self.email})'

class my_preferred_shops(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(16), nullable=False)
	adress = db.Column(db.String(160), nullable=False)
	city = db.Column(db.String(16))
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

	def __repr__(self):
		return f'My_preferred_Shops({self.name},{self.adress},{self.city})'