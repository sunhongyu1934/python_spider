# -*- coding: utf-8 -*-
import scrapy
import re
import urllib
from scrapy.http import Request


class TaobaoSpider(scrapy.Spider):
	name = 'taobao'
	allowed_domains = ['taobao.com']
	#    allowed_domains = []
	start_urls = ['http://taobao.com/']

	def parse(self, response):
		key = '小吃'
		for i in range(0, 2):
			url = 'https://s.taobao.com/search?q=' + str(key) + '&s=' + str(44 * i)
			#            print url
			yield Request(url=url, callback=self.page)
		pass

	def page(self, response):
		body = response.body.decode('utf-8', 'ignore')
		pattam_id = '"nid":"(.*?)"'
		all_id = re.compile(pattam_id).findall(body)
		#	    print all_id

		for i in range(0, len(all_id)):
			#		print i
			this_id = all_id[i]
			#		print this_id
			url = 'https://item.taobao.com/item.htm?id=' + str(this_id)
			yield Request(url=url, callback=self.next)
			pass
		pass

	def next(self, response):
		#        print(response.url)
		url = response.url
		pattam_url = 'https://(.*?).com'
		subdomain = re.compile(pattam_url).findall(url)
		#	print subdomain
		if subdomain[0] != 'item.taobao':
			subSelector = response.xpath('//div[@class="tb-detail-hd"]')
			for sub in subSelector:
				title = sub.xpath('.//h1/text()').extract()[0]
			#		title = response.xpath("//div[@class='tb-detail-hd']/h1/text()").extract()
			pass
		else:
			subSelector = response.xpath('//h3[@class="tb-main-title"]')
			for sub in subSelector:
				title = sub.xpath('./@data-title').extract()[0]
			#		title = response.xpath("//h3[@class='tb-main-title']/@data-title").extract()
			pass
		#		print title
		if subdomain[0] != 'item.taobao':
			pattam_price = '"defaultItemPrice":"(.*?)"'
			price = re.compile(pattam_price).findall(response.body.decode('utf-8', 'ignore'))
			pass
		else:
			subSelector = response.xpath('//div[@class="tb-property-cont"]')
			for sub in subSelector:
				price = sub.xpath('.//em[2]/text()').extract()
			#           	 price = response.xpath("//em[@class = 'tb-rmb-num']/text()").extract()
			pass
		#		print price
		if subdomain[0] != 'item.taobao':
			pattam_id = 'id=(.*?)&'
			this_id = re.compile(pattam_id).findall(url)
			pass
		else:
			pattam_id = 'id=(.*?)$'
			this_id = re.compile(pattam_id).findall(url)
			pass
			#		print this_id
			comment_url = 'https://dsr-rate.tmall.com/list_dsr_info.htm?itemId=' + str(this_id).replace('\']','').replace(
				'[\'', '')
			comment_data = urllib.urlopen(comment_url).read().decode('utf-8', 'ignore')
			pattam_comment = '"rateTotal":(.*?),"'
			comment = re.compile(pattam_comment).findall(comment_data)
			pass
			print(comment)
		pass
