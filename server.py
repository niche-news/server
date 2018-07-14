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
	print(request.form)
	print(request.form.to_dict())
	if 'lol' in request.form:
		print(request.form['lol'])
	data = db.getArticleWithID(request.form['id'])
	return str(data)



@app.route('/getArticles/month/<int:month>', methods=['GET'])
def getArticleFromMonth(month):
	data = db.getAllArticles(True, month)
	return str(data)

@app.route('/getArticleFromMonth', methods=['POST'])
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

if __name__ == '__main__':
	app.run(debug=False, port='55622', host='0.0.0.0')