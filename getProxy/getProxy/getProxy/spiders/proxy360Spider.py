# -*- coding: utf-8 -*-
import scrapy
from getProxy.items import GetproxyItem

class Proxy360spiderSpider(scrapy.Spider):
    name = 'proxy360Spider'
    allowed_domains = ['proxy360.cn']
    start_urls = ['http://www.proxy360.cn/']

    def parse(self, response):
        subSelector = response.xpath('//div[@class="proxylistitem"]')
        items = []
        for sub in subSelector:
            print(sub)
            item = GetproxyItem()
            item['ip'] = sub.xpath('.//span[1]/text()').extract()[0].strip()
            item['port'] = sub.xpath('.//span[2]/text()').extract()[0].strip()
            item['type'] = sub.xpath('.//span[3]/text()').extract()[0].strip()
            item['location'] = sub.xpath('.//span[4]/text()').extract()[0].strip()
            item['protocol'] = sub.xpath('.//span[5]/text()').extract()[0].strip()
            item['source'] = sub.xpath('.//span[8]/text()').extract()[0].strip()
            items.append(item)
        return items
