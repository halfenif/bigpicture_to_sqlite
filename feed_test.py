import feedparser
import time
import db_article
import urllib_article

#---------------------------------
# Const
constUrl = 'http://www.bostonglobe.com/rss/bigpicture'

#---------------------------------
# Def
def insertFeed(item):
    result_title = item.title
    result_link = item.link
    result_published_time = time.gmtime(time.mktime(item.published_parsed))
    result_date_for_key = time.strftime('%Y%m%d%H%M%S', result_published_time)

    db_article.insertItem(result_title, result_link, result_date_for_key)
    return

def writeUrlToFile(item):
    urllib_article.urlToFile(item.link)
    return

#---------------------------------
resultResponse = feedparser.parse(constUrl)

for item in resultResponse.entries:
    insertFeed(item);
    writeUrlToFile(item);





