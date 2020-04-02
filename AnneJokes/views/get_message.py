# -*- coding: utf-8 -*-
from AnneJokes.models.user import User
from AnneJokes.models.message import FoundMessage
from django.views import View
from django.shortcuts import render
from django.http import QueryDict
from django.http.response import HttpResponse


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
                if msg.get('message_id'):
                    msg = FoundMessage.objects.filter(id=int(msg.get('message_id')))
                    msg[0].delete()
                    return HttpResponse('成功')
                if msg.get('all_msg'):
                    msg_all = FoundMessage.objects.filter(user=user[0])
                    msg_all.delete()
                    return HttpResponse('全部删除')
                return HttpResponse('失败')

            return render(request, 'base.html', {'title': 'err-msg', 'message': '错误的用户请求'})
        return render(request, 'base.html', {'title': 'err-msg', 'message': '权限不足'})
