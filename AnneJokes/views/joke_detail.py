# -*-coding:utf-8 -*-
from django.views import View
from AnneJokes.models.user_joke import UserJokes
from AnneJokes.models.user import User
from django.shortcuts import render, redirect


class JokeDetail(View):
    def get(self, request):
        if 'joke_id' in request.GET:
            joke_id = request.GET['joke_id']
            joke = UserJokes.objects.filter(id=int(joke_id))
            if joke:
                data = dict()
                data['joke'] = joke[0]
                data['comment'] = joke[0].jokecomment_set.all()
                if "user_id" in request.session._session:
                    user_id = request.session._session['user_id']
                    user = User.objects.filter(pk=user_id)
                    if user:
                        data['username'] = user[0].nickname
                        data['head_image'] = user[0].user_head_image.name
                        if user[0].user_thumb_head_image.name:
                            data['thumb_img'] = user[0].user_thumb_head_image.name
                        else:
                            data['thumb_img'] = user[0].user_head_image.name
                        return render(request, 'joke_detail.html', data)
                    return render(request, 'base.html', {'title': 'err-msg', "message": '错误的用户id'})
                return render(request, 'joke_detail.html', data)
            return render(request, 'base.html', {'title': 'err-msg', "message": '错误的joke_id'})
        return redirect('/index/')

