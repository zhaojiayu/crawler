# -*- coding:utf-8 -*-
# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field


class GetmovieurlItem(Item):
    # define the fields for your item here like:
    # 电影链接
    movie_url = Field()
    # 电影名字
    movie_name = Field()
    # 电影图片链接
    movie_picurl = Field()
    # name = Field()
    pass
