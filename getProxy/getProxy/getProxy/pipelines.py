# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import time

class GetproxyPipeline(object):
    def process_item(self, item, spider):
        today = time.strftime('%Y%m%d',time.localtime())
        fileName = today+'proxy360.txt'
        with open(fileName,'a',encoding='utf-8') as fp:
            fp.write(item['ip']+'\t')
            fp.write(item['port']+'\t')
            fp.write(item['type']+'\t\t')
            fp.write(item['location']+'\t\t')
            fp.write(item['protocol']+'\t\t')
            fp.write(item['source']+'\n\n')
	    #time.sleep(1)
        return item
