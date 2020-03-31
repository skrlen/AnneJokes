# -*-coding:utf-8 -*-
from AnneJokes.models.user import User
from AnneJokes.models.user_joke import UserJokes
from AnneJokes.models.user_information import UserInformation
from AnneJokes.page_nation.pagenation import pager_user_info
from django.views import View
from django.shortcuts import render, redirect
import random
import datetime


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
                data['user_username'] = user[0].nickname
                data['user_head_image'] = user[0].user_head_image.url

                # page, p_list, index = pager_user_info(int(request.GET['page']), user[0], count=10)
                # data['user_page'] = page
                # data['user_p_list'] = p_list
                # data['index'] = index
                data['pages'] = UserJokes.objects.filter(user=user[0])
                # print(info[0].get_user_gender_display())
                if 'user_id' in request.session._session:
                    # 判断当前用户是否登陆
                    user = User.objects.filter(pk=request.session._session['user_id'])
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
                # print(info[0].get_user_gender_display())
                data['user_id'] = user[0].id
                data['username'] = user[0].nickname
                data['head_image'] = user[0].user_head_image.url
                data['user_username'] = user[0].nickname
                data['user_head_image'] = user[0].user_head_image.url
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
        if "user_id" in request.session._session:
            user = User.objects.filter(id=request.session._session['user_id'])
            if user:
                try:
                    user_name = request.POST['user_name']
                    autograph = request.POST['autograph']
                    year = request.POST['birthday_year']
                    month = request.POST['birthday_month']
                    day = request.POST['birthday_day']
                    gender = request.POST['gender']
                    print(user_name, autograph, '%s-%s-%s' % (year, month, day), gender)
                    user_info = UserInformation.objects.filter(user=user[0])[0]
                    user_info.user_name = user_name
                    user_info.user_autograph = autograph
                    user_info.user_gender = int(gender)
                    user_info.user_birthday = datetime.date(int(year), int(month), int(day))
                    user_info.save()
                    return redirect('/info/')
                except Exception as e:
                    return render(request, 'base.html', {"title": "err", "message": e})
            return render(request, 'base.html', {'title': 'Err-msg', "message": '不太正确的用户，请检查后输入'})
        return render(request, 'base.html', {'title': 'Err-user', "message": '未授权'})
