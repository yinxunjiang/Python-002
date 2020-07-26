from week01.work1.get_movie_url import get_movie_url
import requests
import lxml.etree
from bs4 import BeautifulSoup as bs
import pandas as pd
def get_movie_info():
    #存放电影信息
    movies_info=[]
    urls=get_movie_url()
    # 设置头部信息，猫眼网站设置了cookie校验，需要添加cookie方可访问，先登录猫眼，然后从登录请求的信息中获取cookie
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    cookie = "__mta=20305287.1595735654322.1595735969048.1595736037802.6; uuid=cf95963e8ce14f2daee3.1595735653.1.0.0; mtcdn=K; userTicket=OTbohovwolOtZBWicWczYxfaVSSOITiIyAcdPrsP; n=lbx666865329; lsu=; SERV=maoyan; LREF=aHR0cHM6Ly9tYW95YW4uY29tL3Bhc3Nwb3J0L2xvZ2luP3JlZGlyZWN0PSUyRmZpbG1zJTNGc2hvd1R5cGUlM0Qz; passport.sid=4raZf1vgENyx6pVclrSA0dVXOK7e8_mK; passport.sid.sig=PJPHj2DOXHYGo9US-EVvRyxbOjw"
    header = {}
    header['user-agent'] = user_agent
    header['cookie'] = cookie
    # 请求网站，获取信息
    for url in urls:
        response = requests.get(url, headers=header)
        bs_info = bs(response.text, 'html.parser')
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
        infolist=[movie_name,movie_type,plan_date]
        movies_info.append(infolist)
    return movies_info
    #movie1 = pd.DataFrame(data=movies_info)


movies = pd.DataFrame(data = get_movie_info())
movies.to_csv('./movie1.csv', encoding='utf8', index=False, header=False)
