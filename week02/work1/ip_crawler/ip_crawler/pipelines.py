# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import os
import pandas as pd
import pymysql
from ip_crawler.settings import DATABASES

# BASE_DIR = BASE_DIR = os.path.dirname(
#     os.path.dirname(os.path.abspath(__file__)))
# m_path = os.path.join(BASE_DIR, "maoyan.csv")


class IpCrawlerPipeline:
    def process_item(self, item, spider):
        return item


class MaoyanPipeline:
    def process_item(self, item, spider):
        if spider.name != 'maoyan':
            return item
        m_title = item['m_title']
        m_type = item['m_type']
        m_time = item['m_time']
        
       # 建立连接，创建tb2表 
        TABLE_NAME = 'movies'
        try:
            conn = pymysql.connect(**DATABASES)
            con1 = conn.cursor()
            count = con1.execute(f'select * from {TABLE_NAME};')
        except pymysql.err.ProgrammingError as e:
            err_code = eval(str(e))[0]
            if err_code == 1146:
                sql = f'''CREATE TABLE `{TABLE_NAME}` (
                        `m_title` varchar(30) DEFAULT NULL,
                        `m_type` varchar(22) DEFAULT NULL,
                        `m_time` date DEFAULT NULL
                        )DEFAULT CHARSET=utf8mb4'''
                con1.execute(sql)
            else:
                print(e)
        except Exception as e:
            print(e)
        
        try:
            sql = f"INSERT INTO {TABLE_NAME} values('{m_title}', '{m_type}','{m_time}')"
            con1.execute(sql)
            conn.commit()
            count = con1.execute(f'select * from {TABLE_NAME};')
            print(f'查询到 {count} 条记录')
            print(con1.fetchall())
        except Exception as e:
            print(e)
            conn.rollback()
        finally:
            con1.close()
            conn.close()

        return item
