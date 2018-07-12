import mysql.connector
import json

class database:

	def __init__(self):
        	self.cnx = mysql.connector.connect(user='nicheuser', password='nichepass', host='127.0.0.1', database='NicheNews')
       		self.cursor = self.cnx.cursor()

	def getAllArticles(self):
		# self.cursor.execute("SET @J = json_object('title', title, 'text', text)")
		#cursor.execute("SELECT @J FROM articles")
		# cursor.execute("SELECT 'title', title, 'text', text FROM articles")
		#cursor.execute("SELECT JSON_OBJECT ( KEY 'ID' IS articleID FORMAT JSON, KEY 'title' IS title FORMAT JSON, KEY 'text' IS text FORMAT JSON) 'articles'  FROM articles")
		sqlCommand = "SELECT * FROM articles"
		self.cursor.execute(sqlCommand)
		data = self.cursor.fetchall()
		print(data)
		return str(data)
