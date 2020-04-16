import const_dbms
import dbms

constSQLSelect = 'SELECT pseq, seq, textdata FROM tb_item WHERE pseq = ? ORDER BY seq ASC'

def selectItem(seq):
    conn = const_dbms.get_conn()
    cur = conn.cursor()
    cur.execute(constSQLSelect, (seq, ))
    return cur.fetchall()

if __name__ == '__main__':
    selectItem()
