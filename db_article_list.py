import const_dbms
import dbms

constSQLSelect = "SELECT substr(a.pubdate,1,4) || '-' || substr(a.pubdate,5,2) || '-' || substr(a.pubdate,7,2) pubdate, a.seq, a.title,  a.itemcount, a.firstitemseq FROM tb_article a ORDER BY a.pubdate DESC"

def selectArticle():
    print("Start selectArticle")
    conn = const_dbms.get_conn()
    cur = conn.cursor()
    cur.execute(constSQLSelect)
    return cur.fetchall()

if __name__ == '__main__':
    selectArticle()
