# -*- coding: utf-8 -*-
from AnneJokes.models.user import User
from AnneJokes.models.message import FoundMessage
from django.views import View
from django.shortcuts import render
from django.http import QueryDict


class GetMessage(View):
    def get(self, request):
        if "user_id" in request.session._session:
            user = User.objects.filter(pk=request.session._session['user_id'])
            if user:
                message = FoundMessage.objects.filter(user=user[0]).order_by('-create_at')
                data = dict()
                a = message.filter(is_read=False)
                for i in a:
                    i.is_read = True
                    i.save()
                data['username'] = user[0].nickname
                data['title'] = '%s的消息记录' % user[0].nickname
                data['head_image'] = user[0].user_head_image.name
                data['message'] = message
                if user[0].user_thumb_head_image.name:
                    data['thumb_img'] = user[0].user_thumb_head_image.name
                else:
                    data['thumb_img'] = user[0].user_head_image.name
                return render(request, 'message.html', data)

    def post(self, request):
        pass

    def delete(self, request):
        """
        TODO 要在ajax的请求头中添加 "X-CSRFToken": $('input[name="csrfmiddlewaretoken"]').val()
        :param request:
        :return:
        """
        if "user_id" in request.session._session:
            user = User.objects.filter(id=request.session._session['user_id'])
            if user:
                msg = QueryDict(request.body)
                if msg.get('msg_id'):
                    print(msg.get('msg_id'))
                    return '成功'

            return render(request, 'base.html', {'title': 'err-msg', 'message': '错误的用户请求'})
