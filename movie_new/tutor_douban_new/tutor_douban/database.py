# -*-coding:utf-8-*-

import MySQLdb


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
        self.cur.execute("create table old_movies( movie_name varchar(100), movie_rate varchar(10), \
                              movie_direct varchar(100), movie_writer varchar(100), \
                             movie_roles varchar(100), movie_language varchar(100), \
                             movie_date varchar(20), movie_long varchar(10), movie_description varchar(1500),\
                             movie_url varchar(100),movie_id int(11),movie_picurl varchar(100))")


class DBOperation():
    def __init__(self):
        self.conn = MySQLdb.connect(host="139.196.29.97", db='movie', user='root', passwd='TRzjy123', port=3306, charset='utf8', use_unicode=True)
        self.cur = self.conn.cursor()

    def insert_data(self, value):
        try:
 #           exist_sql = "select COUNT(*) from new_movies WHERE movie_name = '%s'" % value['movie_name']
 #           exist = self.cur.execute(exist_sql)
 #           print exist_sql
 #           if exist:
 #               print 'This movie is exist'
 #           else:
 #               print 'This movie is not exist'
            sql = "insert into \
                                  new_movies(movie_id,movie_name,movie_rate, movie_direct,\
                                  movie_writer,movie_roles,movie_language,movie_date,movie_long,movie_description) \
                                  values(%s,%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            param = (value['movie_id'], value['movie_name'], value['movie_rate'], value['movie_director'],
                     value['movie_writer'], value['movie_roles'], value['movie_language'],
                     value['movie_date'], value['movie_long'],
                     value['movie_description'])
            self.cur.execute(sql, param)

        except MySQLdb.Error, e:
            print "Mysql Error %d : %s" % (e.args[0], e.args[1])

    def select_data(self):
        try:
            sql = "SELECT max(movie_id) FROM new_movies"
            self.cur.execute(sql)
            result = self.cur.fetchall()
            return result
        except MySQLdb.Error, e:
            print "Mysql Error %d : %s" % (e.args[0], e.args[1])

    def dis_conn(self):
            self.conn.commit()
            self.cur.close()
            self.conn.close()


if __name__ == '__main__':
    value = {"movie_id":1,
             "movie_name":  u'\u98de\u5c4b\u73af\u6e38\u8bb0',
             "movie_rate":"yiyu",
             "movie_director":"yiyu",
             "movie_writer":"yiyu",
             "movie_roles":"zhaojiayu",
             "movie_language":"zhaojiayu",
             "movie_date":"zhaojiayu",
             "movie_long":"zhaojiayu",
             "movie_description":"zhaojiayu",}
    print type(value['movie_id'])
    obj = DBOperation()
#    obj.ConnDB()
    obj.insert_data(value)
#    obj.Disconn()
#    object_get = Select()
 #   object_get.SelectData()
#    obj = CreateDB()
#    obj.create_table()
