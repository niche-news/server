USE NicheNews;

DROP TABLE IF EXISTS sources;
DROP TABLE IF EXISTS images;
DROP TABLE IF EXISTS articles;
DROP TABLE IF EXISTS contributors;

CREATE TABLE contributors(
authorID INT NOT NULL UNIQUE  AUTO_INCREMENT,
firstName VARCHAR(20) NOT NULL,
lastName VARCHAR(20) NOT NULL,
image VARCHAR(200) NOT NULL,
bio TEXT NOT NULL,
possition VARCHAR(20) NOT NULL,
PRIMARY KEY (authorID)
);

CREATE TABLE articles(
articleID INT NOT NULL UNIQUE AUTO_INCREMENT,
title VARCHAR(100) NOT NULL,
subTitle VARCHAR(400),
text LONGTEXT NOT NULL,
upvotes INT DEFAULT 0,
authorID INT NOT NULL,
publishDate DATE NOT NULL,
type VARCHAR(10),
PRIMARY KEY (articleID),
FOREIGN KEY (authorID) REFERENCES contributors(authorID)
);

CREATE TABLE sources(
articleID INT NOT NULL,
sourceNumber TINYINT,
title TEXT,
source TEXT,
PRIMARY KEY (articleID, sourceNumber),
FOREIGN KEY (articleID) REFERENCES articles(articleID)
);

CREATE TABLE images(
articleID INT NOT NULL,
image VARCHAR(200) NOT NULL,
paragraph INT NOT NULL DEFAULT 0,
PRIMARY KEY (articleID, image),
FOREIGN KEY (articleID) REFERENCES articles(articleID)
)