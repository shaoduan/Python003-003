# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SpidersItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()

    pass

class MaoYanmoveItem(scrapy.Item):
    film_name = scrapy.Field()
    film_type = scrapy.Field()
    film_release = scrapy.Field()
    
