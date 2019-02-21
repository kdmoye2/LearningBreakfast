from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
	firstname = StringField('First Name')
	lastname = StringField('Last Name')
	email = StringField('Email')
	search = SubmitField('Search')
	add = SubmitField('Add')
	delete = SubmitField('Delete')
