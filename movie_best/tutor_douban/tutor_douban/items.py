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
    # ��Ӱ����
    movie_name = Field()
    # ��Ӱ����
    movie_rate = Field()
    # ��Ӱ����
    movie_director = Field()
    # ��Ӱ���
    movie_writer = Field()
    # ��Ӱ��Ա
    movie_roles = Field()
    # ��Ӱ����
    movie_language = Field()
    # ��Ӱ��ӳʱ��
    movie_date = Field()
    # ��Ӱ�г���***����
    movie_long = Field()
    # ��Ӱ����
    movie_description = Field()
    pass
