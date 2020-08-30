# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from spiders.settings import DB_INFO
import datetime
#class SpidersPipeline:
#    def process_item(self, item, spider):
#        return item


class MaoYanPipeline:
    def process_item(self, item, spider):
        film_name = item['film_name']
        film_type = item['film_type']
        film_release = item['film_release']
        timestamp = int(datetime.datetime.now().timestamp())
        sql = f'REPLACE INTO movies(film_name, film_type, film_release, create_time) \
            VALUES("{film_name}", "{film_type}", "{film_release}", {timestamp})'
        with spider.store_backend.cursor() as cursor:
            cursor.execute(sql)
        spider.store_backend.commit()
        return item

    def open_spider(self, spider):
        mybackend = pymysql.connect(**DB_INFO, cursorclass=pymysql.cursors.DictCursor)
        spider.store_backend = mybackend

    def close_spider(self, spider):
        spider.store_backend.close()