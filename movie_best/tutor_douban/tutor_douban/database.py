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
        self.cur.execute("create table best_movies( movie_name varchar(100), movie_rate varchar(10), \
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

 #           exist_sql = "select COUNT(*) from best_movies WHERE movie_name = '%s'" % value['movie_name']
 #           exist = self.cur.execute(exist_sql)
 #           print exist_sql
 #           if exist:
 #               print 'This movie is exist'
 #           else:
 #               print 'This movie is not exist'
            sql = "insert into \
                                  best_movies(movie_id,movie_name,movie_rate, movie_direct,\
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
            sql = "SELECT max(movie_id) FROM best_movies"
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
    value = {"movie_name": "驴得水",
             "movie_rate":"8.4",
             "movie_director":"周申 / 刘露",
             "movie_writer":"周申 / 刘露",
             "movie_roles":"任素汐 / 大力 / 刘帅良 / 裴魁山 / 阿如那 /",
             "movie_language":"汉语普通话",
             "movie_date":"2016-10-28",
             "movie_long":"111分钟",
             "movie_description":"一群“品行不端”却怀揣教育梦想的大学教师，从大城市来到偏远乡村开办了一所小学校。学校待遇惨淡、生活艰苦，但老师们都自得其乐，每天嘻嘻哈哈打成一片。然而教育部特派员要来突击检查的消息打破了安宁，因为学校有一位“驴得水老师”隐藏着不可告人的秘密。就在所有人都担心丑事即将败露的时候，一个神奇天才的出现拯救了大家，然而谁能料到真正的麻烦才刚刚开始……",
             "movie_id": 40,
             "movie_url": u'http://www.zaizai5.com/jq/88051/player-0-0.html',
             "movie_picurl": u'https://img3.doubanio.com/view/photo/photo/public/p2393044761.jpg'}
#    print type(value['movie_id'])
    obj = DBOperation()
    obj.insert_data(value)
    obj.dis_conn()
#    object_get = Select()
 #   object_get.SelectData()
#    obj = CreateDB()
#    obj.create_database()
#    obj.create_table()
