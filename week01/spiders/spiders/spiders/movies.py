# -*- coding: utf-8 -*-
import scrapy
#from bs4 import BeautifulSoup
from scrapy.selector import Selector
from spiders.items import MaoYanmoveItem
import re


class MoviesSpider(scrapy.Spider):
    name = 'movies'
    allowed_domains = ['maoyan.com']
    #start_urls = ['http://maoyan.com/maoyan.html']
    start_urls = ['https://maoyan.com/films?showType=3']

#    def parse(self, response):
#        items = []
#        soup = BeautifulSoup(response.text, features="html.parser")
#        limit = 10  # top 10
#        for movieInfo in soup.find_all('div', 'movie-hover-info'):
#            item = MaoYanmoveItem()
#            filmNameRaw, filmTypeRaw, filmActorRaw, filmReleaseDateRaw = movieInfo.find_all(
#                'div', 'movie-hover-title')
#            item['film_name'] = filmNameRaw.find('span', 'name').text
#            item['film_type'] = filmTypeRaw.contents[2].strip()
#            item['film_release'] = filmReleaseDateRaw.contents[2].strip()
#            items.append(item)
#            limit -= 1
#            if limit == 0:
#                break
#        return items

    def parse(self, response):
        items = []
        movies = selector = Selector(response=response).xpath('//dl[@class="movie-list"]//div[@class="movie-item film-channel"]')
        limit = 10  # top 10
        for movie in movies:
            item = MaoYanmoveItem()
            item['film_name'] = movie.xpath('.//span[@class="name "]/text()')[0].extract()
            item['film_type'] = re.sub('\s|\n', "", movie.xpath('.//div[@class="movie-hover-title"]/text()')[4].extract())
            item['film_release'] = re.sub('\s|\n', "", movie.xpath('.//div[@class="movie-hover-title movie-hover-brief"]//text()')[2].extract())
            items.append(item)
            limit -= 1
            if limit == 0:
                break
        return items
