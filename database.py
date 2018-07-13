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
		sqlCommand = "SELECT a.*, c.firstName, c.lastName FROM articles a INNER JOIN contributors c ON a.authorID = c.authorID"
		dict = JSONObject()
		dict.articles = {}
		self.cursor.execute(sqlCommand)
		for (articleID, title, subTitle, text, upvotes, authorID, publishDate, type, fName, lName) in self.cursor:
			newArticle = Article(articleID, title, text, str(publishDate), str(fName) + " " + str(lName), subTitle, upvotes, type)
			newArticle.images = []
			newArticle.sources = []
			dict.articles[articleID] = newArticle

		imageSQLCommand = "SELECT a.articleID, i.paragraph, i.image FROM articles a INNER JOIN images i ON i.articleID = a.articleID" 
		self.cursor.execute(imageSQLCommand)
		for (id, imgP, img) in self.cursor:
			newImage = JSONObject()
			newImage.image = img
			newImage.imageParagraph = imgP
			dict.articles[id].images.append(newImage)

		sourcesSQLCommand = "SELECT a.articleID, s.sourceNumber, s.title, s.source FROM articles a INNER JOIN sources s ON a.articleID = s.articleID"
		self.cursor.execute(sourcesSQLCommand)
		for (id, sNum, sTitle, sSource) in self.cursor:
			newSource = JSONObject()
			newSource.sourceNumber = sNum
			newSource.title = sTitle
			newSource.link = sSource
			dict.articles[id].sources.append(newSource)

		return dict.toJSON()

	def getArticleWithID(self, id):
		pass
		# sqlCommand = "SELECT * FROM articles WHERE articleID = '" + id + "'"
		# self.cursor.execute(sqlCommand)


	def loadContributors(self):
		pass
		# FlatFileLoader.loadContributors()
