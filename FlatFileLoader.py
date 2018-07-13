import mysql.connector

def loadContributors():
	cnx = mysql.connector.connect(user='nicheuser', password='nichepass', host='127.0.0.1', database='NicheNews')
	curs = cnx.cursor()

	file = open("contributors.txt", "r")
	lines = file.readlines()
	curs.execute("DELETE FROM contributors")
	curs.exectue("ALTER TABLE contributors AUTO_INCREMENT=1")
	for i in lines:
		user = i.rsplit("\n", 1)[0].split(",")
		sqlStatment = "INSERT INTO contributors (firstName, lastName, possition, image, bio) VALUES ('" + str(user[0]) + "', '" + str(user[1]) + "', '" + str(user[2]) + "', '" + str(user[3]) + "', '" + "Hi my name is " + str(user[0]) + " " + str(user[1]) + "')"
		print(sqlStatment)
		curs.execute(sqlStatment)
		cnx.commit()

	curs.execute("SELECT * FROM contributors")
	print(curs.fetchall())