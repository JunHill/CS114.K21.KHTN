import requests
from lxml import html
import json
from crawler import createData, writeJSON, getHeadline

#phap luat, khoa hoc
link_headers = ["phap-luat", "khoa-hoc"]
topics = [4,6]
for j in range(len(link_headers)):
    for i in range(1, 500):
        vnexpress_articles, status = getHeadline(f"https://vnexpress.net/{link_headers[j]}-p{i}/",
                                                  '//*[@class="title-news"]/a/@title')
        for k in range(len(vnexpress_articles)):
            vnexpress_articles[k] = vnexpress_articles[k].encode('iso-8859-1').decode('utf-8')
        if status != 200:
            print(f"Error with https://vnexpress.net/{link_headers[j]}/p{i}/ !")
            continue
        vnexpress_data = createData()
        writeJSON(vnexpress_data, vnexpress_articles, topics[j], 'vnexpress_' + link_headers[j] + '.txt')

#"the-thao"

for i in range(1, 500):
    vnexpress_articles, status = getHeadline(f"https://vnexpress.net/the-thao/p{i}/",
                                                  '//*[@class="title-news"]/a/@title')
    if status != 200:
        print(f"Error with https://vnexpress.net/the-thao/p{i}/ !")
        continue
    vnexpress_data = createData()
    writeJSON(vnexpress_data, vnexpress_articles, 5, 'vnexpress_the-thao.txt')

#Quan su-chinh tri
for i in range(1, 300):
    vnexpress_articles, status = getHeadline(f"https://vnexpress.net/the-gioi/quan-su-p{i}/",
                                                  '//*[@class="title-news"]/a/@title')
    if status != 200:
        print(f"Error with https://vnexpress.net/the-gioi/quan-su-p{i}/ !")
        continue
    for k in range (len(vnexpress_articles)):
        vnexpress_articles[k] = vnexpress_articles[k].encode('iso-8859-1').decode('utf-8')
    vnexpress_data = createData()
    writeJSON(vnexpress_data, vnexpress_articles, 1, 'vnexpress_chinh_tri.txt')