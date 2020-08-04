import requests
from lxml import html
import json

#structure for JSON files
def createData():
    data = {}
    data["topic"] = ""
    data["headline"] = ""
    return data

#Append topic + headline at the end of the file
def writeJSON(data, articles,topics, writeFile):
    for i in range(len(articles)):
        data["topic"] = topics
        data["headline"] = articles[i]
        with open(writeFile, "a+", encoding='utf8') as outfile:
            json.dump(data, outfile,ensure_ascii=False)
            outfile.write("\n")
        outfile.close()
    print('Done writing!')

#Send GET HTTP requests to server and receive [response 200]
#Parse html tree to get headline data
def getHeadline(link, headline_Xpath):
    h = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'}
    response = requests.get(link, headers=h)
    print(f'{link}: {response}')
    tree = html.fromstring(response.content)
    return tree.xpath(headline_Xpath), response.status_code




