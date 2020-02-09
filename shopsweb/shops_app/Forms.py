from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, length, EqualTo, ValidationError
from shops_app.models import User

class RegistrationForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password',validators=[DataRequired(), length(min=5, max=30)])
	confirm_password = PasswordField('Comfirm password', validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Sign Up')
	def validate_email(self, email):
		user = User.query.filter_by(email=email.data).first()
		if user:
			raise ValidationError('This Email is already exit!Please Chose a diffrent one')


class LoginForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired(), length(min=5, max=30)])
	remember = BooleanField('Remember Me')
	submit = SubmitField('Sign In')
