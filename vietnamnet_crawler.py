from crawler import getHeadline, createData, writeJSON

#crawl 450 pages of vietnamnet
link_headers = ["chinh-tri", "kinh-doanh", "doi-song", "phap-luat", "the-thao", "cong-nghe"]
topics = [1,2,3,4,5,6]
for j in range(len(link_headers)):
    for i in range(1, 450):
        vietnamnet_articles, status = getHeadline(f"https://vietnamnet.vn/vn/{link_headers[j]}/trang{i}/",
                                                  '//*[@class="f-18 title"]/text()')
        if status != 200:
            print(f"Error with https://vietnamnet.vn/vn/{link_headers[j]}/trang{i}/!")
            continue
        vietnamnet_data = createData()
        writeJSON(vietnamnet_data, vietnamnet_articles, topics[j], 'vietnamnet_' + link_headers[j] + '.txt')