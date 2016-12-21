# -*- coding: utf-8 -*-
#__author__ = 'Administrator'
import sys
##***********test1****************************
#file_object = open('E:\\tutor_douban\movie_name.txt', 'r')
#print('yiyu----------------')
#for line in file_object:
#    print(line)
#***********************************************
import urllib
import urllib2
import re
from scrapy.selector import HtmlXPathSelector


def h(url):
    revtal = urllib.urlretrieve(url)[0]


    print('*********000000000********')
    print(revtal)
    savepage(revtal)


def savepage(webpage):
    print('**11111111111111111***')
    print(webpage)
    print('***********************')
    f = open(webpage)
    lines = f.readlines()
    f.close()
    print('****2222222222222**********')
    print(lines)
    print('******************')
#    hxs = HtmlXPathSelector(f)
#    movie_url = hxs.select('//*[@class="playSource"]/@href').extract()
#    print movie_url[0]

if __name__ == '__main__':
    h(url='http://so.v.2345.com/search_%E8%BF%99%E4%B8%AA%E6%9D%80%E6%89%8B%E4%B8%8D%E5%A4%AA%E5%86%B7/')
#    h(url="https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%BB%8F%E5%85%B8&sort=recommend&page_limit=20&page_start=0")