import dbms
import os
constOutputFolder = './output_dbms'
constDBMS = './output_dbms/db_bigpicture.db'

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
# Folder Safe
try:
    os.stat(constOutputFolder)
except:
    os.makedirs(constOutputFolder)

#---------------------------------
# Create Table
conn = dbms.connect.sqlite(constDBMS)
cur = conn.cursor()

cur.execute(constDBArticle)
cur.execute(constDBItem)

conn.commit()
conn.close()