# -*-coding:utf-8 -*-
from AnneJokes.models.user import User
from AnneJokes.method.email import send_html_mail
from django.views import View
from django.http.response import HttpResponse


class RetrievePassword(View):
    def get(self, request):
        return HttpResponse("正在施工，请耐心等待")

    def post(self, request):
        return HttpResponse("正在马不停蹄的做，请耐心等待")
