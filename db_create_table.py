import dbms
import os
import const_dbms

constDBArticle = (
    "CREATE TABLE `tb_article` (                         "
    "	`seq`	INTEGER PRIMARY KEY AUTOINCREMENT,         "
    "	`title`	TEXT,                                   "
    "	`link`	TEXT,                                      "
    "	`pubdate`	TEXT,                                   "
    "	`regdate`	datetime DEFAULT CURRENT_TIMESTAMP      "
    ")                                                            "
)

constDBItem = (
"CREATE TABLE `tb_item` (                                           "
"	`seq`	INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, "
"	`pseq`	INTEGER NOT NULL,                                      "
"	`textdata`	TEXT,                                                    "
"	`rawdata`	BLOB,                                                    "
"	`linkdata`	TEXT,                                                    "
"	`regdate`	datetime DEFAULT CURRENT_TIMESTAMP       "
")                                                                         "
)


#---------------------------------
# Create Table
conn = const_dbms.get_conn()
cur = conn.cursor()

cur.execute(constDBArticle)
cur.execute(constDBItem)

conn.commit()
conn.close()
