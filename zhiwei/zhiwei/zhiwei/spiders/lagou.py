import scrapy
import re
import urllib
from scrapy.http import Request



class LagouSpider(scrapy.Spider):
    name = 'lagou'
    allowed_domains = ['lagou.com']
    start_urls = ['https://www.baidu.com/?tn=57095150_2_oem_dg']

    # 获取拉勾的网页
    def parse(self, response):
        api_headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36",
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Host":"www.lagou.com",
        }
        for i in range(1, 3):
            url = 'https://www.lagou.com/zhaopin/' + str(i)
            print(url)
            yield Request(url=url, callback=self.page,headers=api_headers,errback=self.error)


    # 获取各招聘页的详细页
    def page(self, response):
        positionid = response.xpath("//li[@class= 'con_list_item default_list']/@data-positionid").extract()[0]
        print(positionid)

    def error(self,response):
        print("error")
