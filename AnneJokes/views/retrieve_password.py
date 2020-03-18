# -*-coding:utf-8 -*-
from AnneJokes.models.user import User
from AnneJokes.method.email import send_html_mail
from django.views import View
from django.shortcuts import render


class RetrievePassword(View):
    def get(self, request):
        return render(request, 'base.html', {"title": "尊敬的用户你好", "message": "该页面正在施工，请耐心等待"})

    def post(self, request):

        return render(request, 'base.html', {"title": "尊敬的用户你好", "message": "该页面正在施工，请耐心等待"})
