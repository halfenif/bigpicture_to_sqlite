import urllib
import datetime
import codecs
import os

from urllib.request import urlopen
from urllib.parse import urlparse

#---------------------------------
# Const
constDateTime = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
#constUrl = 'http://www.google.co.kr'
#constUrl = 'http://www.bostonglobe.com:80/rss/bigpicture'
constUrl = 'http://www.bostonglobe.com/news/bigpicture/2017/02/24/festival-defined/bG6YGhHkmd98vOMQ3QAAQJ/story.html'
constUrlNetLoc = urlparse(constUrl).netloc.replace(':','_')

constCharSet = 'UTF-8'
constOutputFolder = './output_response/'
constResponseFileFullPath = constOutputFolder + 'Response.' + constUrlNetLoc + '.' + constDateTime + '.xml'

#---------------------------------
# Folder Safe
try:
    os.stat(constOutputFolder)
except:
    os.makedirs(constOutputFolder)

#---------------------------------
# Flow Control
configWriteFile = 'Y'
configPrint = 'N'

#---------------------------------
# Request Call
objResponse = urlopen(constUrl)

format, params = objResponse.getheader('Content-type').split(';')
strResponseCharSet = params.split('=')[1]

strResponse = objResponse.read().decode(strResponseCharSet)

if configPrint == 'Y':
    print('Response:' + strResponse)

print('ResponseCharSet:' + strResponseCharSet)

if configWriteFile == 'Y':
    f = codecs.open(constResponseFileFullPath, 'w', strResponseCharSet)
    f.write(strResponse)
    f.close()
    print('Response To File Writed: ' + constResponseFileFullPath)
