# coding:utf-8

from __future__ import print_function
import requests
import time
import re
import os
import sys
import random
# sys.setrecursionlimit(20)
try:
	from urllib import quote
except:
	from urllib.parse import quote


class UserAgent(object):
	ua_list = [
		'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
		'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
		'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
		'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko',
		'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;',
		'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;',
		'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
		'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
		'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
		'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
		'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
		'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)',
		'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)',
		'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
		'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)',
		'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)',
		'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)',
		'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)',
		'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
		"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
		"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
		"Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
		"Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
		"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
		"Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
		"Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
		"Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
		"Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
		"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
		"Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
		"Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
		"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
		"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
		"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
		"Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
	]

	@property
	def random(self):
		return random.choice(self.ua_list)

try:
	from fake_useragent import UserAgent
except:
	print('import fakeUA fail')
finally:
	ua = UserAgent()


# from settings import sgattrs, type_api_dic

base_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(base_path)


sgattrs = [
	["6", "b", "t", "f", "2", "z", "l", "5", "w", "h", "q", "i", "s", "e", "c", "p", "m", "u", "9", "8", "y",
	 "k", "j", "r", "x", "n", "-", "0", "3", "4", "d", "1", "a", "o", "7", "v", "g"],
	["1", "8", "o", "s", "z", "u", "n", "v", "m", "b", "9", "f", "d", "7", "h", "c", "p", "y", "2", "0", "3",
	 "j", "-", "i", "l", "k", "t", "q", "4", "6", "r", "a", "w", "5", "e", "x", "g"],
	["s", "6", "h", "0", "p", "g", "3", "n", "m", "y", "l", "d", "x", "e", "a", "k", "z", "u", "f", "4", "r",
	 "b", "-", "7", "o", "c", "i", "8", "v", "2", "1", "9", "q", "w", "t", "j", "5"],
	["x", "7", "0", "d", "i", "g", "a", "c", "t", "h", "u", "p", "f", "6", "v", "e", "q", "4", "b", "5", "k",
	 "w", "9", "s", "-", "j", "l", "y", "3", "o", "n", "z", "m", "2", "1", "r", "8"],
	["z", "j", "3", "l", "1", "u", "s", "4", "5", "g", "c", "h", "7", "o", "t", "2", "k", "a", "-", "e", "x",
	 "y", "b", "n", "8", "i", "6", "q", "p", "0", "d", "r", "v", "m", "w", "f", "9"],
	["j", "h", "p", "x", "3", "d", "6", "5", "8", "k", "t", "l", "z", "b", "4", "n", "r", "v", "y", "m", "g",
	 "a", "0", "1", "c", "9", "-", "2", "7", "q", "e", "w", "u", "s", "f", "o", "i"],
	["8", "q", "-", "u", "d", "k", "7", "t", "z", "4", "x", "f", "v", "w", "p", "2", "e", "9", "o", "m", "5",
	 "g", "1", "j", "i", "n", "6", "3", "r", "l", "b", "h", "y", "c", "a", "s", "0"],
	["d", "4", "9", "m", "o", "i", "5", "k", "q", "n", "c", "s", "6", "b", "j", "y", "x", "l", "a", "v", "3",
	 "t", "u", "h", "-", "r", "z", "2", "0", "7", "g", "p", "8", "f", "1", "w", "e"],
	["7", "-", "g", "x", "6", "5", "n", "u", "q", "z", "w", "t", "m", "0", "h", "o", "y", "p", "i", "f", "k",
	 "s", "9", "l", "r", "1", "2", "v", "4", "e", "8", "c", "b", "a", "d", "j", "3"],
	["1", "t", "8", "z", "o", "f", "l", "5", "2", "y", "q", "9", "p", "g", "r", "x", "e", "s", "d", "4", "n",
	 "b", "u", "a", "m", "c", "h", "j", "3", "v", "i", "0", "-", "w", "7", "k", "6"]]

