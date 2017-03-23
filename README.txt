#-------------------
# Description
This is script for RSS Image(Boston Big Picture) to Local SQLITE Table(blob)

#-------------------
# Install Module
pip install DBMS
pip install feedparser
pip install beautifulsoup4
pip install lxml



#-------------------
# Table Create
# RUN db_create_table.py
CREATE TABLE `tb_article` (
	`seq`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`title`	TEXT,
	`link`	TEXT,
	`pubdate`	TEXT,
	`regdate`	datetime DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE `tb_item` (
	`seq`	INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
	`pseq`	INTEGER NOT NULL,
	`textdata`	TEXT,
	`rawdata`	BLOB,
	`linkdata`	TEXT,
	`regdate`	datetime DEFAULT CURRENT_TIMESTAMP
);

#-------------------
# Program call
feed_article.py
1) feed_parser -> db_article.insertItem() -> Exist Check [Skip or db_article.sqlInsert()]
2) db_article.sqlSelectArticleForItemUpdate() ->  feed_item.insertItemFromArticle()
   LOOP: urllib_article.urlToString() -> htmllib_article.parseArticle()
                                          >> Delete Item(by seq)
                                          LOOP: db_item.sqlInsert()

