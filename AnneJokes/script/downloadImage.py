import io
import sys
import requests
import time
import random
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')


def download(url, name):

    headers = {
        "User-Agent": "Mozilla/5.0(Windows NT 10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/72.0.3626.81Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip,deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Host": "mpic.spriteapp.cn",
        "If-Modified-Since": "Fri, 01 Nov 2019 11:42:32 GMT",
        "If-None-Match": "5dbc1a28-19efc9",
        "Upgrade-Insecure-Requests": "1",
    }

    head = {
       "Accept": "image/webp,image/apng,image/*,*/*;q=0.8Accept-Encoding:gzip",
       "deflateAccept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Host": "mpic.spriteapp.cn",
        "Pragma": "no-cache",
        'Referer': '%s' % (url.split('\n')[0], ),
        "User-Agent": "Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/72.0.3626.81Safari/537.36",
    }

    image_data = requests.get(url, headers=headers)
    on = requests.get("http://mpic.spriteapp.cn/favicon.ico", headers=head)
    print(on.url)

    save_image(data=image_data, name=name)


def save_image(data, name):
    time.sleep(random.randrange(1, 3))
    try:
        a = './loadImage/%s' % name
        with open(a, 'wb+')as f:
            f.write(data.content)
        # print(a)
        with open('./image_name.txt', 'a')as d:
            d.write('%s\r' % name)

    except Exception as e:
        print(e)


def spilt(data, index):
    if index != 1:
        image_url = data.split('|')[1]
        image_name = image_url.split('/')[-1].split('\n')[0]
        print(image_name)
        download(image_url, image_name)
    return True


def run():
    print('start')
    with open('./budejie.csv', 'r', encoding='utf-8')as f:
        i = 1
        while True:
            spilt(f.readline(), i)
            print(i)
            i += 1
        # spilt(f.readline())


if __name__ == "__main__":
    print('1')
    run()
