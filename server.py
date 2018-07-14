from flask import Flask, request
from database import *

app = Flask(__name__)
db = database()

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

@app.route('/getArticle', methods=['POST'])
def getArticleWithIDPostMethod():
	if 'id' in request.form:
		return(db.getArticleWithID(request.form['id']))
	else:
		return str(db.getAllArticles(False, ""))



@app.route('/getArticles/month/<int:month>', methods=['GET'])
def getArticleFromMonth(month):
	data = db.getAllArticles(True, month)
	return str(data)

@app.route('/getArticlesFromMonth', methods=['POST'])
def getArticleFromMonthPostMethod():
	data = db.getAllArticles(True, request.form['month'])
	return str(data)



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
	if 'title' not in f or 'text' not in f or 'date' not in f or 'authorID' not in f:
		return "Please make sure you have 'text', 'title', 'date', and 'authorID' as args"
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
	if 'firstName' not in f or 'lastName' not in f or 'image' not in f or 'possition' not in f or 'bio' not in f:
		return "Please make sure you have 'firstName', 'lastName', 'image', 'possition', 'bio'"
	return str(db.addContributor(f['firstName'], f['lastName'], f['image'], f['possition'], f['bio']))

@app.route('/addBio', methods=['POST'])
def addBio():
	f = request.form
	if 'id' not in f or 'bio' not in f:
		return "Please make sure you have 'id' and 'bio' as args"
	return str(db.addBio(f['id'], f['bio']))

if __name__ == '__main__':
	app.run(debug=False, port='55622', host='0.0.0.0')