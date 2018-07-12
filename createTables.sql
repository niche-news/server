USE NicheNews;

DROP TABLE IF EXISTS sources;
DROP TABLE IF EXISTS articles;
DROP TABLE IF EXISTS contributors;

CREATE TABLE contributors(
authorID INT NOT NULL UNIQUE PRIMARY KEY AUTO_INCREMENT,
firstName VARCHAR(20) NOT NULL,
lastName VARCHAR(20) NOT NULL,
image VARCHAR(50),
bio TEXT NOT NULL,
possition VARCHAR(20)
);

CREATE TABLE articles(
articleID INT NOT NULL UNIQUE AUTO_INCREMENT,
title VARCHAR(100) NOT NULL,
subTitle VARCHAR(100),
text LONGTEXT NOT NULL,
image VARCHAR(50),
upvotes INT DEFAULT 0,
authorID INT,
publishDate DATE NOT NULL,
type VARCHAR(10),
PRIMARY KEY (articleID),
FOREIGN KEY (authorID) REFERENCES contributors(authorID)
);

CREATE TABLE sources(
sourceNumber TINYINT,
articleID INT NOT NULL,
title VARCHAR(30) NOT NULL,
source TEXT,
PRIMARY KEY (articleID, sourceNumber),
FOREIGN KEY (articleID) REFERENCES articles(articleID)
);