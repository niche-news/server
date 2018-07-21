from flask import Flask, request
from database import *
import hashlib

app = Flask(__name__)
db = database()

import logging
logging.basicConfig(filename='error.log',level=logging.DEBUG)
open('error.log', 'w').close()

def authenticate(passWord):
	passwordFile = open('pass.txt', 'r')
	return hashlib.sha256(passWord.encode()).hexdigest() == passwordFile.readline()

@app.route('/')
def indexPage():
	return "welcome to nicheNews"

@app.route('/getArticles', methods=['GET'])
def getArticles():
	data = db.getAllArticles(False, "")
	return str(data)

@app.route('/getArticle/id/<int:articleID>', methods=['GET'])
def getArticleWithID(articleID):
	data = db.getArticleWithID(articleID)
	return str(data)

@app.route('/getArticles/month/<int:month>', methods=['GET'])
def getArticleFromMonth(month):
	data = db.getAllArticles(True, month)
	return str(data)

@app.route('/getArticle', methods=['POST'])
def getArticleWithIDPostMethod():
	if 'id' in request.form:
		return(db.getArticleWithID(request.form['id']))
	elif 'month' in request.form:
		return(db.getAllArticles(True, request.form['month']))
	else:
		return str(db.getAllArticles(False, ""))


@app.route('/getContributors', methods=['GET','POST'])
def getContributors():
	if request.method == 'GET':
		return str(db.getContributors("", ""))
	else:
		if 'id' in request.form:
			return str(db.getContributors("authorID", request.form['id']))
		elif 'firstName' in request.form:
			return str(db.getContributors("firstName", request.form['firstName']))
		elif 'lastName' in request.form:
			return str(db.getContributors("lastName", request.form['lastName']))
		else:
			return str(db.getContributors("", ""))			


@app.route('/getContributors/id/<int:id>')
def getContributorsWithID(id):
	return str(db.getContributors("authorID", id))

@app.route('/getContributors/firstName/<firstName>')
def getContributorsWithFirstName(firstName):
	return str(db.getContributors("firstName", firstName))

@app.route('/getContributors/lastName/<lastName>')
def getContributorsWithLastName(lastName):
	return str(db.getContributors("lastName", lastName))

@app.route('/uploadArticle', methods=['POST'])
def uploadArticle():
	f = request.form

	if 'pass' not in f:
		return "Please use the password"
	
	if not authenticate(f['pass']):
		return "Incorrect Password"

	if 'title' not in f or 'text' not in f or 'date' not in f or 'authorID' not in f:
		return "Please make sure you have 'text', 'title', 'date', and 'authorID' as args optional: ('subTitle', 'type')"
	article = Article.init(f['title'], f['text'], f['authorID'], f['date'])
	if 'subTitle' in f:
		print(f['subTitle'])
		article.subTitle = f['subTitle']
	if 'type' in f:
		article.type = f['type']
	return str(db.addArticle(article))

@app.route('/addContributor', methods=['POST'])
def addContributors():
	f = request.form

	if 'pass' not in f:
		return "Please use the password"
	
	if not authenticate(f['pass']):
		return "Incorrect Password"

	if 'firstName' not in f or 'lastName' not in f or 'image' not in f or 'position' not in f:
		return "Please make sure you have 'firstName', 'lastName', 'image', and 'position' as args"
	return str(db.addContributor(f['firstName'], f['lastName'], f['image'], f['position']))

@app.route('/addBio', methods=['POST'])
def addBio():
	f = request.form

	if 'pass' not in f:
		return "Please use the password"
	
	if not authenticate(f['pass']):
		return "Incorrect Password"

	if 'id' not in f or 'bio' not in f:
		return "Please make sure you have 'id' and 'bio' as args"
	return str(db.addBio(f['id'], f['bio']))

@app.route('/addImage', methods=['POST'])
def addImage():
	f = request.form

	if 'pass' not in f:
		return "Please use the password"
	
	if not authenticate(f['pass']):
		return "Incorrect Password"

	if 'articleID' not in f or 'image' not in f:
		return "Please make sure you have 'articleID' and 'image' as args optional: ('paragraph')"
	image = Image(f['articleID'], f['image'])
	if 'paragraph' in f:
		image.paragraph = f['paragraph']
	return str(db.addImage(image))

@app.route('/addSource', methods=['POST'])
def addSource():
	f = request.form

	if 'pass' not in f:
		return "Please use the password"
	
	if not authenticate(f['pass']):
		return "Incorrect Password"

		
	if 'articleID' not in f or 'sourceNumber' not in f:
		return "Please make sure you have 'articleID' and 'sourceNumber' as args with at least one of: ('title', 'link')"
	source = Source(f['articleID'], f['sourceNumber'])
	if 'title' in f and 'link' in f:
		source.title = f['title']
		source.link = f['link']
	elif 'link' in f:
		source.link = f['link']
	elif 'title' in f:
		source.title = f['title']
	else:
		return "Please make sure you have 'articleID' and 'sourceNumber' as args with at least one of: ('title', 'link')"
	return str(db.addSource(source))

if __name__ == '__main__':
	app.run(debug=True, port='55622', host='0.0.0.0')
