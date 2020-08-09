# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class IpCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class MaoyanItem(scrapy.Item):
    m_title = scrapy.Field()
    m_type = scrapy.Field()
    m_time = scrapy.Field() 