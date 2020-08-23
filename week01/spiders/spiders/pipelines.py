# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


#class SpidersPipeline:
#    def process_item(self, item, spider):
#        return item

class MaoYanPipeline:
    def process_item(self, item, spider):
        film_name = item['film_name']
        film_type = item['film_type']
        film_release = item['film_release']
        output = f'{film_name},{film_type},{film_release}\n'
        with open('/tmp/maoyanmoive.txt', 'a+', encoding='utf-8') as result:
            result.write(output)
        return item