type_api_dic = {
	'company': "http://www.tianyancha.com/v2/company/{id}.json",
	'search': 'http://www.tianyancha.com/v2/search/{keys}.json?',
	'getInfoById': "http://dis.tianyancha.com/dis/getInfoById/{id}.json?",
	'pv': 'http://pv.tianyancha.com/pv?url=/company/{id}',
	'f_isfm': 'http://www.tianyancha.com/f/isfm.json?&id={id}',
	'stock_count': 'http://www.tianyancha.com/stock/count.json?graphId={id}',
	'search_getNewCompanyName': 'http://www.tianyancha.com/v2/search/getNewCompanyName.json?companyName={keys}',
	'expanse_getAll': 'http://www.tianyancha.com/expanse/getAll.json?id={id}',
	'wxApi_getJsSdkConfig': 'http://www.tianyancha.com/wxApi/getJsSdkConfig.json?url=http%%3A%%2F%%2Fwww.tianyancha.com%%2Fcompany%%2F{id}',
	'exist': 'http://dis.tianyancha.com/dis/exist/{id}.json',
	'near_s': 'http://www.tianyancha.com/v2/near/s.json?id={id}&pn=1',
	'updatetime': 'http://www.tianyancha.com/v2/updatetime/{id}.json?random={random}',
	'getnews': 'http://www.tianyancha.com/v2/getnews/{keys}.json',
	'expanse_staff': 'http://www.tianyancha.com/expanse/staff.json?id={id}&ps=20&pn=1',
	'expanse_holder': 'http://www.tianyancha.com/expanse/holder.json?id={id}&ps=20&pn=1',
	'expanse_inverst': 'http://www.tianyancha.com/expanse/inverst.json?id={id}&ps=20&pn=1',
	'expanse_changeinfo': 'http://www.tianyancha.com/expanse/changeinfo.json?id={id}&ps=5&pn=1',
	'expanse_annu': 'http://www.tianyancha.com/expanse/annu.json?id={id}&ps=5&pn=1',
	'expanse_findHistoryRongzi': 'http://www.tianyancha.com/expanse/findHistoryRongzi.json?name={keys}&ps=10&pn=1',
	'expanse_findTeamMember': 'http://www.tianyancha.com/expanse/findTeamMember.json?name={keys}&ps=5&pn=1',
	'expanse_findProduct': 'http://www.tianyancha.com/expanse/findProduct.json?name={keys}&ps=15&pn=1',
	'expanse_findTzanli': 'http://www.tianyancha.com/expanse/findTzanli.json?name={keys}&ps=10&pn=1',
	'expanse_findJingpin': 'http://www.tianyancha.com/expanse/findJingpin.json?name={keys}&ps=10&pn=1',
	'getlawsuit': 'http://www.tianyancha.com/v2/getlawsuit/{keys}.json?page=1&ps=10',
	'court': 'http://www.tianyancha.com/v2/court/{keys}.json?',
	'expanse_zhixing': 'http://www.tianyancha.com/expanse/zhixing.json?id={id}&pn=1&ps=5',
	'expanse_companyEquity': 'http://www.tianyancha.com/expanse/companyEquity.json?name={keys}&ps=5&pn=1',
	'expanse_bid': 'http://www.tianyancha.com/expanse/bid.json?id={id}&pn=1&ps=10',
	'extend_getEmploymentList': 'http://www.tianyancha.com/extend/getEmploymentList.json?companyName={keys}&pn=1&ps=10',
	'expanse_taxcredit': 'http://www.tianyancha.com/expanse/taxcredit.json?id={id}&ps=5&pn=1',
	'expanse_companyCheckInfo': 'http://www.tianyancha.com/expanse/companyCheckInfo.json?name={keys}&pn=1&ps=5',
	'expanse_appbkinfo': 'http://www.tianyancha.com/expanse/appbkinfo.json?id={id}&ps=5&pn=1',
	'tm_getTmList': 'http://www.tianyancha.com/tm/getTmList.json?id={id}&pageNum=1&ps=5',
	'expanse_patent': 'http://www.tianyancha.com/expanse/patent.json?id={id}&pn=1&ps=5',
	'expanse_copyReg': 'http://www.tianyancha.com/expanse/copyReg.json?id={id}&pn=1&ps=5',
	'IcpList': 'http://www.tianyancha.com/v2/IcpList/{id}.json',
}


