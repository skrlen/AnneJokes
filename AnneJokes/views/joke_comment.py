# -*-coding:utf-8 -*-
"""
评论模块
"""
from django.http.response import HttpResponse
from django.views import View
from AnneJokes.models.user import User
from AnneJokes.models.joke_comment import JokeComment
from django.db.models import Q
from AnneJokes.models.user_joke import UserJokes
import json
import time


class Comments(View):

    def get(self, request):

        # 获取所有评论
        pk = request.GET['joke_id']
        comments = JokeComment.objects.filter(Q(joke_id=pk) & Q(comment_state=True))
        comm = dict()
        # 评论评论的评论
        # comment_comments = JokeComment
        for i in comments:
            comm[i.id] = [i.user.nickname, i.comment, i.user.user_head_image.url]
        js = json.dumps(comm)
        print(comm)
        return HttpResponse(js)

    def post(self, request):
        # 添加新的评论
        if "user_id" in request.session._session:
            if 'joke_id' in request.POST:
                joke_id = request.POST['joke_id']
                user_id = request.session._session['user_id']
                joke_comment_content = request.POST['comment']
                if joke_comment_content:
                    joke = UserJokes.objects.filter(pk=int(joke_id))
                    user = User.objects.filter(pk=int(user_id))
                    if joke and user:
                        joke_comment_obj = JokeComment.objects.create(user=user[0], joke=joke[0], comment=joke_comment_content)
                        joke_comment_obj.save()
                        self_comment = JokeComment.objects.filter(user=user[0]).order_by('-create_at')[0]
                        print(self_comment.user.nickname, self_comment.joke.joke_content)
                        data = dict()
                        data[self_comment.id] = [self_comment.user.nickname, joke_comment_content, self_comment.user.user_head_image.url]
                        json1 = json.dumps(data)

                        return HttpResponse(json1)
                return HttpResponse('{}')
            return HttpResponse("缺少参数")

        return HttpResponse("未授权")


    def delete(self, request):
        # 删除自己的评论
        pass


