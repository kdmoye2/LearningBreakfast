from app import db

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	firstname = db.Column(db.String(64), index=True, unique=False)
	lastname = db.Column(db.String(64), index=True, unique=False)
	email = db.Column(db.String(120), index=True, unique=False)

	def __repr__(self):
		return '<User {}>'.format(self.firstname)
