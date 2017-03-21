from bs4 import BeautifulSoup

def parsing_test(strContent, pseq):
    soup = BeautifulSoup(strContent, "html.parser")

    for item in soup.find_all('div', attrs={"class":"photo"}):
        linkdata = 'http:' +item.img["src"]
        print(linkdata)

        textdata = item.find_next('div',  attrs={"class": "gcaption geor"}).text
        print(textdata)




    # find_result = soup.find('div',  attrs={"class": "photo"})
    #
    # print(find_result.img["src"])
    #
    # find_result = find_result.find_next('div',  attrs={"class": "gcaption geor"})
    #
    # print(find_result.text)
    #
    # find_result = find_result.find_next('div', attrs={"class": "photo"})
    #
    # print(find_result.img["src"])
    #
    # find_result = find_result.find_next('div',  attrs={"class": "gcaption geor"})
    #
    # print(find_result.text)

    return