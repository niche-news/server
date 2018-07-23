import mysql.connector
import sys, os, json
import FlatFileLoader
from Objects import *
from datetime import date

class database:

	def connect(self):
		self.cnx = mysql.connector.connect(user='nicheuser', password='nichepass', host='127.0.0.1', database='NicheNews')
		self.cursor = self.cnx.cursor()

	def __init__(self):
		self.connect()

	def getAllArticles(self, withLimitation, limit, value):
		self.connect()
		sqlCommand = ""
		imageSQLCommand = ""
		sourcesSQLCommand = ""

		if withLimitation:
			sqlCommand = "SELECT a.*, c.firstName, c.lastName, c.authorID FROM articles a INNER JOIN contributors c ON a.authorID = c.authorID WHERE " + limit + " = " + str(value)
			imageSQLCommand = "SELECT a.articleID, i.paragraph, i.image FROM articles a INNER JOIN images i ON i.articleID = a.articleID WHERE " + limit + " = " + str(value)
			sourcesSQLCommand = "SELECT a.articleID, s.sourceNumber, s.title, s.source FROM articles a INNER JOIN sources s ON a.articleID = s.articleID WHERE " + limit + " = " + str(value)
		else:
			sqlCommand = "SELECT a.*, c.firstName, c.lastName FROM articles a INNER JOIN contributors c ON a.authorID = c.authorID"
			imageSQLCommand = "SELECT a.articleID, i.paragraph, i.image FROM articles a INNER JOIN images i ON i.articleID = a.articleID" 
			sourcesSQLCommand = "SELECT a.articleID, s.sourceNumber, s.title, s.source FROM articles a INNER JOIN sources s ON a.articleID = s.articleID"
		dict = JSONObject()
		dict.articles = {}
		self.cursor.execute(sqlCommand)
		for (articleID, title, subTitle, text, upvotes, authorID, publishDate, type, fName, lName, authorID) in self.cursor:
			newArticle = Article(articleID, title, text, str(publishDate), str(fName) + " " + str(lName), subTitle, upvotes, type, authorID)
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
		self.connect()
		sqlCommand = "SELECT a.*, c.firstName, c.lastName, c.authorID FROM articles a INNER JOIN contributors c ON a.authorID = c.authorID WHERE a.articleID = " + str(id)
		self.cursor.execute(sqlCommand)
		
		rows = self.cursor.fetchall()

		if len(rows) == 0:
			return "No Results"

		c = [0]
		for a in rows:
			c = a

		article = Article(c[0], c[1], c[3], str(c[6]), str(c[8]) + " " + str(c[9]), c[2], c[4], c[7], c[10])
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
		self.connect()
		sqlCommand = ""
		articleSQLCommand = ""
		if limit == "":
			sqlCommand = "SELECT * FROM contributors"	
			articleSQLCommand = "SELECT a.articleID, c.authorID FROM articles a INNER JOIN contributors c ON a.authorID = c.authorID"
		else:
			sqlCommand = "SELECT * FROM contributors c WHERE " + limit + " = '" + str(id) + "'"
			articleSQLCommand = "SELECT a.articleID, c.authorID FROM articles a INNER JOIN contributors c ON a.authorID = c.authorID WHERE " + limit + " = '" + str(id) + "'"

		self.cursor.execute(sqlCommand)
		rows = self.cursor.fetchall()
		if len(rows) == 0:
			return "No Results"

		jsonDict = JSONObject()
		jsonDict.contributors = {}

		c = [0]
		for i in rows:
			c = i
			if limit == "":
				contributor = Contributor(c[0], c[1], c[2], c[3], c[4], c[5])
				jsonDict.contributors[c[0]] = contributor

		if limit != "":
			contributor = Contributor(c[0], c[1], c[2], c[3], c[4], c[5])
			jsonDict.contributors[c[0]] = contributor

		self.cursor.execute(articleSQLCommand)
		rows = self.cursor.fetchall()

		for i in rows:
			jsonDict.contributors[i[1]].articleIDs.append(i[0])

		return jsonDict.toJSON()

	def addArticle(self, a):
		self.connect()
		sqlCommand = "INSERT INTO articles (title, subTitle, text, authorID, upvotes, publishDate, type) VALUES ('" + a.title + "', '" + a.subTitle + "', '" + a.text + "', '" + a.authorName + "', " + str(a.upvotes) + ", " + str(a.date) + ", '" + a.type + "')"
		self.cursor.execute(sqlCommand)
		self.cnx.commit()
		self.cursor.execute("SELECT articleID FROM articles WHERE title = '" + a.title + "'")
		return self.cursor.fetchall()[0][0]

	def addContributor(self, fName, lName, image, possition):
		self.connect()
		sqlCommand = "INSERT INTO contributors (firstName, lastName, image, possition) VALUES ('" + fName + "', '" + lName + "', '" + image + "', '" + possition + "')"
		self.cursor.execute(sqlCommand)
		self.cnx.commit()
		self.cursor.execute("SELECT authorID FROM contributors WHERE firstName = '" + fName + "'")
		return self.cursor.fetchall()[0][0]

	def addBio(self, id, bio):
		self.connect()
		sqlCommand = "UPDATE contributors c SET bio = '" + bio + "' WHERE c.authorID = " + str(id)
		self.cursor.execute(sqlCommand)
		self.cnx.commit()
		return self.getContributors("c.authorID", id)

	def addImage(self, image):
		self.connect()
		sqlCommand = "INSERT INTO images (articleID, image, paragraph) VALUES (" + image.articleID + ", '" + image.image+ "', " + str(image.paragraph) + ")"
		self.cursor.execute(sqlCommand)
		self.cnx.commit()
		return self.getArticleWithID(image.articleID)

	def addSource(self, source):
		self.connect()
		sqlCommand = "INSERT INTO sources (articleID, sourceNumber, title, source) VALUES (" + str(source.articleID) + ", " + str(source.sourceNumber) + ", '" + source.title + "', '" + source.link + "')"
		self.cursor.execute(sqlCommand)
		self.cnx.commit()
		return self.getArticleWithID(source.articleID)
