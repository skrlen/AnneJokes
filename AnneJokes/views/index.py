from django.shortcuts import render, redirect
from django.views import View
from AnneJokes.models.user import User
from AnneJokes.page_nation.pagenation import pager
from AnneJokes.models.message import FoundMessage
from django.db.models.query import Q


class Index(View):
    def get(self, request):
        index = 1
        if "page" in request.GET:
            index = request.GET['page']
        if 'user_id' in request.session._session:
            user_id = request.session._session['user_id']
            user = User.objects.filter(pk=user_id)[0]
            date = dict()
            date['message_num'] = FoundMessage.objects.filter(Q(user=user), Q(is_read=False)).count()
            date['username'] = user.nickname
            date['head_image'] = user.user_head_image.name
            if user.user_thumb_head_image.name:
                date['thumb_img'] = user.user_thumb_head_image.name
            else:
                date['thumb_img'] = user.user_head_image.name
            date['user_level'] = user.user_level
            page, plist, index = pager(index, user=user)
            date['joke_page'] = page
            page1 = [str(p) for p in plist]
            date['joke_list'] = page1
            date['all_page'] = len(page1)
            date['joke_index'] = int(index)

            return render(request, 'index.html', date)
        else:
            data = dict()
            page, plist, index = pager(index)
            data['joke_page'] = page
            page1 = [str(p) for p in plist]
            data['joke_list'] = page1
            data['all_page'] = len(page1)
            data['joke_index'] = index
            return render(request, 'index.html', data)


