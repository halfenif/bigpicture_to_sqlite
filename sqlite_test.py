import sqlite3

constDBMS = './output_dbms/db_bigpicture.db'
constSQLInsert = 'INSERT INTO tb_article (title, link, pubdate) values (?, ?, ?)'
constSQLSelect = 'SELECT SEQ FROM tb_article WHERE LINK = ?'
#constSQLSelect = "SELECT * FROM tb_article WHERE SEQ = %s"
constParamLink = 'http://www.bostonglobe.com/news/bigpicture/2017/03/01/globe-photos-month-february/Bkj6A440o1e84N44rszTqL/story.html'

conn = sqlite3.connect(constDBMS)

cur = conn.cursor()

#cur.execute(constSQLSelect, constParamLink)
cur.execute(constSQLSelect, ('11',))

rows = cur.fetchall()
for row in rows:
    print(row)
