import mysql.connector
import sys, os, json
import FlatFileLoader
from Objects import *
from datetime import date

class database:

	def __init__(self):
        	self.cnx = mysql.connector.connect(user='nicheuser', password='nichepass', host='127.0.0.1', database='NicheNews')
       		self.cursor = self.cnx.cursor()

	def getAllArticles(self, withLimitation, month):
		sqlCommand = ""
		imageSQLCommand = ""
		sourcesSQLCommand = ""

		if withLimitation:
			sqlCommand = "SELECT a.*, c.firstName, c.lastName FROM articles a INNER JOIN contributors c ON a.authorID = c.authorID WHERE MONTH(a.publishDate) = " + str(month)
			imageSQLCommand = "SELECT a.articleID, i.paragraph, i.image FROM articles a INNER JOIN images i ON i.articleID = a.articleID WHERE MONTH(a.publishDate) = " + str(month)
			sourcesSQLCommand = "SELECT a.articleID, s.sourceNumber, s.title, s.source FROM articles a INNER JOIN sources s ON a.articleID = s.articleID WHERE MONTH(a.publishDate) = " + str(month)
		else:
			sqlCommand = "SELECT a.*, c.firstName, c.lastName FROM articles a INNER JOIN contributors c ON a.authorID = c.authorID"
			imageSQLCommand = "SELECT a.articleID, i.paragraph, i.image FROM articles a INNER JOIN images i ON i.articleID = a.articleID" 
			sourcesSQLCommand = "SELECT a.articleID, s.sourceNumber, s.title, s.source FROM articles a INNER JOIN sources s ON a.articleID = s.articleID"

		dict = JSONObject()
		dict.articles = {}
		self.cursor.execute(sqlCommand)
		for (articleID, title, subTitle, text, upvotes, authorID, publishDate, type, fName, lName) in self.cursor:
			newArticle = Article(articleID, title, text, str(publishDate), str(fName) + " " + str(lName), subTitle, upvotes, type)
			dict.articles[articleID] = newArticle

		self.cursor.execute(imageSQLCommand)
		for (id, imgP, img) in self.cursor:
			newImage = JSONObject()
			newImage.image = img
			newImage.imageParagraph = imgP
			dict.articles[id].images.append(newImage)

		self.cursor.execute(sourcesSQLCommand)
		for (id, sNum, sTitle, sSource) in self.cursor:
			newSource = JSONObject()
			newSource.sourceNumber = sNum
			newSource.title = sTitle
			newSource.link = sSource
			dict.articles[id].sources.append(newSource)

		return dict.toJSON()

	def getArticleWithID(self, id):
		sqlCommand = "SELECT a.*, c.firstName, c.lastName FROM articles a INNER JOIN contributors c ON a.authorID = c.authorID WHERE a.articleID = " + str(id)
		self.cursor.execute(sqlCommand)
		
		rows = self.cursor.fetchall()

		if len(rows) == 0:
			return "No Results"

		c = [0]
		for a in rows:
			c = a

		article = Article(c[0], c[1], c[3], str(c[6]), str(c[8]) + " " + str(c[9]), c[2], c[4], c[7])
		imageSQLCommand = "SELECT a.articleID, i.paragraph, i.image FROM articles a INNER JOIN images i ON i.articleID = a.articleID WHERE a.articleID = " + str(id)
		self.cursor.execute(imageSQLCommand)
		for (id, imgP, img) in self.cursor:
			newImage = JSONObject()
			newImage.image = img
			newImage.imageParagraph = imgP
			article.images.append(newImage)
		
		sourcesSQLCommand = "SELECT a.articleID, s.sourceNumber, s.title, s.source FROM articles a INNER JOIN sources s ON a.articleID = s.articleID WHERE a.articleID = " + str(id)
		self.cursor.execute(sourcesSQLCommand)
		for (id, sNum, sTitle, sSource) in self.cursor:
			newSource = JSONObject()
			newSource.sourceNumber = sNum
			newSource.title = sTitle
			newSource.link = sSource
			article.sources.append(newSource)

		jsonData = JSONObject()
		jsonData.article = article
		return jsonData.toJSON()

	def getContributors(self, limit, id):
		sqlCommand = ""
		if limit == "":
			sqlCommand = "SELECT * FROM contributors"	
		else:
			sqlCommand = "SELECT * FROM contributors WHERE " + limit + " = '" + str(id) + "'"

		self.cursor.execute(sqlCommand)
		rows = self.cursor.fetchall()
		if len(rows) == 0:
			return "No Results"

		jsonDict = JSONObject()
		jsonDict.contributors = []

		c = [0]
		for i in rows:
			c = i
			if limit == "":
				contributor = Contributor(c[0], c[1], c[2], c[3], c[4], c[5])
				jsonDict.contributors.append(contributor)

		if limit != "":
			contributor = Contributor(c[0], c[1], c[2], c[3], c[4], c[5])
			jsonDict.contributors.append(contributor)

		return jsonDict.toJSON()

	def addArticle(self, a):
		sqlCommand = "INSERT INTO articles (title, subTitle, text, authorID, upvotes, publishDate, type) VALUES ('" + a.title + "', '" + a.subTitle + "', '" + a.text + "', '" + a.authorName + "', " + str(a.upvotes) + ", " + str(a.date) + ", '" + a.type + "')"
		self.cursor.execute(sqlCommand)
		self.cnx.commit()
		self.cursor.execute("SELECT articleID FROM articles WHERE title = '" + a.title + "'")
		return self.cursor.fetchall()[0][0]

	def addContributor(self, fName, lName, image, possition, bio):
		sqlCommand = "INSERT INTO contributors (firstName, lastName, image, bio, possition) VALUES ('" + fName + "', '" + lName + "', '" + image + "', '" + possition + "', '" + bio + "')"
		self.cursor.execute(sqlCommand)
		self.cnx.commit()
		self.cursor.execute("SELECT authorID FROM contributors WHERE firstName = '" + fName + "'")
		return self.cursor.fetchall()[0][0]

	def addBio(self, id, bio):
		sqlCommand = "UPDATE contributors SET bio = '" + bio + "' WHERE authorID = " + str(id)
		self.cursor.execute(sqlCommand)
		self.cnx.commit()
		return self.getContributors("authorID", id)

