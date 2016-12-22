# Scrapy for tutor_douban project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'tutor_douban'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['tutor_douban.spiders']
NEWSPIDER_MODULE = 'tutor_douban.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

# start MySQL database configure settings
# end of MySQL database configure settings

ITEM_PIPELINES = {'tutor_douban.pipelines.TutorDoubanPipeline'}

