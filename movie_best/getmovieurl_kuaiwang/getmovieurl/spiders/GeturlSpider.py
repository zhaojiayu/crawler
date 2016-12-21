# -*- coding:utf-8 -*-
# __author__ = 'Administrator'
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from getmovieurl.items import GetmovieurlItem
import re
import getmovieurl.database
from scrapy.http import FormRequest


class GeturlSpider(BaseSpider):
    name = "movie_url"  #唯一的命名方式，程序的入口
    # 爬取酷爱网的片源
    allowed_domains = ["http://www.djkuai.com/"]
    name_obj = getmovieurl.database.DBOperation()
    movie_names = name_obj.select_data()
    print movie_names
    start_urls = ['http://www.djkuai.com/index.php/search']

    def parse(self, response):
        print response
        for data in self.movie_names:
        #    print data[0]
            form_data = {"wd": data[0].encode('utf-8').strip()}
         #   form_data = {"wd": "大鱼海棠"}
         #   print form_data
            yield FormRequest.from_response(response, formdata=form_data,
                                            callback=self.item_parse, dont_filter=True)

    def item_parse(self, response):
        print '********get url**********************'
 #       print response.body
    #    print 'ok'
        hxs = HtmlXPathSelector(response)
        item = GetmovieurlItem()
        mov_names = hxs.select('//*[@class="play-txt"]/h3/a/text()').extract()
        movie_img = hxs.select('//*[@class="play-img"]/img/@src').extract()
        movie_url = hxs.select('//*[@class="play-txt"]/h3/a/@href').extract()
        pre_url = "http://www.djkuai.com"
    #    print mov_names
    #    print movie_img
    #    print movie_url
    #    movie_name = hxs.select('//*[@class="col_c"]/@value').extract()
    #   能够找到movie_name，则对该movie的信息进行进一步判断爬取
        if mov_names:
            for i in range(len(mov_names)):
                print 'get here'
                print mov_names[i]
              #  print 'get database'
                for movie_name_x in self.movie_names:
               #     print movie_name_x[0]
                    # 查询到本页面内存在与数据库中movie_name一样的电影名的电影时，爬取该电影的信息
                    if mov_names[i] == movie_name_x[0]:
                        print 'same'
                        movie_name = mov_names[i]
                        movie_images = hxs.select('//*[@class="play-img"]/img/@src').extract()
                        movie_img = movie_images[i]
                        movie_urls = hxs.select('//*[@class="play-txt"]/h3/a/@href').extract()
                        movie_url = movie_urls[i]
                        break
                    else:
                        #print 'different'
                        movie_url = ''
                        movie_name = ''
                        movie_img = ''
                else:
                    continue
                break
        else:
            movie_url = ''
            movie_name = ''
            movie_img = ''

        item['movie_name'] = ''.join(movie_name).strip().replace(',', ';').replace('\'', '\\\'').replace('\"', '\\\"').replace(':', ';')
        item['movie_picurl'] = ''.join(movie_img).strip().replace(',', ';').replace('\'', '\\\'').replace('\"', '\\\"')
        item['movie_url'] = pre_url+''.join(movie_url).strip().replace(',', ';').replace('\'', '\\\'').replace('\"', '\\\"')

        yield item