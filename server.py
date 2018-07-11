from flask import Flask, request
import mysql.connector
import json

app = Flask(__name__)

cnx = mysql.connector.connect(user='nicheuser', password='nichepass', host='127.0.0.1', database='NicheNews')
cursor = cnx.cursor()


@app.route('/')
def indexPage():
	return "welcome to nicheNews"

@app.route('/getArticles', methods=['GET', 'POST'])
def getArticles():
	cursor.execute("SET @J = json_object('title', title, 'text', text)")
	#cursor.execute("SELECT @J FROM articles")
	#cursor.execute("SELECT 'title', title, 'text', text FROM articles")
	#cursor.execute("SELECT JSON_OBJECT ( KEY 'ID' IS articleID FORMAT JSON, KEY 'title' IS title FORMAT JSON, KEY 'text' IS text FORMAT JSON) 'articles'  FROM articles")
	data = cursor.fetchall()
	#print(json.dumps(data))
	return str(data)

if __name__ == '__main__':
	app.run(debug=True, port=55622)
