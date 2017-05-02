import datetime
import os
import db_item
import urllib

from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import urlparse
from os.path import splitext, basename

constOutputFolder = './output_image/'

#---------------------------------
# Folder Safe
try:
    os.stat(constOutputFolder)
except:
    os.makedirs(constOutputFolder)

#---------------------------------
# Html Parsing & Insert Item
def parseArticle(strContent, pseq):
    soup_all = BeautifulSoup(strContent,'lxml')

    allDiv = soup_all.find_all('div',  attrs={"class": "photo"})

    #------------------------------
    #init Item
    db_item.sqlDeleteBypseq(pseq)

    for item in allDiv:
        linkdata = 'http:' + urllib.parse.quote(item.img["src"])

        try:
            textdata = item.find_next('div', attrs={"class": "gcaption geor"}).text
        except Exception as err:
            textdata = "Error"
            print(err)

        rawdata = ""

        try:
            obj_response = urlopen(linkdata)
            rawdata = obj_response.read()
        except Exception as err:
            print(err)

        #------------------
        #Test Stream To Image
        #streamToFile(rawdata, linkdata)

        db_item.sqlInsert(pseq, textdata, rawdata, linkdata)
        print('[Insert Item]' + linkdata)

    return


#---------------------------------
# Stream to File >> Image Stream To File
def streamToFile(stream, url):
    url_net_Loc = urlparse(url).netloc.replace(':', '_')
    write_date_time = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

    disassembled = urlparse(url)
    filename, file_ext = splitext(basename(disassembled.path))

    file_full_path = constOutputFolder + 'Response.' + write_date_time + '.' + filename + file_ext

    f = open(file_full_path, 'wb')
    f.write(stream)
    f.close()
    print('Response To File Writed: ' + file_full_path)
    return
