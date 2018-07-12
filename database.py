import mysql.connector
import sys, os, json
from Objects import *
from datetime import date

class database:

	def __init__(self):
        	self.cnx = mysql.connector.connect(user='nicheuser', password='nichepass', host='127.0.0.1', database='NicheNews')
       		self.cursor = self.cnx.cursor()

	def getAllArticles(self):
		sqlCommand = "SELECT articleID, title, text, subTitle, publishDate, image, upvotes, type FROM articles"
		self.cursor.execute(sqlCommand)
		dict = JSONObject()
		dict.articles = []
		for (articleID, title, text, subTitle, publishDate, image, upvotes, type) in self.cursor:
			newArticle = Article(articleID, title, text, str(publishDate))
			newArticle.updateWith(subTitle, image, upvotes, type)
			dict.articles.append(newArticle)
		return dict.toJSON()

	def getArticleWith(self, id):
		sqlCommand = "SELECT "
