import dbms
import time
import const_dbms

constSQLInsert = 'INSERT INTO tb_article (title, link, pubdate) values (?, ?, ?)'
constSQLSelectForExistCheck = 'SELECT seq FROM tb_article WHERE link = ?'
constSQLSelectForItemUpdate = 'SELECT seq, link FROM tb_article WHERE seq IN (SELECT seq FROM tb_article EXCEPT SELECT pseq seq FROM tb_item)'
constParamTestLink = 'http://www.bostonglobe.com/news/bigpicture/2017/03/01/globe-photos-month-february/Bkj6A440o1e84N44rszTqL/story.html'


#---------------------------------
# SQL Exist Check
def sqlExistCheck(link):
    conn = const_dbms.get_conn()
    cur = conn.cursor()
    cur.execute(constSQLSelectForExistCheck, (link,))

    bExist = False

    if len(cur.fetchall())  > 0:
        bExist = True

    conn.close()
    return bExist

#---------------------------------
# SQL Retrive Article for Item Update
def sqlSelectArticleForItemUpdate():
    conn = const_dbms.get_conn()
    cur = conn.cursor()
    cur.execute(constSQLSelectForItemUpdate)

    result = []

    for item in cur.fetchall():
        result.append(item)

    conn.close()
    return result

#---------------------------------
# SQL Article Insert
def sqlInsert(result_title, result_link, result_date_for_key):
    conn = const_dbms.get_conn()
    cur = conn.cursor()
    cur.execute(constSQLInsert, (result_title, result_link, result_date_for_key,))
    cur.showStatement()
    conn.commit()
    conn.close()
    return

#---------------------------------
# Article Logic - Insert or Skip
def insertItem(result_title, result_link, result_date_for_key):
    if sqlExistCheck(result_link):
        print('[Exist  Article] ' + result_title)
    else:
        sqlInsert(result_title, result_link, result_date_for_key)
        print('[Insert Article] ' + result_title)

    return

#---------------------------------
# Test Suit
if __name__ == "__main__":
    if sqlExistCheck(constParamTestLink):
        print('Exist Data!')
    else:
        print('New Data')
