from django.shortcuts import render, redirect
from django.views import View
from AnneJokes.models.user_joke import UserJokes
from AnneJokes.models.user import User
from django.http.response import HttpResponse


class UserLogin(View):
    def get(self, request):
        return HttpResponse('{"state": 4, "message": "请求错误"}')

    def post(self, request):
        if 'verify' in request.session._session:
            verify = request.session._session['verify']
            user_verify = request.POST['verify']
            if verify.lower() == user_verify:
                user = User.objects.filter(email=request.POST['email'], password=request.POST['password'])
                if user:
                    request.session['user_id'] = user[0].id
                    users = dict()
                    users['username'] = user[0].nickname
                    users['user_level'] = user[0].user_level
                    head_image = user[0].user_head_image.name
                    users['head_image'] = head_image
                    # return redirect('/index/', users)
                    return HttpResponse(' ', 2)
                return HttpResponse('登陆失败,账号或者密码错误', 4)
            return HttpResponse('验证码错误，请重新输入', 4)
        else:
            return HttpResponse('验证码错误，请重新输入', 4)

    def delete(self, request):
        request.session.clear()
        return render(request, 'index.html')




