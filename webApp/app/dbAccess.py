from app.models import User
from app import db

def Search(firstname="", lastname="", email=""):
	users = 0
	print firstname
        if firstname != "":
		users = User.query.filter_by(firstname=firstname)
        elif lastname != "":
		users = User.query.filter_by(lastname=lastname)
        elif email != "":
		users = User.query.filter_by(email)
	else:
		users = User.query.all()
	#users = User.query.all()
	print "my users are ", users
	return users	

def Add(firstName, lastName, eMail):
	print "in add and lastname = ", lastName, " and firstName = ", firstName , " and eMail = ", eMail
	u = User()
	u.firstname = firstName
	u.lastname = lastName
	u.email = eMail
	db.session.add(u)
	db.session.commit()

#def Delete(firstname, lastname, email):
