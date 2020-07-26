import requests
import lxml.etree
from bs4 import BeautifulSoup as bs
# 爬取页面详细信息
def get_movie_url():
    # 电影首页
    url = 'https://maoyan.com/films?showType=3'
    #设置头部信息，猫眼网站设置了cookie校验，需要添加cookie方可访问，先登录猫眼，然后从登录请求的信息中获取cookie
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    cookie="__mta=20305287.1595735654322.1595735969048.1595736037802.6; uuid=cf95963e8ce14f2daee3.1595735653.1.0.0; mtcdn=K; userTicket=OTbohovwolOtZBWicWczYxfaVSSOITiIyAcdPrsP; n=lbx666865329; lsu=; SERV=maoyan; LREF=aHR0cHM6Ly9tYW95YW4uY29tL3Bhc3Nwb3J0L2xvZ2luP3JlZGlyZWN0PSUyRmZpbG1zJTNGc2hvd1R5cGUlM0Qz; passport.sid=4raZf1vgENyx6pVclrSA0dVXOK7e8_mK; passport.sid.sig=PJPHj2DOXHYGo9US-EVvRyxbOjw"
    header = {}
    header['user-agent'] = user_agent
    header['cookie']=cookie
    #请求网站，获取返回信息
    response = requests.get(url, headers=header)
    bs_info = bs(response.text, 'html.parser')
    #定义一个空列表，用于存放电影的详情链接
    movie_urls=[]
    #获取前10个电影的详情链接，为后面在详情页获取电影类型、上映时间等信息做准备
    for tag in bs_info.find_all('div',attrs={'class': 'channel-detail movie-item-title'},limit=10):
        url=tag.find('a').get('href')
        #由于获取到的链接信息都是类似：films/1297466这样的，没有补全前缀，这里我们自行补全
        movie_urls.append("https://maoyan.com"+url)
    return movie_urls

