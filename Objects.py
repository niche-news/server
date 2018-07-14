import sys, os, json

class JSONObject:
	def toJSON(self):
		return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

class Article(object):

	def __init__(self, articleID, title, text, date, authorName, subTitle, upVotes, type):
		self.articleID = articleID
		self.title = title
		self.text = text
		self.date = date
		self.subTitle = subTitle
		self.authorName = authorName
		self.type = type
		self.upvotes = upVotes
		self.images = []
		self.sources = []

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

	def toJSON(self):
		return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)