# -*-coding:utf-8 -*-
from AnneJokes.models.user import User
from django.views import View
from AnneJokes.method.hashlib_md5 import str_md5
from django.shortcuts import redirect, render
from django.http.response import HttpResponse


class UserActive(View):
    def get(self, request):
        if 'data' and 'id' in request.GET:
            email = request.GET['data']
            id = request.GET['id']
            try:
                user = User.objects.get(pk=id)
                user_mail = str_md5(user.email)
                if not user.user_state:
                    if user_mail == email:
                        request.session['user_id'] = user.id
                        user.user_state = True
                        user.save()
                        return render(request, 'register_response.html', {"message": "激活成功，正在跳转\r如果未跳转，点击<a href='http://121.36.249.255/index/'>这里</a>"})
                    return render(request, 'register_response.html', {"message": "错误的信息！"})
                return render(request, 'register_response.html', {"message": "无效链接"})
            except Exception as e:
                return render(request, 'register_response.html', {"message": e})

        return render(request, 'register_response.html', {"message": "您输入的链接不完整，请检查后输入"})
