from flask import Flask, request
from database import *

app = Flask(__name__)
db = database()



@app.route('/')
def indexPage():
	return "welcome to nicheNews"

@app.route('/getArticles', methods=['GET', 'POST'])
def getArticles():
	data = db.getAllArticles()
	return str(data)

if __name__ == '__main__':
	app.run(debug=True, port=55622)
