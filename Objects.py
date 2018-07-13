import sys, os, json

class JSONObject:
	def toJSON(self):
		return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

class Article(object):

	def __init__(self, articleID, title, text, date, authorName, subTitle, image, upVotes, type):
		self.articleID = articleID
		self.title = title
		self.text = text
		self.date = date
		self.subTitle = subTitle
		self.authorName = authorName
		self.image = image
		self.type = type
		self.upvotes = upVotes



#	def __init__(self, articleID, title, subTitle, text, fName, lName, date, imageLocation, type, upvotes):
#		self.__init__(articleID, title, text, date)
#		self.subTitle = subTitle
#		self.authorName = str(fName) + " " + str(lName)
#		self.imageLocation = imageLocation
#		self.type = type
#		self.upvotes = upvotes

	def test(self):
		pass

	def toJSON(self):
		return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
