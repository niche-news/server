import mysql.connector
import sys, os, json
import FlatFileLoader
from Objects import *
from datetime import date

class database:

	def __init__(self):
        	self.cnx = mysql.connector.connect(user='nicheuser', password='nichepass', host='127.0.0.1', database='NicheNews')
       		self.cursor = self.cnx.cursor()

	def getAllArticles(self):
		sqlCommand = "SELECT * FROM articles"
		self.cursor.execute(sqlCommand)
		dict = JSONObject()
		dict.articles = []
		for (articleID, title, subTitle, text, image, upvotes, authorID, publishDate, type) in self.cursor:
			newArticle = Article(articleID, title, text, str(publishDate))
			newArticle.updateWith(subTitle, image, upvotes, type)
			dict.articles.append(newArticle)
		return dict.toJSON()

	def getArticleWithID(self, id):
		sqlCommand = "SELECT * FROM articles WHERE articleID = '" + id + "'"
		# self.cursor.execute(sqlCommand)


	def loadContributors(self):
		FlatFileLoader.loadContributors()