from django.http.response import HttpResponse
from django.views import View
from AnneJokes.models.joke_info import JokeInfo
from django.db.models import Q
from AnneJokes.models.joke_comment import JokeComment
from AnneJokes.models.user import User
from AnneJokes.models.user_joke import UserJokes
from AnneJokes.models.comment2comment import Comment2Comment
from AnneJokes.models.message import FoundMessage


class JokeInfoCount(View):

    def get(self, request):
        if 'joke_id' in request.GET:
            joke_id = int(request.GET['joke_id'])
            fabulous = JokeInfo.objects.filter(Q(joke_id=joke_id), Q(joke_type=1))
            setp_on = JokeInfo.objects.filter(Q(joke_id=joke_id) & Q(joke_type=2))

            comment = JokeComment.objects.filter(joke_id=joke_id)

            if "user_id" in request.session._session:
                user = User.objects.filter(pk=int(request.session._session['user_id']))[0]
                fabulous_already = JokeInfo.objects.filter(Q(joke_id=joke_id), Q(joke_type=1), Q(user=user))
                setp_on_already = JokeInfo.objects.filter(Q(joke_id=joke_id) & Q(joke_type=2), Q(user=user))
                fa_state = 0
                sea_state = 0
                if len(fabulous_already) > 0:
                    fa_state = 1
                if len(setp_on_already) > 0:
                    sea_state = 1

                comment = JokeComment.objects.filter(joke_id=joke_id)
                com2com = Comment2Comment.objects.filter(joke_comment_id__in=[i.id for i in comment])
                comment = len(comment) + len(com2com)
                if fa_state == sea_state == 0:
                    return HttpResponse('%s,%s,%s' % (len(fabulous), len(setp_on), comment))
                return HttpResponse('%s,%s,%s,%s,%s' % (len(fabulous), fa_state, len(setp_on), sea_state, comment))

            return HttpResponse('%s,%s,%s' % (len(fabulous), len(setp_on), len(comment)))
        return HttpResponse('不要乱看，超过三次送永久封禁大礼包一个')

    def post(self, request):
        joke = UserJokes.objects.filter(pk=int(request.POST['joke_id']))[0]
        data_type = int(request.POST['data_type'])
        if "user_id" in request.session._session:
            user = User.objects.filter(pk=int(request.session._session['user_id']))[0]
            if joke and user is not None:
                joke_type_save = JokeInfo.objects.create(user=user, joke=joke, joke_type=data_type)
                joke_type_save.save()
                if user.id != joke.id:
                    msg = FoundMessage.objects.create(user=joke.user, from_user=user.id,
                                                      message='%s ---👍点赞了你的发布  %s' % (user.nickname, joke.joke_content))
                    msg.save()
                # print(joke_type_save.choice)
                a = {1: '点赞', 2: '点踩'}
                return HttpResponse('%s成功' % a[JokeInfo.objects.get(id=joke_type_save.id).joke_type])
            elif joke is None:
                return HttpResponse('错误的指令')
            elif user is None:
                return HttpResponse('请先登录，然后才能进行操作')
            else:
                return HttpResponse('errorMessage')
        return HttpResponse('请先登录，然后才能进行操作')

    def delete(self, request):
        body_message = request.body.decode()
        joke_id = body_message.split('&')
        q = [i.split('=') for i in joke_id]
        joke = UserJokes.objects.filter(pk=int(q[0][1]))[0]
        data_type = int(q[1][1])
        user = User.objects.filter(pk=int(request.session._session['user_id']))[0]
        if joke and user is not None:
            joke_type_delete = JokeInfo.objects.filter(user=user, joke=joke, joke_type=data_type)
            if not joke_type_delete:
                return HttpResponse('意外的错误')
            a = {1: '取消点赞', 2: '取消点踩'}
            joke_type_delete[0].delete()
            return HttpResponse('%s成功' % a[data_type])
        elif joke is None:
            return HttpResponse('错误的指令')
        elif user is None:
            return HttpResponse('请先登录，然后才能进行操作')
        else:
            return HttpResponse('errorMessage')


