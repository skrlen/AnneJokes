import io
import sys
from selenium import webdriver
import time
import random
import logging
log = logging.getLogger('budejie')
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')


def next_page(bowser):
    srce = bowser.find_elements_by_class_name("lazy")
    print(srce, type(srce), len(srce))
    try:
        save_message(srce)
        log.info('当前页正常结束')
        bowser.close()
        return True
    except Exception as e:
        print(e)
        log.error("错误异常，来源于存储错误，原因是%s" % e)
        bowser.close()
        return False


def save_message(srce):
    with open('./budejie.csv', 'a', encoding='utf-8')as f:
        f.write('标题|链接\r')
        for i in srce:

            title = i.get_attribute("title")
            url = i.get_attribute("data-original")
            if title:
                print(title)
                print(url)
                f.write("%s|%s\r" % (title, url))
            else:
                continue


def get_url(final, page_index=1):
    if final+page_index == 1:
        return 'http://www.budejie.com/'
    url = 'http://www.budejie.com/%s' % (final+page_index,)
    log.info("目前的页码是%s" % (final+page_index,))
    return url


def run(url):
    try:
        bowser = webdriver.Chrome()
        bowser.get(url)
        time.sleep(random.randrange(0, 2))
        next_page(bowser)
        return True
    except Exception as e:
        log.error('未知错误，原因%s' % e)
        return False


if __name__ == "__main__":
    a = 0
    while True:
        url = get_url(a)
        run(url)
        a += 1


