import scrapy
from ip_crawler.items import MaoyanItem
from scrapy.selector import Selector


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    def start_requests(self):
        url = 'https://maoyan.com/films?showType=3'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        movies = Selector(response=response).xpath('//div[@class="movie-hover-info"]')[:10]
        for movie in movies:
            item = MaoyanItem()
            m_title = movie.xpath('./div[1]/span[1]/text()')
            m_type = movie.xpath('./div[2]/text()')[-1]
            m_time = movie.xpath('./div[4]/text()')[-1]
            print(m_title.extract_first().strip())
            print(m_type.extract().strip())
            print(m_time.extract().strip())
            item['m_title'] = m_title.extract_first().strip()
            item['m_type'] = m_type.extract().strip()
            item['m_time'] = m_time.extract().strip()
            yield item
