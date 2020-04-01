# -*-coding: utf-8 -*-
from AnneJokes.models.user_joke import UserJokes
from AnneJokes.models.user import User
from django.views import View
from django.shortcuts import render


class MyJoke(View):
    def get(self, request):
        if "user_id" in request.session._session:
            user = User.objects.filter(id=request.session._session['user_id'])
            if user:
                joke = UserJokes.objects.filter(user=user[0])
                data = dict()
                data['title'] = '%s的空间' % user[0].nickname
                data['username'] = user[0].nickname
                data['pages'] = joke
                data['head_image'] = user[0].user_head_image.name
                if user[0].user_thumb_head_image.name:
                    data['thumb_img'] = user[0].user_thumb_head_image.name
                else:
                    data['thumb_img'] = user[0].user_head_image.name
                print(data)
                return render(request, 'my_joke.html', data)
            return render(request, 'base.html', {'title': 'Err-user', "message": '姿势不太对，重新登陆再来一遍'})
        if 'HTTP_X_FORWARDER_FOR' in request.META:
            ip = request.META['HTTP_X_FORWARDER_FOR']
        else:
            ip = request.META['REMOTE_ADDR']
        return render(request, 'base.html', {'title': 'Err-user', "message": 'ip: %s 请先登陆才能查看。' % ip})



