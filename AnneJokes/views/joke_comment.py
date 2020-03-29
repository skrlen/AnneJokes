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
from AnneJokes.models.comment2comment import Comment2Comment


class Comments(View):

    def get(self, request):

        # 获取所有评论
        pk = request.GET['joke_id']
        comments = JokeComment.objects.filter(Q(joke_id=pk) & Q(comment_state=True) & Q(comment_self=None))
        comm = dict()
        for i in comments:
            c2c = []
            for w in i.comment2comment_set.all():
                c2c.append([w.user.nickname, w.comment, w.user.user_head_image.url])
            comm[i.id] = [i.user.nickname, i.comment, i.user.user_head_image.url, c2c]
        js = json.dumps(comm)
        return HttpResponse(js)

    def post(self, request):
        # 添加新的评论
        if "user_id" in request.session._session:
            user_id = request.session._session['user_id']
            # TODO 评论评论的评论， 暂时搁浅， 等待后边完善时做
            # if 'comment2_ids' in request.POST:
            #     comment_self_id = request.POST['comment2_ids']
            #     comment = request.POST['comment']
            #     joke_comment = Comment2Comment.objects.filter(id=int(comment_self_id))
            #     joke_comment2 = joke_comment[0].comment2comment_set.all()
            #     for i in joke_comment2:
            #         print(i.comment, i.id, i.comment2com2com.id)
            #
            #     return HttpResponse('0000000000')

            if 'comment_id' in request.POST:
                comment_id = request.POST['comment_id']
                comment = request.POST['comment']
                joke_comment = JokeComment.objects.filter(id=int(comment_id))
                user = User.objects.filter(pk=int(user_id))
                if joke_comment and user:
                    comm = Comment2Comment.objects.create(user=user[0], joke_comment=joke_comment[0], comment=comment)
                    comm.save()
                    data = dict()
                    data[comm.id] = [comm.user.nickname, comm.comment, comm.user.user_thumb_head_image.url if comm.user.user_thumb_head_image else comm.user.user_head_image.url]
                    data = json.dumps(data)
                    return HttpResponse(data)

                return HttpResponse('{}')

            if 'joke_id' in request.POST:
                joke_id = request.POST['joke_id']
                joke_comment_content = request.POST['comment']
                if joke_comment_content:
                    joke = UserJokes.objects.filter(pk=int(joke_id))
                    user = User.objects.filter(pk=int(user_id))
                    if joke and user:
                        joke_comment_obj = JokeComment.objects.create(user=user[0], joke=joke[0], comment=joke_comment_content)
                        joke_comment_obj.save()
                        self_comment = JokeComment.objects.filter(user=user[0]).order_by('-create_at')[0]
                        data = dict()
                        data[self_comment.id] = [self_comment.user.nickname, joke_comment_content, self_comment.user.user_head_image.url]
                        json1 = json.dumps(data)

                        return HttpResponse(json1)
                return HttpResponse('{}')
            return HttpResponse("缺少参数")

        return HttpResponse("未授权")

    def delete(self, request):
        # TODO 删除自己的评论
        pass


