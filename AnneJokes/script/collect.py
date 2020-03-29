# -*-coding:utf-8 -*-
"""
用于自动收集静态文件，防止用户上传的图片没有及时刷新
"""
import time
import os


def collect():
    os.system('cd AnneJokes')
    time.sleep(0.5)
    os.system('python3 manage.py collectstatic')
    time.sleep(1)
    os.system('yes')
