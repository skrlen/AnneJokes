from django.shortcuts import render, redirect
from django.views import View
from AnneJokes.models.user import User
from AnneJokes.page_nation.pagenation import pager


class Index(View):
    def get(self, request):
        index = 1
        if "page_index" in request.GET:
            index = request.GET['page_index']
        if 'user_id' in request.session._session:
            user_id = request.session._session['user_id']
            user = User.objects.filter(pk=user_id)[0]
            date = dict()
            date['username'] = user.nickname
            date['head_image'] = user.user_head_image.name
            date['user_level'] = user.user_level
            page, plist, index = pager(index)
            date['joke_page'] = page
            date['joke_list'] = plist

            return render(request, 'index.html', date)
        else:
            data = dict()
            page, plist, index = pager(index)
            data['joke_page'] = page
            data['joke_list'] = plist
            return render(request, 'index.html', data)


