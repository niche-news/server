import mysql.connector


cnx = mysql.connector.connect(user='nicheuser', password='nichepass', host='127.0.0.1', database='NicheNews')
curs = cnx.cursor()

def reloadTheWholeDatabase():
	curs.execute("DELETE FROM sources")
	curs.execute("DELETE FROM images")
	curs.execute("DELETE FROM articles")
	curs.execute("DELETE FROM contributors")

	loadContributors()
	loadArticles()
	loadSources()
	loadImages()

def loadContributors():
	file = open("flatfiles/contributors.txt", "r")
	lines = file.readlines()
	curs.execute("ALTER TABLE contributors AUTO_INCREMENT=1")
	for i in lines:
		user = i.rsplit("\n", 1)[0].split(";")
		sqlStatment = "INSERT INTO contributors (firstName, lastName, possition, image, bio) VALUES ('" + str(user[0]) + "', '" + str(user[1]) + "', '" + str(user[2]) + "', '" + str(user[3]) + "', '" + "Hi my name is " + str(user[0]) + " " + str(user[1]) + "')"
		curs.execute(sqlStatment)
		cnx.commit()

def loadArticles():
	articleInfo = open("flatfiles/articleInfo.txt", "r")
	articleTexts = open("flatfiles/articleText.txt", "r")
	curs.execute("ALTER TABLE articles AUTO_INCREMENT=1")
	aiLines = articleInfo.readlines()
	for i in aiLines:
		inf = i.rsplit("\n", 1)[0].split(";")
		txt = articleTexts.readline().rsplit("\n", 1)[0]
		sqlStatment = "INSERT INTO articles (articleID, title, subTitle, text, upvotes, authorID, publishDate) VALUES (" + inf[0] + ", '" + inf[1] + "', '" + inf[2] + "', '" + txt + "', " + inf[3] + ", " + inf[4] + ", " + inf[5] + ")"
		curs.execute(sqlStatment)
		cnx.commit()

def loadSources():
	sources = open("flatfiles/articleSources.txt", "r")
	for i in sources.readlines():
		inf = i.rsplit("\n", 1)[0].split(";")
		sqlStatment = "INSERT INTO sources (articleID, sourceNumber, title, source) VALUES (" + inf[0] + ", " + inf[1] + " ,'" + inf[2] + "', '" + inf[3] + "')"
		curs.execute(sqlStatment)
		cnx.commit()

def loadImages():
	images = open("flatfiles/articleImages.txt", "r")
	
	for i in images.readlines():
		inf = i.rsplit("\n", 1)[0].split(";")
		sqlStatment = "INSERT INTO images (articleID, paragraph, image) VALUES ( " + inf[0] + ", " + inf[1] + ", '" + inf[2] + "')"
		curs.execute(sqlStatment)
		cnx.commit()

reloadTheWholeDatabase()

