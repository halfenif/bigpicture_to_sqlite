import time
import dbms
import const_dbms

constSQLInsert = 'INSERT INTO tb_article (title, link, pubdate) values (?, ?, ?)'
constSQLSelect = 'SELECT SEQ FROM tb_article WHERE LINK = ?'
constParamLink = 'http://www.bostonglobe.com/news/bigpicture/2017/03/01/globe-photos-month-february/Bkj6A440o1e84N44rszTqL/story.html'


#---------------------------------
# Exist Check
def sqlExistCheck(link):
    conn = const_dbms.get_conn()
    cur = conn.cursor()
    cur.execute(constSQLSelect, (link,))

    bExist = False

    if len(cur.fetchall())  > 0:
        bExist = True

    conn.close()
    return bExist


def sqlInsert(item):
    result_title = item.title
    result_link = item.link
    result_published_time = time.gmtime(time.mktime(item.published_parsed))
    result_date_for_key = time.strftime('%Y%m%d%H%M%S', result_published_time)

    conn = const_dbms.get_conn()
    cur = conn.cursor()
    cur.execute(constSQLInsert, (result_title, result_link, result_date_for_key,))
    cur.showStatement()
    conn.commit()
    conn.close()
    return

def insertItem(item):
    if sqlExistCheck(item.link):
        print('Exist Link:' + item.link)
    else:
        sqlInsert(item)

    return

#---------------------------------
# Test Suit
if __name__ == "__main__":
    if sqlExistCheck(constParamLink):
        print('Exist Data!')
    else:
        print('New Data')
