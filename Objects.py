import json

class Article(object):

	def __init__(self, articleID, title, text, date):
		self.articleID = articleID
		self.title = title
		self.text = text
		self.date = date

#	def __init__(self, articleID, title, subTitle, text, fName, lName, date, imageLocation, type, upvotes):
#		self.__init__(articleID, title, text, date)
#		self.subTitle = subTitle
#		self.authorName = str(fName) + " " + str(lName)
#		self.imageLocation = imageLocation
#		self.type = type
#		self.upvotes = upvotes

	def toJSON(self):
	        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
