# -*- coding: utf-8 -*-
# Define your item pipelines here
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html


# from scrapy import signals
# import json
# import codecs
from twisted.enterprise import adbapi
from datetime import datetime
from hashlib import md5
import MySQLdb
import MySQLdb.cursors
import database


class TutorDoubanPipeline(object):
    def __init__(self):
        self.db = database.DBOperation()

    def process_item(self, item, spider):
        self.db.insert_data(item)
        return item

    def close_spider(self, spider):
        self.db.dis_conn()



# class JsonWithEncodingCnblogsPipeline(object):
#    def __init__(self):
#        self.file = codecs.open('cnblogs.json', 'w', encoding='utf-8')

#    def process_item(self, item, spider):
#        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
#        self.file.write(line)
#        return item

#    def spider_closed(self, spider):
#        self.file.close()

'''
class TutorDoubanPipeline(object):
    def __init__(self):
        self.dbpool = adbapi.ConnectionPool(
            'MySQLdb',
            host="192.168.1.108",
            user='user',
            passwd='user',
            port=3306,
            charset='utf8',
            cursorclass=MySQLdb.cursors.DictCursor,
            use_unicode=True
            )
#        self.dbpool = dbpool

#   读取数据库配置文件，并生成数据库实例
#    @classmethod
#    def from_settings(cls, settings):
#        dbargs = dict(
#            host='192.168.1.108',
#            db='movie',
#            user='user',
#            passwd='user',
#            charset='utf8',
#            cursorclass=MySQLdb.cursors.DictCursor,
#            use_unicode=True,
#        )
#       与数据库建立链接
#        dbpool = adbapi.ConnectionPool('MySQLdb', **dbargs)
#        return cls(dbpool)

#   pipeline默认调用
    def process_item(self, item):
        print item
        d = self.dbpool.runInteraction(self._do_upinsert, item)
#        d = self.dbpool.runInteraction(database.Insert.InsertData, item, spider)
#        d.addErrback(self._handle_error, item)
#        d.addBoth(lambda _: item)
        return item
#        return d


#    将每行更新或写入数据库中
    def _do_upinsert(self, conn, item):
        execute_sql = "insert into best_movies(movie_name,movie_rate, movie_direct,\
                      movie_writer,movie_roles,movie_language,movie_date,movie_long,movie_description,movie_url) \
                      values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        param = (item['movie_name'], item['movie_rate'], item['movie_director'], item['movie_writer'],
                       item['movie_roles'], item['movie_language'], item['movie_date'], item['movie_long'],
                       item['movie_description'], item['movie_url'])
        execute_sql1 = "insert into best_movies values('yyy', 'zzz', 'movie_direct',\
                             'movie_writer', 'movie_roles', 'movie_language','movie_date', 'movie_long',\
                             'movie_description', 'movie_url')"
        print('********database********************')
        print execute_sql
        conn.execute(execute_sql, param)

#        linkmd5id = self._get_linkmd5id(item)
        #print linkmd5id
#        now = datetime.utcnow().replace(microsecond=0).isoformat(' ')
#        conn.execute("""
#                select 1 from cnblogsinfo where linkmd5id = %s
#        """, (linkmd5id, ))
#        ret = conn.fetchone()

#        if ret:
            conn.execute("""
                update cnblogsinfo set title = %s, description = %s, link = %s, listUrl = %s, updated = %s where linkmd5id = %s
            """, (item['title'], item['desc'], item['link'], item['listUrl'], now, linkmd5id))
            #print """
            #    update cnblogsinfo set title = %s, description = %s, link = %s, listUrl = %s, updated = %s where linkmd5id = %s
            #""", (item['title'], item['desc'], item['link'], item['listUrl'], now, linkmd5id)
        else:
            conn.execute("""
                insert into cnblogsinfo(linkmd5id, title, description, link, listUrl, updated)
                values(%s, %s, %s, %s, %s, %s)
            """, (linkmd5id, item['title'], item['desc'], item['link'], item['listUrl'], now))
            #print """
            #    insert into cnblogsinfo(linkmd5id, title, description, link, listUrl, updated)
            #    values(%s, %s, %s, %s, %s, %s)
            #""", (linkmd5id, item['title'], item['desc'], item['link'], item['listUrl'], now)

    #获取url的md5编码
#    def _get_linkmd5id(self, item):
        #url进行md5处理，为避免重复采集设计
#        return md5(item['link']).hexdigest()
    #异常处理

#    def _handle_error(self, failue, item, spider):
#        log.err(failure)

if __name__ == '__main__':
    value = {"movie_name":" u'\u8fd9\u4e2a\u6740\u624b\u4e0d\u592a\u51b7 L\xe9on",
             "movie_rate":" u'9.4","movie_direct":"zhaojiayu",
             "movie_writer":"zhaojiayu","movie_roles":"zhaojiayu",
             "movie_language":" u'\u82f1\u8bed / \u610f\u5927\u5229\u8bed / \u6cd5\u8bed",
             "movie_date":"zhaojiayu",
             "movie_long":"zhaojiayu","movie_description":"zhaojiayu","movie_url":"zhaojiayu"}
    print value
    obj = TutorDoubanPipeline()

    obj.process_item(value)



import json
import codecs
import database'''
