# -*- coding:utf-8 -*-
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
import database


class GetmovieurlPipeline(object):
    def __init__(self):
        self.db = database.DBOperation()

    def process_item(self, item, spider):
        if item['movie_url']:
            if item['movie_url'] == 'url':
                print 'no url'
            else:
                self.db.update_data(item)
        else:
            print 'no this movie'
         #   self.db.delete_col(item)

        return item

    def close_spider(self, spider):
        results = self.db.select_col()
        data = {}
        for i in range(len(results)):
            if results[i][1]:
                continue
            else:
                data['movie_name'] = results[i][0]
                self.db.delete_col(data)
        self.db.dis_conn()
