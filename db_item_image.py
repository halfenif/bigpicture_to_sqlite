import const_dbms
import dbms
import os
import sys
import base64

tempSQL = []
tempSQL.append("SELECT a.textdata, a.rawdata, b.title, substr(b.pubdate,1,4) || '-' || substr(b.pubdate,5,2) || '-' || substr(b.pubdate,7,2) pubdate ")
tempSQL.append("       ,(SELECT MAX(t.seq) FROM tb_item t WHERE t.pseq = ? and t.seq < ?) seq_before ")
tempSQL.append("       ,(SELECT MIN(t.seq) FROM tb_item t WHERE t.pseq = ? and t.seq > ?) seq_after ")
tempSQL.append("FROM tb_item a, tb_article b ")
tempSQL.append("WHERE a.pseq = b.seq AND a.pseq = ? AND a.seq = ? ")

constSQLSelect = ''.join(tempSQL)

class item_image():
    data_uri = None
    textdata = None
    pseq = None
    seq = None
    seq_before = ''
    seq_after = ''
    title = ''
    pubdate = ''

    def __setrawdata__(self, rawdata):
        try:
            self.data_uri = base64.b64encode(rawdata).decode()
        except:
            self.data_uri = "Error"
            pass

    def __settextdata__(self, textdata):
        self.textdata = textdata

    def __setpseq__(self, pseq):
        self.pseq = pseq

    def __setseq__(self, seq):
        self.seq = seq

    def __setseq_before__(self, seq_before):
        if seq_before == None:
            self.seq_before = '0'
        else:
            self.seq_before = seq_before

    def __setseq_after__(self, seq_after):
        if seq_after == None:
            self.seq_after = '0'
        else:
            self.seq_after = seq_after

    def __settitle__(self, title):
        self.title = title

    def __setpubdate__(self, pubdate):
        self.pubdate = pubdate

def selectItem(pseq, seq):

    conn = const_dbms.get_conn()
    cur = conn.cursor()
    cur.execute(constSQLSelect, (pseq, seq, pseq, seq, pseq, seq, ))

    #item > dbms.cursor.Record
    item = cur.fetchone()

    if item == None:
        return ''

    return_image = item_image
    return_image.__setrawdata__(return_image, item["rawdata"])
    return_image.__settextdata__(return_image, item["textdata"])
    return_image.__setpseq__(return_image, pseq)
    return_image.__setseq__(return_image, seq)
    return_image.__setseq_before__(return_image, item["seq_before"])
    return_image.__setseq_after__(return_image, item["seq_after"])
    return_image.__settitle__(return_image, item["title"])
    return_image.__setpubdate__(return_image, item["pubdate"])

    return return_image


if __name__ == '__main__':
    selectItem()
