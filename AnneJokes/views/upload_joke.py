# -*-coding:utf-8 -*-
from AnneJokes.models.user import User
from AnneJokes.models.user_joke import UserJokes
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.views import View


class UploadJokes(View):
    def get(self, request):
        if "user_id" in request.session._session:
            user = User.objects.filter(id=int(request.session._session['user_id']))
            if user:
                users = dict()
                users['username'] = user[0].nickname
                users['user_level'] = user[0].user_level
                head_image = user[0].user_head_image.name
                users['head_image'] = head_image
                return render(request, 'upload_joke.html', users)
            return render(request, 'upload_joke.html')
        return render(request, 'upload_joke.html')

    def post(self, request):
        if "user_id" in request.session._session:
            user = User.objects.filter(id=int(request.session._session['user_id']))
            if user:
                joke = UserJokes.objects.create(user=user[0],
                                                joke_content=request.POST['content'],
                                                joke_image=request.FILES['image'],
                                                joke_states=1
                                                )
                joke.save()
                users = dict()
                users['username'] = user[0].nickname
                users['user_level'] = user[0].user_level
                head_image = user[0].user_head_image.name
                users['head_image'] = head_image
                users['title'] = "投稿成功"
                users['message'] = "上传成功，请静待审核！"
                return render(request, 'base.html', users)
            return render(request, 'base.html', {"title": "投稿失败", 'message': "上传失败，原因：错误的用户！"})
        return render(request, 'base.html', {"title": "Error states", 'message': "请登录！"})

