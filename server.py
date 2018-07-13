from flask import Flask, request
from database import *

app = Flask(__name__)
db = database()



@app.route('/')
def indexPage():
	return "welcome to nicheNews"

@app.route('/getArticles', methods=['GET'])
def getArticles():
	data = db.getAllArticles()
	return str(data)

if __name__ == '__main__':
	app.run(debug=False, port='55622', host='0.0.0.0')
	

