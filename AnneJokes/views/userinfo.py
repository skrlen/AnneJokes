# -*-coding:utf-8 -*-
from AnneJokes.models.user import User
from AnneJokes.models.user_information import UserInformation
from django.http.response import HttpResponse
from django.views import View
from django.shortcuts import render, redirect
import random


class ShowUserInfo(View):

    def get(self, request):
        if 'user_id' in request.GET:
            user = User.objects.filter(pk=int(request.GET['user_id']))
            if user:
                data = dict()
                data['title'] = user[0].nickname
                info = UserInformation.objects.filter(user=user[0])
                data['user_name'] = info[0].user_name if info else ''
                data['user_gender'] = info[0].get_user_gender_display() if info else ''
                data['user_birthday'] = info[0].user_birthday if info else ''
                data['user_address'] = info[0].user_address if info else ''
                data['user_autograph'] = info[0].user_autograph if info else ''
                data['user_country'] = info[0].user_country if info else ''
                # print(info[0].get_user_gender_display())
                data['username'] = user[0].nickname
                data['head_image'] = user[0].user_head_image.url
                # data['background_image'] = '/media/background'+str(random.randrange(1, 5))+'.jpg'
                data['color'] = random.choices(['#e4b9b9', '#269abc', '#737373', '#eeeeee'])
                if user[0].user_thumb_head_image.name:
                    data['thumb_img'] = user[0].user_thumb_head_image.name
                else:
                    data['thumb_img'] = user[0].user_head_image.name
                return render(request, 'userInfo.html', data)
            return render(request, 'base.html', {'message': '错误的用户', 'title': 'Errors, No Users'})
        if 'user_id' in request.session._session:
            user = User.objects.filter(pk=request.session._session['user_id'])
            if user:
                data = dict()
                data['title'] = user[0].nickname
                info = UserInformation.objects.filter(user=user[0])
                data['user_name'] = info[0].user_name if info else ''
                data['user_gender'] = info[0].get_user_gender_display() if info else ''
                data['user_birthday'] = info[0].user_birthday if info else ''
                data['user_address'] = info[0].user_address if info else ''
                data['user_autograph'] = info[0].user_autograph if info else ''
                data['user_country'] = info[0].user_country if info else ''
                print(info[0].get_user_gender_display())
                data['username'] = user[0].nickname
                data['head_image'] = user[0].user_head_image.url
                # data['background_image'] = '/media/background'+str(random.randrange(1, 5))+'.jpg'
                data['color'] = random.choices(['#e4b9b9', '#269abc', '#737373', '#eeeeee'])
                if user[0].user_thumb_head_image.name:
                    data['thumb_img'] = user[0].user_thumb_head_image.name
                else:
                    data['thumb_img'] = user[0].user_head_image.name
                return render(request, 'userInfo.html', data)
            return render(request, 'userInfo.html')
        return redirect('/index/')

    def post(self, request):
        pass
