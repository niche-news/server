import mysql.connector
import json
from Objects import *
from datetime import date

class database:

	def __init__(self):
        	self.cnx = mysql.connector.connect(user='nicheuser', password='nichepass', host='127.0.0.1', database='NicheNews')
       		self.cursor = self.cnx.cursor()

	def getAllArticles(self):
		sqlCommand = "SELECT articleID, title, text, publishDate FROM articles"
		self.cursor.execute(sqlCommand)
		arr = []
		#data = self.cursor.fetchall()
		for (articleID, title, text, publishDate) in self.cursor:
			#print('id: ' + str(articleID) + " title: " + str(title) + " text: " + str(text) + " date: " + str(publishDate))
			newArticle = Article(articleID, title, text, str(publishDate.date()))
			arr.append(newArticle.toJSON())
		#print(data)
		#return str(data)
		return json.dumps(arr)
