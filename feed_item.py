import db_item
import urllib_article
import htmllib_article
import htmllib_test

#---------------------------------
# Insert Item
def insertItemFromArticle(strLink, pSeq):
    strContent = urllib_article.urlToString(strLink)
    htmllib_article.parseArticle(strContent, pSeq)
    return

#---------------------------------
# Test Suit
if __name__ == "__main__":
    row = db_item.selectItemTest()

    strLink = row["link"]
    pSeq = row["seq"]

    insertItemFromArticle(strLink, pSeq)