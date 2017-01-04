# -*- coding:utf-8 -*-
import sys
reload(sys)
from scrapy.spider import BaseSpider
from scrapy.http import Request
from scrapy.selector import HtmlXPathSelector
from tutor_douban.items import TutorDoubanItem
import re
import os
import tutor_douban.database
import urllib
import json


class DoubanSpider(BaseSpider):
    name = "douban"  #唯一的命名方式，程序的入口
    allowed_domains = ["movie.douban.com"]
    start_urls = ["https://movie.douban.com/j/search_subjects?type=movie&tag=%E6%9C%80%E6%96%B0&page_limit=20&page_start=480"]
    movie_names_short = []
#    id_num = 0
    id_obj = tutor_douban.database.DBOperation()
    max_id = id_obj.select_data()
#    print max_id
    if max_id[0][0]:
        id_num = max_id[0][0]+1
    else:
        id_num = 0

#    start_urls = []
#    url_head = "https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%BB%8F%E5%85%B8&sort=recommend&page_limit=20&"
#    for i in range(0, 1):
#        start_page = "page_start=%s" % (20*i)
#        get_url = url_head + start_page
#        start_urls.append(get_url)
#    print start_urls

    def parse(self, response):
        data = json.loads(response.body)
        result = data['subjects']
     #   print result
#       *********for test,get one url**************
#        movie_link = result[1]['url']
#        self.movie_names_short.append(result[1]['title'])
#        self.movie_image_src = result[1]['cover']
#        yield Request(movie_link, callback=self.parse_item)

#    **************to get all urls*****************
        for i in range(len(result)):
            movie_link = result[i]['url']
            self.movie_names_short.append(result[i]['title'])
            movie_image_name = result[i]['title']
            movie_image_src = result[i]['cover']
            image_name = "%s.jpg" % movie_image_name
         #   print image_name
            image_path = os.path.join("E:\movie_pics", image_name)
            urllib.urlretrieve(movie_image_src, image_path)
            yield Request(movie_link, callback=self.parse_item)


#    自定义函数，用来处理新链接的request后获得的response
#    用于与Parse方法一起实现递归爬虫
    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)
        movie_name_long = hxs.select('//*[@id="content"]/h1/span[1]/text()').extract()
#        print movie_name_long[0]
        for name in self.movie_names_short:
            if re.search(name, movie_name_long[0]):
                movie_name = name
                break
            else:
                movie_name = movie_name_long
#        print '*********movie_name*************'
#        print movie_name
        movie_director = hxs.select('//*[@id="info"]/span[1]/span[2]/a/text()').extract()
#       print(movie_director[0])
        movie_writer = hxs.select('//*[@id="info"]/span[2]/span[2]/a/text()').extract()
        movie_rate = hxs.select('//*[@property="v:average"]/text()').extract()
#       print(movie_rate[0])

#       爬取电影详情需要在已有对象中继续爬取
        movie_description_paths = hxs.select('//*[@id="link-report"]')
        movie_description = movie_description_paths.select('.//*[@property="v:summary"]/text()').extract()

#       提取演员需要从已有的xPath对象中继续爬我要的内容
        movie_roles_paths = hxs.select('//*[@id="info"]/span[3]/span[2]')
        movie_roles = movie_roles_paths.select('.//*[@rel="v:starring"]/text()').extract()
#        print movie_roles[1]

#       获取电影详细信息序列
        movie_detail = hxs.select('//*[@id="info"]').extract()

#       电影详情信息字符串
        movie_detail_str = ''.join(movie_detail).strip()

        movie_language_str = ".*语言:</span> (.+?)<br><span.*".decode("utf8")
        movie_date_str = ".*上映日期:</span> <span property=\"v:initialReleaseDate\" content=\"(\S+?)\">(\S+?)</span>.*".decode("utf8")
        movie_long_str = ".*片长:</span> <span property=\"v:runtime\" content=\"(\d+).*".decode("utf8")

        pattern_language = re.compile(movie_language_str, re.S)
        pattern_date = re.compile(movie_date_str, re.S)
        pattern_long = re.compile(movie_long_str, re.S)

        movie_language = re.search(pattern_language, movie_detail_str)
        movie_date = re.search(pattern_date, movie_detail_str)
        movie_long = re.search(pattern_long, movie_detail_str)

        item = TutorDoubanItem()
#        print movie_url
#        item['movie_url'] = ''.join(movie_url).strip().replace(',', ';').replace('\'', '\\\'').replace('\"', '\\\"')
#        print item['movie_url']
        item['movie_id'] = self.id_num
#        print type(item['movie_id'])
        item['movie_name'] = ''.join(movie_name).strip().replace(',', ';').replace('\'', '\\\'').replace('\"', '\\\"').replace(':', ';')
        item['movie_rate'] = ''.join(movie_rate).strip().replace(',', ';').replace('\'', '\\\'').replace('\"', '\\\"').replace(':', ';')

        actor = ""
        for m in range(len(movie_roles)):
            actor = actor + movie_roles[m].strip().replace(',', ';').replace('\'', '\\\'').replace('\"', '\\\"').replace(':', ';') if len(movie_roles) > 0 else ''
        item['movie_roles'] = actor

        des = ""
        for k in range(len(movie_description)):
            des = des+movie_description[k].strip().replace(',', ';').replace('\'', '\\\'').replace('\"', '\\\"').replace(':', ';') if len(movie_description) > 0 else ''
        item['movie_description'] = des

        item['movie_writer'] = ';'.join(movie_writer).strip().replace(',', ';').replace('\'', '\\\'').replace('\"', '\\\"').replace(':', ';')
        item['movie_director'] = ';'.join(movie_director).strip().replace(',', ';').replace('\'', '\\\'').replace('\"', '\\\"').replace(':', ';')

        if movie_language:
            item['movie_language'] = movie_language.group(1).strip().replace(',',';').replace('\'','\\\'').replace('\"','\\\"').replace(':',';')

        item['movie_date'] = ""
        if movie_date:
            item['movie_date'] = movie_date.group(1).strip().replace(',', ';').replace('\'', '\\\'').replace('\"','\\\"').replace(':',';')

        item['movie_long'] = ""
        if movie_long:
            item['movie_long'] = movie_long.group(1)
        self.id_num += 1
        print item['movie_name']
        yield item





