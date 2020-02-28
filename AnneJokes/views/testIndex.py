from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.views import View


class Test(View):

    def get(self, request):
        return HttpResponse("你请求的状态是%s" % request.method)

    def post(self, request):
        return HttpResponse("你请求的状态是%s" % request.method)




