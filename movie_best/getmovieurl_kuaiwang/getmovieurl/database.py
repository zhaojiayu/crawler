# -*- coding:utf-8 -*-

import MySQLdb
from getmovieurl.items import GetmovieurlItem


class CreateDB():
    def __init__(self):
        self.host = "139.196.29.97"
        self.conn = MySQLdb.connect(self.host, user='root', passwd='TRzjy123', port=3306, charset='utf8', use_unicode=True)
        self.cur = self.conn.cursor()

    def create_database(self):
        create_db_sql = 'CREATE DATABASE movie DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci'
        self.cur.execute(create_db_sql)

    def create_table(self):
        self.conn.select_db('movie')
        self.cur.execute("create table best_movies( movie_name varchar(100), movie_rate varchar(10), \
                              movie_direct varchar(100), movie_writer varchar(100), \
                             movie_roles varchar(100), movie_language varchar(100), \
                             movie_date varchar(20), movie_long varchar(10), movie_description varchar(1500),\
                             movie_url varchar(100))")


class DBOperation():
    def __init__(self):
        self.conn = MySQLdb.connect(host="139.196.29.97", db='movie', user='root', passwd='TRzjy123', port=3306, charset='utf8', use_unicode=True)
        self.cur = self.conn.cursor()

    def update_data(self, value):
        try:
            sql = "UPDATE best_movies SET movie_url = '%s',movie_picurl = '%s' WHERE movie_name = '%s'" % (value['movie_url'], value['movie_picurl'], value['movie_name'])
            self.cur.execute(sql)

        except MySQLdb.Error, e:
            print "Mysql Error %d : %s" % (e.args[0], e.args[1])

    def select_data(self):
        try:
            max_sql = "SELECT max(movie_id) FROM best_movies WHERE movie_url !=''"
            self.cur.execute(max_sql)
            number = self.cur.fetchall()
            print number
            if number[0][0]:
                print 'not none'
                sql = "SELECT movie_name FROM best_movies WHERE movie_id > %s" % number[0][0]
            else:
                print 'none'
                sql = "SELECT movie_name FROM best_movies"
        #    print sql
            self.cur.execute(sql)
            results = self.cur.fetchall()
            return results
          #  print results
          #  for i in range(len(results)):
          #      print results[i][0]
        except MySQLdb.Error, e:
            print "Mysql Error %d : %s" % (e.args[0], e.args[1])

    def select_col(self):
        try:
            sel_col_sql = "SELECT movie_name,movie_url FROM best_movies"
            self.cur.execute(sel_col_sql)
            sel_col_results = self.cur.fetchall()
            return sel_col_results
         #   print sel_col_results
          #  for i in range(len(sel_col_results)):
           #     print sel_col_results[i][1]
            #    data = {}
            #    if sel_col_results[i][1]:
            #        print 'yes'
            #        continue
            #    else:
            #        print 'none'
            #        data['movie_name'] = sel_col_results[i][0]
            #        self.delete_col(data)
        except MySQLdb.Error, e:
            print "Mysql Error %d : %s" % (e.args[0], e.args[1])

    def delete_col(self, value):
        try:
            del_col_sql = "DELETE FROM best_movies WHERE movie_name = '%s'" % value['movie_name']
          #  del_col_sql = "DELETE FROM old_movies WHERE movie_name = 'yy'"
        #    print del_col_sql
            self.cur.execute(del_col_sql)
        except MySQLdb.Error, e:
            print "Mysql Error %d : %s" % (e.args[0], e.args[1])

    def dis_conn(self):
            self.conn.commit()
            self.cur.close()
            self.conn.close()


if __name__ == '__main__':
    value = {"movie_name": u'V\u5b57\u4ec7\u6740\u961f',
#             "movie_rate":"yiyu",
#             "movie_director":"yiyu",
#             "movie_writer":"yiyu",
#             "movie_roles":"zhaojiayu",
#             "movie_language":"zhaojiayu",
#             "movie_date":"zhaojiayu",
#             "movie_long":"zhaojiayu",
#             "movie_description":"zhaojiayu",
             "movie_picurl": u'http://imgwx1.2345.com/dypcimg/img/c/10/sup31983.jpg?1429772047',
             "movie_url": u'http://v.youku.com/v_show/id_XMzUzODk3MTQw.html?tpa=dW5pb25faWQ9MTAwOTAzXzEwMDAwMV8wMV8wMQ'}
    print value['movie_name']
#    obj = Update()
#    obj.ConnDB()
#    obj.UpdataData(value)
#    obj.Disconn()
    object_get = DBOperation()
    object_get.select_data()
    print 'ss'
   # object_get.select_col()
#    object_get.delete_col(value)
#    object_get.dis_conn()

#    obj1 = Delete()
#    obj1.DeleteCol(value)
#    obj1.Disconn()

