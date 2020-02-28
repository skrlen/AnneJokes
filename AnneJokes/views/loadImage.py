from django.shortcuts import render, redirect
from django.views import View
from django.http.response import HttpResponse
from AnneJokes.mapping import verify

# 验证码请求


class LoadImage(View):

    def get(self, request):
        return HttpResponse('{"state":"4", "message":"错误的请求"}')

    def post(self, request):
        name, image = verify()
        str2 = 'data:image/png;base64,%s' % image
        q = [name, str2]
        request.session['verify'] = name
        return HttpResponse(str(q))
