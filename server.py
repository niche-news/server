from flask import Flask, request


app = Flask(__name__)
db = database()



@app.route('/')
def indexPage():
	return "welcome to nicheNews"

@app.route('/getArticles', methods=['GET', 'POST'])
def getArticles():
	

if __name__ == '__main__':
	app.run(debug=True, port=55622)