class GetApi(object):
	def __init__(self, type_api=None, id=None, keys=None, proxies=None, max_retries=7):
		self.type_api = type_api
		self.id = id
		self.keys = keys
		self.proxies = proxies
		self.max_retries = max_retries

		self.session = requests.session()
		self.api_headers = {
			"User-Agent": ua.random,
			"Accept": "application/json, text/plain, */*",
			"Accept-Encoding": "gzip, deflate",
			"Tyc-From": "normal",
			'Host': 'www.tianyancha.com',
			"Referer": "http://www.tianyancha.com/company/{id}".format(id=self.id),
		}

	def __format_api(self, value):
		args = {}
		if '{id}' in value:
			args['id'] = self.id
		if '{keys}' in value:
			args['keys'] = quote(self.keys)
		if '{random}' in value:
			args['random'] = int(time.time()) * 1000
		return value.format(**args)

	def __set_cookie(self, tongji_url, to='token', u='_utm'):
		if self.proxies:
			tongji_page = self.session.request("GET", tongji_url, headers=self.api_headers, proxies=self.proxies)
		else:
			print('use local ip!')
			tongji_page = self.session.request("GET", tongji_url, headers=self.api_headers)

		if not tongji_page:
			self.max_retries -= 1
			if not self.max_retries:
				print('max retries tongji')
				exit(1)
			print('no tongji result! retrying!')
			#time.sleep(1)
			self.__set_cookie(tongji_url, to='token', u='_utm')

		js_code = "".join([chr(int(code)) for code in tongji_page.json()["data"]["v"].split(",")])
		token = re.findall(r"token=(\w+);", js_code)[0]

		fxck_chars = re.findall(r"\'([\d\,]+)\'", js_code)[0].split(",")
		parm = self.keys if self.type_api == 'search' else str(self.id)
		index = int(str(ord(parm[0]))[1])
		sogou = sgattrs[index]
		utm = "".join([sogou[int(fxck)] for fxck in fxck_chars])

		self.session.cookies.set(to, token)
		self.session.cookies.set(u, utm)

	def get_api(self):
		if self.type_api == 'company':
			tongji_url = 'http://www.tianyancha.com/tongji/{id}.json?random={random}'.format(id=self.id, random=int(time.time()) * 1000)
			self.__set_cookie(tongji_url)
		elif self.type_api == 'search':
			tongji_url = 'http://www.tianyancha.com/tongji/{keys}.json?random={random}'.format(keys=quote(self.keys), random=int(time.time()) * 1000)
			self.api_headers.update({
				"Referer": 'http://www.tianyancha.com/search?key={keys}&checkFrom=searchBox'.format(keys=quote(self.keys)),
			})
			self.__set_cookie(tongji_url)
		elif self.type_api == 'getInfoById':
			tongji_url = "http://dis.tianyancha.com/qq/{id}.json?random={random}".format(id=self.id, random=int(time.time()) * 1000)
			self.api_headers.update({
				'Host': 'dis.tianyancha.com',
				'Referer': 'http://dis.tianyancha.com/dis/old'
			})
			self.__set_cookie(tongji_url, to='rtoken', u='_rutm')
		api_url = self.__format_api(type_api_dic.get(self.type_api, type_api_dic['IcpList']))
		if self.proxies:
			api_page = self.session.request('GET', api_url, headers=self.api_headers, proxies=self.proxies)
		else:
			print('use local ip!')
			api_page = self.session.request('GET', api_url, headers=self.api_headers)
		if not api_page:
			self.max_retries -= 1
			if not self.max_retries:
				print('max retries json')
				exit(1)
			print('no json result! retrying!')
			time.sleep(1)
			self.get_api()
		return api_page.text

def get_json(type=None, id=None, keys=None, proxies=None):
	if type is None:
		type = input('%s\nPlease input a type upside: ' % str(type_api_dic.keys()))
		if not type or type not in type_api_dic.keys():
			get_json(type=None, id=None, keys=None, proxies=None)
	if not id:
		if '{id}' in type_api_dic[type]:
			id = input('Please input id: ')
			if not id:
				get_json(type=None, id=None, keys=None, proxies=None)
	if not keys:
		if '{keys}' in type_api_dic[type]:
			keys = input('Please input keys: ')
			if not keys:
				get_json(type=None, id=None, keys=None, proxies=None)

	api = GetApi(type_api=type, id=id, keys=keys, proxies=proxies)
	return api.get_api()

if __name__ == '__main__':
    # api = GetApi(type_api='company', id=24722813)
    # api = GetApi(type_api='search', keys='中译语通科技（北京）有限公司')
    # api = GetApi(type_api='getInfoById', id=24722813)
    # api = GetApi(type_api='IcpList', id=24722813, keys='中译语通科技（北京）有限公司')
    # 代理服务器
    proxyHost = "proxy.abuyun.com"
    proxyPort = "9020"

    # 代理隧道验证信息
    proxyUser = "HU5DU38W4JUS429D"
    proxyPass = "E90AAF44448EEEC4"

    proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
	    "host": proxyHost,
	    "port": proxyPort,
	    "user": proxyUser,
	    "pass": proxyPass,
    }

    proxies = {
	    "http": proxyMeta,
	    "https": proxyMeta,
    }
    """
    所有type类型：
    ['company', 'search', 'getInfoById', 'pv', 'f_isfm', 'stock_count', 'search_getNewCompanyName', 'expanse_getAll', 'wxApi_getJsSdkConfig', 'exist', 'near_s', 'updatetime', 'getnews', 'expanse_staff', 'expanse_holder', 'expanse_inverst', 'expanse_changeinfo', 'expanse_annu', 'expanse_findHistoryRongzi', 'expanse_findTeamMember', 'expanse_findProduct', 'expanse_findTzanli', 'expanse_findJingpin', 'getlawsuit', 'court', 'expanse_zhixing', 'expanse_companyEquity', 'expanse_bid', 'extend_getEmploymentList', 'expanse_taxcredit', 'expanse_companyCheckInfo', 'expanse_appbkinfo', 'tm_getTmList', 'expanse_patent', 'expanse_copyReg', 'IcpList']
    """
    json = get_json(type='company', id=24722813)
    print(json)