# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
#from week01.work2.maoyan.maoyan.items import MaoyanItem
from maoyan.items import MaoyanItem
#from ..items import MaoyanItem
from scrapy.selector import Selector
import lxml.etree
class DoubanSpider(scrapy.Spider):
    name = 'maoyan_movie'
    allowed_domains = ['maoyan.com']
    start_urls = ['http://maoyan.com/']
    # 起始URL列表
    start_urls = ['https://maoyan.com/films?showType=3']

#   注释默认的parse函数
#   def parse(self, response):
#        pass


    # 解析函数
    def parse(self, response):
        soup = BeautifulSoup(response.text, 'html.parser')
        #定义一个空列表，用于存放电影的详情链接
        movie_urls=[]
        #获取前10个电影的详情链接，为后面在详情页获取电影类型、上映时间等信息做准备
        for tag in soup.find_all('div',attrs={'class': 'channel-detail movie-item-title'},limit=10):
            url=tag.find('a').get('href')
            #由于获取到的链接信息都是类似：films/1297466这样的，没有补全前缀，这里我们自行补全
            movie_urls.append("https://maoyan.com"+url)
            # 在items.py定义
        item = MaoyanItem()
        for url in movie_urls:
            yield scrapy.Request(url=url, meta={'item': item}, callback=self.parse2)


    # 解析具体页面
    def parse2(self, response):
        item = response.meta['item']
        soup = BeautifulSoup(response.text, 'html.parser')
        # xml化处理
        selector = lxml.etree.HTML(response.text)
        # 电影名称
        movie_name = selector.xpath('//h1/text()')
        print(f'电影名称: {movie_name}')
        # 类型
        movie_type = selector.xpath('//li[@class="ellipsis"][1]/a/text()')
        print(f'电影类型: {movie_type}')
        # 上映时间
        plan_date = selector.xpath('//li[@class="ellipsis"][3]/text()')
        print(f'上映时间：{plan_date}')
        item["title"]=movie_name
        item["film_type"]=movie_type
        item["date"]=plan_date
        yield item



