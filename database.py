import mysql.connector
import json

class database:

	def __init__(self):
        	self.cnx = mysql.connector.connect(user='nicheuser', password='nichepass', host='127.0.0.1', database='NicheNews')
       		self.cursor = self.cnx.cursor()

	def getAllArticles(self):
		sqlCommand = "SELECT * FROM articles"
		self.cursor.execute(sqlCommand)
		arr = []
		data = self.cursor.fetchall()
		for (articleID, title, text, date) in self.cursor:
			print('id: ' + str(articleID) + " title: " + str(title) + " text: " + str(text) + " date: " str(date))
			#newArticle = Article(articleID, title, text, date)
			# arr.append(newArticle.toJSON())
		print(data)
		return str(data)
		# return arr