import sys, os, json

class JSONObject:
	def toJSON(self):
		return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

class Article(object):

	def __init__(self, articleID, title, text, date, authorName, subTitle, upVotes, type, authorID):
		self.articleID = articleID
		self.title = title
		self.text = text
		self.date = date
		self.subTitle = subTitle
		self.authorName = authorName
		self.type = type
		self.upvotes = upVotes
		self.authorID = authorID
		self.images = []
		self.sources = []
	
	@classmethod
	def init(cls, title, text, authorID, publishDate):
		return cls(0, title, text, publishDate, authorID, '', 0, '')

	def toJSON(self):
		return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

class Contributor(object):

	def __init__(self, id, firstName, lastName, image, bio, possition):
		self.id = id
		self.nameFirst = firstName
		self.nameLast = lastName
		self.image = image
		self.bio = bio
		self.possition = possition
		self.articleIDs = []

	def toJSON(self):
		return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

class Image(JSONObject):

	def __init__(self, id, image):
		self.articleID = id
		self.image = image
		self.paragraph = 0

class Source(JSONObject):

	def __init__(self, id, sourceNumber):#, title, link):
		self.articleID = id
		self.sourceNumber = sourceNumber
		self.title = ''
		self.link = ''
