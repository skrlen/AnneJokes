# -*-coding:utf-8 -*-
from django.shortcuts import redirect, render
from django.views import View
from AnneJokes.models.user import User
from django.http.response import HttpResponse
from AnneJokes.method.hashlib_md5 import str_md5
from AnneJokes.method.email import send_html_mail
from AnneJokes.method.email import send_mails


class Register(View):
    def get(self, request):
        if 'email' in request.GET:
            user_email = request.GET['email']
            print(user_email)
            if User.objects.filter(email=user_email):
                resp = HttpResponse("false")
                resp.set_cookie("email_state", 0)
                return resp
            resp = HttpResponse("true")
            resp.set_cookie("email_state", 1)
            return resp
        elif 'nickname' in request.GET:
            nickname = request.GET['nickname']
            if User.objects.filter(nickname=nickname):
                return HttpResponse("false")
            return HttpResponse("true")

    def post(self, request):
        if "email_state" in request.COOKIES:
            if request.COOKIES['email_state'] == '1':
                email = request.POST['email']
                password = request.POST['first-password']
                nickname = request.POST['nickname']
                headimage = request.FILES['headimage']
                password_md5 = str_md5(password)
                user = User.objects.create(email=email, password=password_md5, nickname=nickname, user_head_image=headimage)
                user.save()
                # activate_str = str_md5(email)
                # title = "AnneJoke<skrlen@126.com>"
                # content = '我们为了确定是您本人在操作，请验证您的身份<a href="http://121.36.249.255/activate/?data=%s&id=%s">点击激活</a>，如果您未订阅，此信息请忽略' % (activate_str, user.id)
                # state = send_html_mail(title=title, content=content, to=['skrlen@126.com', email])
                # if state:
                #     return render(request, 'register_response.html', {"message": "注册失败，原因：%s" % state})
                # return render(request, 'register_response.html', {"message": "注册成功，快去邮箱激活吧"})
                return render(request, 'register_response.html', {"message": "注册成功，快去尽情的玩耍吧"})
            else:
                return render(request, 'register_response.html', {"message": "邮箱已经被使用了,快去换个新的吧"})
        return render(request, 'register_response.html', {"message": "未知错误，请重试"})
