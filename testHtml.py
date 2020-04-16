from bs4 import BeautifulSoup
import json
import re

file_full_path = './output_response/01.strContent.2020-04-15_21-49-12.490.html'

# Read File
f = open(file_full_path, 'r')
strContent = f.read()
f.close()
#print(strContent)

# Soup Html
soup_all = BeautifulSoup(strContent,'html.parser')
#print(soup_all)

pattern = re.compile(r"Fusion.globalContent={.*};Fusion.globalContentConfig")
soup_script = soup_all.find("script", text=pattern)
# print(soup_script.text)

soup_group = pattern.search(soup_script.text).group()
# print(soup_group)

strJsonInput = soup_group[21:-27]
# print(strJsonInput)

dataJson = json.loads(strJsonInput)
# print(json.dumps(dataJson, ensure_ascii=False, indent="\t"))

# with open(file_full_path+'.dump', 'w') as outfile:
#     json.dump(dataJson, outfile, ensure_ascii=False, indent=4)

dataLevel1 = dataJson["content_elements"]
# print(json.dumps(dataLevel1, ensure_ascii=False, indent="\t"))

# with open(file_full_path+'.content_elements.dump', 'w') as outfile:
#     json.dump(dataLevel1, outfile, ensure_ascii=False, indent=4)

for item in dataLevel1:
    # print('-------------------------')
    # print(item)

    dataId      = item["_id"]
    dataCaption = item["caption"]
    dataUrl     = item["url"]
    print(dataId)
    print(dataCaption)
    print(dataUrl)
