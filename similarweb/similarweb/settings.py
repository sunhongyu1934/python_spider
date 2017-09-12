# -*- coding: utf-8 -*-

# Scrapy settings for similarweb project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
# test git
BOT_NAME = 'similarweb'

SPIDER_MODULES = ['similarweb.spiders']
NEWSPIDER_MODULE = 'similarweb.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# LOG_FILE = 'log/similarweb.log'
LOG_LEVEL = 'DEBUG'

CONCURRENT_REQUESTS = 32

# DataBase Setting
#REDIS_HOST = 'localhost'
#MONGO_URI = 'mongodb://123.57.217.48:27017'
#MONGO_URI = 'mongodb://root:innotree_mongodb@10.44.51.90:27017'

#MONGO_DATABASE = 'similarweb'

#XUNDAILI_HTTP_URL = 'http://www.xdaili.cn/ipagent/privateProxy/applyStaticProxy?count=1&spiderId=33c0ced745ff4d338376160ae8cb198f&returnType=2'

DOWNLOAD_DELAY = 0
DOWNLOAD_TIMEOUT = 20

RETRY_TIMES = 32
RETRY_HTTP_CODES = [500, 502, 503, 504, 400, 402, 401, 403, 404, 408, 429, 301, 304]

# Disable cookies (enabled by default)
COOKIES_ENABLED = False
# COOKIES_DEBUG = False

AUTOTHROTTLE_ENABLED = False
AUTOTHROTTLE_DEBUG = False

DOWNLOADER_MIDDLEWARES = {
    #'similarweb.misc.middlewares.ProxyMiddleware': 546,
    #'similarweb.misc.middlewares.InnoProxy': 600
}

ITEM_PIPELINES = {
   #'similarweb.pipelines.MongoPipeline': 300,
  # 'similarweb.pipelines.HBasePipeline': 450,
   'similarweb.pipelines.MySQLPipeline': 600,
}

# EXTENSIONS = {
#     'scrapy.misc.extensions.LogStats': 500,
# }

# scrapy-redis configuration
# Enables scheduling storing requests queue in redis.
#启用Redis调度存储请求队列
#SCHEDULER = "scrapy_redis.scheduler.Scheduler"

# Ensure all spiders share same duplicates filter through redis.
#确保所有的爬虫通过Redis去重
#DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
