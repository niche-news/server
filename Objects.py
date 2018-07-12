import json

class Article(Obejct):

	def __init(self, articleID, title, subTitle, text, fName, lName, publishDate, artcileDate):
		self.articleID = articleID
		self.title = title
		self.subTitle = subTitle
		self.text = text
		self.authorName = str(fName) + " " + str(lName)
		self.publishDate = publishDate
		self.artcileDate = artcileDate

	def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)