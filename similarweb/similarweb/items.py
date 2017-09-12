# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field

# 第一次抓取是将 2016-1 - 2017-3 之间的数据全部抓取回来。
class SimilarwebUVItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pid = Field()
    mongo_id = Field()
    domain_url = Field()
    uv_json = Field()
    start_date = Field()
    end_date = Field()
    time_interval = Field()

class SimilarwebPVItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pid = Field()
    mongo_id = Field()
    domain_url = Field()
    pv_json = Field()
    start_date = Field()
    end_date = Field()
    time_interval = Field()