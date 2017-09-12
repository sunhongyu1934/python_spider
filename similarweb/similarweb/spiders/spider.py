# -*- coding: utf-8 -*-

import scrapy
from scrapy import Spider

from similarweb.items import *
from similarweb.settings import *
import pymysql
import logging
import json
from urllib.parse import quote



mysql = pymysql.connect(
    host='etl2.innotree.org',
    port=3308,
    user='spider',
    password='spider',
    db='spider',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor,
    use_unicode=True
)

def getValueFromJson(key, jsonValue):
    if key in jsonValue:
        return jsonValue[key]
    else:
        return None

# 抓取策略是先抓取 uv， 如果这个url没有uv的话就不抓取pv，节省api的调用次数
# 需要提前处理sUrl, 将http://www 这些东西去掉，只留下 jd.com 这样的一级域名，不然similarweb的数据请求不回来

class SimilarwebSpider(Spider):
    name = "similarweb"
    start_urls = [
        "http://www.baidu.com",
    ]


    def parse(self, response):
        logging.info("Enter similarweb spider...")
        with mysql.cursor() as cursor:
            sql = "SELECT `data_id` as `pid`, `data_info` as `domain_url` FROM `data_for_similarweb` where flag='1 'limit 100"
            #sql = "SELECT `id`, `sWeixinUrl` FROM `domain` WHERE `id` = 24"
            cursor.execute(sql)
            result = cursor.fetchall()
            for record in result:
                domain_url = record['domain_url']
                uv_item = SimilarwebUVItem()
                uv_item['pid'] = str(record['pid'])
                uv_item['domain_url'] = domain_url

                uv_api = "https://api.similarweb.com/v1/website/%s/total-traffic-and-engagement/visits?api_key=c51dd1b28735d715eefdb6034ed8e311&start_date=2017-05&end_date=2017-06&main_domain_only=false&granularity=Daily" % quote(domain_url)
                #uv_api = 'https://api.similarweb.com/v1/website/ele.me/total-traffic-and-engagement/visits?api_key=c51dd1b28735d715eefdb6034ed8e311&start_date=2017-05&end_date=2017-06&main_domain_only=false&granularity=Daily'
                request = scrapy.Request(uv_api, callback=self.parse_uv, dont_filter=True, errback=self.handle_error)
                request.meta['item'] = uv_item
                request.meta['dont_redirect'] = True
                logging.info("yield uv request for pid:%s url:%s", uv_item['pid'], uv_item['domain_url'])
                yield request

    def parse_uv(self, response):
        uv_item = response.meta['item']

        jsonresponse = json.loads(response.body_as_unicode())
        
        if jsonresponse['meta']['status'] == "Error":
            logging.info("This domain has no uv, pid:%s, url:%s", uv_item['pid'], uv_item['domain_url'])
            return
        else:
            print(uv_item)
            return
            logging.info("Get uv data, pid:%s, url:%s", uv_item['pid'], uv_item['domain_url'])
  
            pv_item = SimilarwebPVItem()
            pv_item['pid'] = uv_item['pid']
            pv_item['domain_url'] = uv_item['domain_url']

            pv_api = "https://api.similarweb.com/v1/website/%s/total-traffic-and-engagement/pages-per-visit?api_key=c51dd1b28735d715eefdb6034ed8e311&start_date=2017-05&end_date=2017-06&main_domain_only=false&granularity=Daily" % uv_item['domain_url']
            request = scrapy.Request(pv_api, priority=10, callback=self.parse_pv, dont_filter=True, errback=self.handle_error, headers=None)
            request.meta['item'] = pv_item
            request.meta['dont_redirect'] = True
            logging.info("yield pv request for pid:%s url:%s", pv_item['pid'], pv_item['domain_url'])
            yield request

        uv_item['start_date'] = jsonresponse['visits'][0]['date']
        uv_item['end_date'] = jsonresponse['visits'][-1]['date']
        uv_item['time_interval'] = uv_item['start_date'] + "----" + uv_item['end_date']
        uv_item['uv_json'] = jsonresponse
        yield uv_item

    def parse_pv(self, response):
        pv_item = response.meta['item']
        jsonresponse = json.loads(response.body_as_unicode())
        
        if jsonresponse['meta']['status'] == "Error":
            logging.info("This domain has no pv, pid:%s, url:%s", pv_item['pid'], pv_item['domain_url'])
            return
        else:
            logging.info("Get pv data, pid:%s, url:%s", pv_item['pid'], pv_item['domain_url'])
        
        pv_item['start_date'] = jsonresponse['pages_per_visit'][0]['date']
        pv_item['end_date'] = jsonresponse['pages_per_visit'][-1]['date']
        pv_item['time_interval'] = pv_item['start_date'] + "----" + pv_item['end_date']
        pv_item['pv_json'] = jsonresponse
        yield pv_item

    def handle_error(self, response):
        logging.info("request failure")
