# -*- coding:utf-8 -*-
#__author__ = 'Administrator'

#import scrapy.http
import urllib2
import urllib

'''
def post_test():
    url = 'http://www.kankongjian.com/index.php?s=vod-search'
#    url = 'http://www.kankongjian.com/vod-search.html'
    postdata = {}
#    postdata["data"] = json.dumps(item, ensure_ascii=False)
    postdata["wd"] = "Flip Flappers"
    encodedata = urllib.urlencode(postdata)
    req = urllib2.Request(url, encodedata)
    print '*********************'
#    req = urllib2.Request(url, encodedata)
    page = urllib2.urlopen(req)
    ret_str = page.read()
    print ret_str'''


class TestGet():
    def get_test(self,name):
        request_url = 'http://tv.2345.com/moviecore/server/search/?q=' + urllib.quote(
            name)+'&ctl=think&jqueryCallback=jQuery183043205193813774856_1478601994451&_=1478603005995'
        text = self._get(request_url)
        print type(text)


if __name__ == '__main__':
    obj = TestGet()
    obj.get_test('肖申克的救赎')
#    post_test()