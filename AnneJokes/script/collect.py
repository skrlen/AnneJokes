# -*-coding:utf-8 -*-
"""
用于自动收集静态文件，防止用户上传的图片没有及时刷新
"""
# import time
import os


def collect():

    os.popen('cd && cd AnneJokes && python3 manage.py collectstatic --noinput')
