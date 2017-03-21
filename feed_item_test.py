import db_item
import urllib_article
import htmllib_article
import htmllib_test

row = db_item.selectItemTest()

strLink = row["link"]
pSeq = row["seq"]

#print("strLink:" + strLink)
#print("pSeq:" + str(pSeq))

strContent = urllib_article.urlToString(strLink)
htmllib_article.parseArticle(strContent, pSeq)
#htmllib_test.parsing_test(strContent, pSeq)

