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

	def test(self):
		pass

	def toJSON(self):
		return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
