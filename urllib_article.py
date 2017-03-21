import urllib
import datetime
import codecs
import os

from urllib.request import urlopen
from urllib.parse import urlparse

#---------------------------------
# Const
constDateTime = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
constCharSet = 'UTF-8'
constOutputFolder = './output_response/'

isDebug = 'N'

#---------------------------------
# Folder Safe
try:
    os.stat(constOutputFolder)
except:
    os.makedirs(constOutputFolder)


#---------------------------------
# get URL CharterSet
def urlGetCharterSet(url):
    obj_response = urlopen(url)
    format, params = obj_response.getheader('Content-type').split(';')
    strResponseCharSet = params.split('=')[1]
    #print('ResponseCharSet:' + strResponseCharSet)
    return strResponseCharSet

#---------------------------------
# URL to String
def urlToString(url):
    obj_response = urlopen(url)
    strResponseCharSet = urlGetCharterSet(url)
    strResponse = obj_response.read().decode(strResponseCharSet)
    return strResponse

#---------------------------------
# URL to File
def urlToFile(url):
    url_net_Loc = urlparse(url).netloc.replace(':', '_')
    write_date_time = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    file_full_path = constOutputFolder + 'Response.' + url_net_Loc + '.' + write_date_time + '.txt'

    strResponseCharSet = urlGetCharterSet(url)
    strResponse = urlToString(url)

    f = codecs.open(file_full_path, 'w', strResponseCharSet)
    f.write(strResponse)
    f.close()
    print('Response To File Writed: ' + file_full_path)
    return

def urlParseArticle(link):
    return


