from shops_app import db, login_manager, app
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))


class User(db.Model, UserMixin):
	"""
	inherit from UserMixin, which provides default implementations for all of these properties and methods:
		is_authenticated : This property should return True if the user is authenticated
		is_active : This property should return True if this is an active user
		is_anonymous : This property should return True if this is an anonymous user. (Actual users should return False instead)
		get_id() : This method must return a unicode that uniquely identifies this user, and can be used to load the user
					from the user_loader callback
	"""
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(120), unique=True, nullable=False)
	password = db.Column(db.String(60), nullable=False)
	# one-to-many a user can have a lot of preferred shops
	shops = db.relationship('my_preferred_shops', backref='author', lazy=True)

	
	def __repr__(self):
		return f'User({self.id},{self.email})'


class my_preferred_shops(db.Model):

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(30), nullable=False)
	address = db.Column(db.String(160), nullable=False)
	city = db.Column(db.String(16))
	email = db.Column(db.String(120))
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

	
	def __repr__(self):
		return f'My_preferred_Shops({self.name},{self.address},{self.city})'