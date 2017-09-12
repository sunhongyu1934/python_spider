from lxml import etree

import requests

public_headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36",
        }
response=requests.get("https://www.lagou.com/jobs/3508702.html",headers=public_headers)

html=etree.HTML(response.content.decode("utf-8"))
a=html.xpath('//dd/ul[@class="c_feature"]/li[4]/text()')
print(str(a[1]).replace(' ',''))