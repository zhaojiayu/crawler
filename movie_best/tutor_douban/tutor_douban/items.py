# -*- coding: cp936 -*-
# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field


class TutorDoubanItem(Item):
    # define the fields for your item here like:
    # name = Field()
    movie_id = Field()
    # 电影名字
    movie_name = Field()
    # 电影评分
    movie_rate = Field()
    # 电影导演
    movie_director = Field()
    # 电影编剧
    movie_writer = Field()
    # 电影演员
    movie_roles = Field()
    # 电影语言
    movie_language = Field()
    # 电影上映时间
    movie_date = Field()
    # 电影市场：***分钟
    movie_long = Field()
    # 电影描述
    movie_description = Field()
    pass
