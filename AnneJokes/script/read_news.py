# -*-coding:utf-8 -*-
import requests
import json


def web_page():
    url = 'http://news.cctv.com/2019/07/gaiban/cmsdatainterface/page/news_1.jsonp?cb=t&cb=news'
    headers = {
        'referer': 'http://news.cctv.com/',
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36",
        'Cookie': 'cna=3oQZFmNgJGkCASrn473kb1rC; sca=430911ab; _CCTV_CURRENT_CITY=101180101; country_code=CN',
        'Host': 'news.cctv.com'
    }
    page = requests.get(url, headers=headers)
    dic = page.content.decode('utf-8')[5:-1]
    a = json.loads(dic)
    return a['data']['list']
    # for i in a['data']['list']:
    #     print(i['image2'], i['title'], i['focus_date'], i['brief'], i['url'])

