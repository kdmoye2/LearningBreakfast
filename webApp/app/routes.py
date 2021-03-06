from flask import render_template, flash, redirect, request, url_for
from app import app, dbAccess
from app.forms import LoginForm
from app.models import User

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
	form = LoginForm()
	print "here I am"
	if (request.args.get('search')):
		#call search method
		firstName = request.args.get('firstname')
		searchResults = dbAccess.Search(firstName)
		print "in routes, users are", searchResults
		return redirect(url_for('search'))
	elif (request.args.get('add')):
		firstName = request.args.get('firstname')
		lastName = request.args.get('lastname')
		EMail = request.args.get('email')
		#call add method
		dbAccess.Add(firstName, lastName, EMail)
		return render_template('index.html', form=form)
	elif (request.args.get('delete')):
		#call delete method
		print "in delete"
	else:
		print "you suck"
		return render_template('index.html', form=form)

@app.route('/search', methods=['GET', 'POST'])
def search():
	print "in search routes"
	firstName = request.args.get('firstname') 
	lastName = request.args.get('lastname') 
	email = request.args.get('email') 
	searchResults = dbAccess.Search(firstName, lastName, email)
	for u in searchResults:
		print(u.id, u.firstname, u.lastname, u.email)
	print "in routes, users are", searchResults
	return render_template('search.html', searchResults=searchResults)

@app.route('/add', methods=['GET', 'POST'])
def add():
        form = LoginForm()
	print "in add routes"
        if (request.args.get('add')):
		firstName = request.args.get('firstname') 
		lastName = request.args.get('lastname') 
		email = request.args.get('email') 
		dbAccess.Add(firstName, lastName, email)
		flash('user added')
		return redirect(url_for('index'))
	#for u in searchResults:
	#	print(u.id, u.firstname, u.lastname, u.email)
	#print "in routes, users are", searchResults
	return render_template('add.html', form=form)

        #if form.validate_on_submit():
#	print request.args.get('firstname')
#	print form.firstname
#	print request.args.get('lastname')
#	print request.args.get('email')
#	print request.args.get('search')
#	print request.args.get('delete')
#	print request.args.get('add')
#		print "first name queried : {value}".format(value=form.firstname.data)
#		query = User.query.filter_by(firstname=form.firstname.data).first()
#		print query
#		if query is None:
#			flash('record does not exist')
#			return redirect(url_for('index'))
#	else:
#		print "you suck"
#	return render_template('index.html', form=form)


#@app.route('/search', methods=['GET', 'POST'])
#def search:
#	form = LoginForm()
#	if form.validate_on_submit():
#		print "first name queried : {value}".format(value=form.firstname.data)
#
#	return render_template('index.html', form=form)
