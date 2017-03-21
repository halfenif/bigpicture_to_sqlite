import dbms

constDBMS = './output_dbms/db_bigpicture.db'
constSQLSelect = 'SELECT seq, link FROM tb_article'
constSQLSelect = 'SELECT seq, link FROM tb_article'
constSQLInsert = 'INSERT INTO tb_item (pseq, textdata, rawdata, linkdata) values (?, ?, ?, ?)'
constSQLDelete = 'DELETE FROM tb_item WHERE pseq = ?'


def selectItemTest():
    conn = dbms.connect.sqlite(constDBMS)
    cur = conn.cursor()
    cur.execute(constSQLSelect + ' LIMIT 1')
    row = cur.fetchone()
    return row

def sqlInsert(pseq, textdata, rawdata, linkdata):
    conn = dbms.connect.sqlite(constDBMS)
    cur = conn.cursor()
    cur.execute(constSQLInsert, (pseq, textdata, rawdata, linkdata, ))
    cur.showStatement()
    conn.commit()
    conn.close()
    return

def sqlDeleteBypseq(pseq):
    conn = dbms.connect.sqlite(constDBMS)
    cur = conn.cursor()
    cur.execute(constSQLDelete, (pseq, ))
    cur.showStatement()
    conn.commit()
    conn.close()
    return
#---------------------------------
# Test Suit
if __name__ == "__main__":
    selectItemTest();
