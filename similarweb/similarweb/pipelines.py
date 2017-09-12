# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
import logging


from similarweb.settings import *
from similarweb.items import *

'''
# mongo
similarweb_uv_collection = 'similarweb_uv'
similarweb_pv_collection = 'similarweb_pv'

# hbase
connection = happybase.Connection(host="10.45.146.248", port=9090, timeout=10000)
hbase_table = connection.table("project_factor_value_origin")
'''
# mysql
mysql = pymysql.connect(
    host='etl2.innotree.org',
    port=3308,
    user='spider',
    password='spider',
    db='dw_online',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor,
    use_unicode=True
)

mysql2 = pymysql.connect(
    host= 'etl2.innotree.org',
    port=3308,
    user='spider',
    password='spider',
    db='dw_online',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor,
    use_unicode=True
)
'''
class MongoPipeline(object):
    def __init__(self):
        self.mongo_uri = MONGO_URI
        self.mongo_db = MONGO_DATABASE

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        if isinstance(item, SimilarwebUVItem):
            try:
                ret = self.db[similarweb_uv_collection].insert_one(dict(item))
                item['mongo_id'] = str(ret.inserted_id)
                logging.info("Success insert uv into mongodb for pid:%s, mongo_id:%s", item['pid'], str(ret.inserted_id))

            except:
                item['mongo_id'] = "0"
                logging.info("Insert uv into mongodb failed pid:%s", item['pid'])

            return item

        elif isinstance(item, SimilarwebPVItem):
            try:
                ret = self.db[similarweb_pv_collection].insert_one(dict(item))
                item['mongo_id'] = str(ret.inserted_id)
                logging.info("Success insert pv into mongodb for pid:%s, mongo_id:%s", item['pid'], str(ret.inserted_id))

            except:
                item['mongo_id'] = "0"
                logging.info("Insert pv into mongodb failed pid:%s", item['pid'])
            
            return item
            
        else:
            return item

class HBasePipeline(object):
    
    def process_item(self, item, spider):
        
        if isinstance(item, SimilarwebUVItem):
            for uv_value in item['uv_json']['visits']:
                row_key = item['pid'] + '_' + uv_value['date'].replace("-", "")
                value_dict = {}
                value_dict[b'data:host'] = bytes(item['domain_url'])
                value_dict[b'data:sim_uv'] = bytes(uv_value['visits'])

                hbase_table.put(bytes(row_key), value_dict)
            logging.info("insert similarweb_uv into hbase ok, pid:%s, start_date:%s, end_date:%s", item['pid'], item['start_date'], item['end_date'])
            return item

        elif isinstance(item, SimilarwebPVItem):
            for pv_value in item['pv_json']['pages_per_visit']:
                row_key = item['pid'] + '_' + pv_value['date'].replace("-", "")
                value_dict = {}
                value_dict[b'data:host'] = bytes(item['domain_url'])
                value_dict[b'data:sim_ppv'] = bytes(pv_value['pages_per_visit'])

                hbase_table.put(bytes(row_key), value_dict)
            logging.info("insert similarweb_pv into hbase ok, pid:%s, start_date:%s, end_date:%s", item['pid'], item['start_date'], item['end_date'])
            return item
'''
class MySQLPipeline(object):

    def process_item(self, item, spider):
        
        if isinstance(item, SimilarwebUVItem):
            with mysql2.cursor() as cursor:
                update_sql = "UPDATE `domain` SET `flag`=1 where `id` = %s"
                cursor.execute(update_sql, item['pid'])
            mysql2.commit()
            logging.info("update titan ok, pid:%s", item['pid'])

            with mysql.cursor() as cursor:
                insert_sql = "INSERT INTO `similarweb_uv` (`pid`, `domain_url`, `uv_json`, `time1`, `mongo_id`) VALUES(%s, %s, %s, %s, %s)"
                insert_sql_item = "INSERT INTO `similarweb_uv_item` (`pid`, `domain_url`, `date1`, `uv_value`) VALUES(%s, %s, %s, %s)"

                try:
                    cursor.execute(insert_sql, (item['pid'], item['domain_url'], str(item['uv_json']['visits']), item['time_interval'], '0'))
                    for uv_item in item['uv_json']['visits']:
                        date = uv_item['date'].replace('-','')
                        uv_value = uv_item['visits']
                        cursor.execute(insert_sql_item, (item['pid'], item['domain_url'], date, uv_value))

                except Exception as e:
                    logging.error("insert similarweb_uv exception, pid:%s", item['pid'])
                    logging.error(e)
                    return
                
            mysql.commit()
            logging.info("insert similarweb_uv into mysql ok, pid:%s", item['pid'])
            return item

        elif isinstance(item, SimilarwebPVItem):
            with mysql.cursor() as cursor:
                insert_sql = "INSERT INTO `similarweb_pv` (`pid`, `domain_url`, `pv_json`, `time1`, `mongo_id`) VALUES(%s, %s, %s, %s, %s)"
                insert_sql_item = "INSERT INTO `similarweb_pv_item` (`pid`, `domain_url`, `date1`, `pv_value`) VALUES(%s, %s, %s, %s)"

                try:
                    cursor.execute(insert_sql, (item['pid'], item['domain_url'], str(item['pv_json']['pages_per_visit']), item['time_interval'], '0'))
                    for pv_item in item['pv_json']['pages_per_visit']:
                        date = pv_item['date'].replace('-','')
                        pv_value = pv_item['pages_per_visit']
                        cursor.execute(insert_sql_item, (item['pid'], item['domain_url'], date, pv_value))

                except Exception as e:
                    logging.error("insert similarweb_pv exception, pid:%s", item['pid'])
                    logging.error(e)
                    return item
                
            mysql.commit()
            logging.info("insert similarweb_pv into mysql ok, pid:%s", item['pid'])
            return item

    def close_spider(spider):
        mysql.close()
