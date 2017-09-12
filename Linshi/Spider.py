#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from scrapy.spider import BaseSpider
from scrapy.http import Request
from scrapy.selector import HtmlXPathSelector
from Tutorial.items import TutorialItem
import re

class DoubanSpider(BaseSpider):
    name = "douban"
    allowed_domains = ["movie.douban.com"]
    start_urls = []

def start_requests(self):
    file_object = open('movie_name.txt','r')
    
    try:
        url_head = "https://movie.douban.com/subject_search?search_text="
        self.api_headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36",
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate",
        }
        for line in file_object:
            self.start_urls.append(url_head + line)
            
        for url in self.start_urls:
            yield self.scrapy.Request(url=url,headers=self.api_headers)
    finally:
        file_object.close()
        
#def parse(self, response):
