import datetime
import codecs
import os

# Const
constDateTime = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
constOutputFolder = './output_response/'

#---------------------------------
# Folder Safe
try:
    os.stat(constOutputFolder)
except:
    os.makedirs(constOutputFolder)

#---------------------------------
# String To File
def strToFile(strContent, typeStr, strKey, strExt):
    constResponseFileFullPath = constOutputFolder + typeStr + '.' + constDateTime + '.' + strKey + '.' +strExt
    f = codecs.open(constResponseFileFullPath, 'w', 'UTF-8')
    f.write(strContent)
    f.close()
    print('Response To File Writed: ' + constResponseFileFullPath)