#!/bin/env python3
#
# 作业1：
#     安装并使用 requests、bs4 库，爬取猫眼电影（）的前 10 个电影名称、电影类型和上映时间，
#     并以 UTF-8 字符集保存到 csv 格式的文件中。

import logging
import re
import sys

import requests
from bs4 import BeautifulSoup
from pandas import DataFrame

# set logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setLevel(logging.INFO)
# create formatter
fmt = "%(asctime)-15s %(levelname)s %(filename)s %(funcName)s %(lineno)d %(message)s"
datefmt = "%Y-%m-%d %H:%M:%S"
formatter = logging.Formatter(fmt, datefmt)
# add handler and formatter to logger
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

url = 'http://localhost/maoyan.html'
headers = {
    'user-agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0',
    "Referer": "https://www.baidu.com/",
}
output_file='/tmp/maoyan.csv'

try:
    respon = requests.get(url, headers=headers)
    logger.debug(f"Respon Code: {respon.status_code}")
    m = re.match('^(4|5)[0-9]+', str(respon.status_code))
    if m is not None:
        logger.error(f"Respon Faild: Status Code: {respon.status_code}")

    result = {
        'filmName': [],
        'filmType': [],
        'filmRelaseDate': [],
    }

    limit = 10  # top 10

    soup = BeautifulSoup(respon.content, features="html.parser")
    for movieInfo in soup.find_all('div', 'movie-hover-info'):
        filmNameRaw, filmTypeRaw, filmActorRaw, filmReleaseDateRaw = movieInfo.find_all(
            'div', 'movie-hover-title')
        result['filmName'].append(filmNameRaw.find('span', 'name').text)
        result['filmType'].append(filmTypeRaw.contents[2].strip())
        # filmActor = filmActorRaw.contents[2].strip() # No Need
        result['filmRelaseDate'].append(filmReleaseDateRaw.contents[2].strip())
        limit -= 1
        if limit == 0:
            break

    df = DataFrame(result)
    logger.debug(df)
    df.to_csv(output_file, sep=',', index=False)
except requests.exceptions.RequestException as e:
    logger.error(e)
