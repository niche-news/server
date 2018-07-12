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
		for (articleID, title, text, publishDate) in self.cursor:
			newArticle = Article(articleID, title, text, str(publishDate.date()))
			arr.append(newArticle.toJSON())
		return json.dumps(arr)

	def getArticleWith(self, id):
		sqlCommand = "SELECT "
