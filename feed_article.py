import feedparser
import time
import db_article
import urllib_article
import feed_item
import urllib

#---------------------------------
# Const
constUrl = 'http://www.bostonglobe.com/rss/bigpicture'

#---------------------------------
# Insert Data
def insertFeed(item):
    result_title = item.title
    result_link = item.link
    result_published_time = time.gmtime(time.mktime(item.published_parsed))
    result_date_for_key = time.strftime('%Y%m%d%H%M%S', result_published_time)

    db_article.insertItem(result_title, result_link, result_date_for_key)
    return

#---------------------------------
# TestCall
def writeUrlToFile(item):
    urllib_article.urlToFile(item.link)
    return

#---------------------------------
#Main Logic

## Parsing WebSite (RSS)
resultResponse = feedparser.parse(constUrl)

## RSS item To DB
for item in resultResponse.entries:
    insertFeed(item);
    #writeUrlToFile(item);

print('------------OK Article Parsing End')

## Update Item
resultArticle = db_article.sqlSelectArticleForItemUpdate()
print(resultArticle)
for item in resultArticle:
    feed_item.insertItemFromArticle(item["link"], item["seq"])
    print("[Insert Item from Article END]" + item["link"])

print('------------OK Item Insert End')


