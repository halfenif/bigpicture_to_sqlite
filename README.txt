#-------------------
# Description
This is script for RSS Image(Boston Big Picture) to Local SQLITE Table(blob)

#-------------------
# Install Module
pip3 install DBMS
pip3 install feedparser
pip3 install beautifulsoup4
pip3 install flask

#-------------------
# Table Create
python3 db_create_table.py

#-------------------
# Get Feeds and Images
python3 feed_article.py
1) feed_parser -> db_article.insertItem() -> Exist Check [Skip or db_article.sqlInsert()]
2) db_article.sqlSelectArticleForItemUpdate() ->  feed_item.insertItemFromArticle()
   LOOP: urllib_article.urlToString() -> htmllib_article.parseArticle()
                                          >> Delete Item(by seq)
                                          LOOP: db_item.sqlInsert()

#-------------------
# View Image by Flask default httpd
python3 app_start.py
