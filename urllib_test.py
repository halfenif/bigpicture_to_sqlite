import urllib
import datetime
import codecs

from urllib.request import urlopen
from urllib.parse import urlparse

#---------------------------------
# Const
constDateTime = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
#constUrl = 'http://www.google.co.kr'
constUrl = 'http://www.bostonglobe.com:80/rss/bigpicture'
assert isinstance(urlparse(constUrl).netloc, object)
constUrlNetLoc = urlparse(constUrl).netloc.replace(':','_')
print(constUrlNetLoc)

constCharSet = 'UTF-8'
constOutputFolder = './'
constResponseFileFullPath = constOutputFolder + 'Response.' + constDateTime + '.txt'
#---------------------------------
# Flow Control
configWriteFile = 'Y'
configPrint = 'N'
#---------------------------------
objResponse = urlopen(constUrl)

format, params = objResponse.getheader('Content-type').split(';')
strResponseCharSet = params.split('=')[1]

strResponse = objResponse.read().decode(strResponseCharSet)

if configPrint == 'Y':
    print('Response:' + strResponse)

print('ResponseCharSet:' + strResponseCharSet)

if configWriteFile == 'Y':
    f = codecs.open(constResponseFileFullPath, 'w', strResponseCharSet)
    #f = open(constResponseFileFullPath, 'w')
    f.write(strResponse)
    f.close()
    print('Response To File Writed: ' + constResponseFileFullPath)
