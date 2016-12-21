# -*- coding = utf-8 -*-
#__author__ = 'Administrator'
import urllib
import os


def image_save():
    src = 'https://img3.doubanio.com/view/movie_poster_cover/lpst/public/p480747492.jpg'
    file_name = 'yy.jpg'
    file_path = os.path.join("E:\\tutor_douban\pics", file_name)
    urllib.urlretrieve(src, file_path)

if __name__ == '__main__':
    image_save()