from django.http.response import HttpResponse
from django.views import View
from AnneJokes.models.user import User
from AnneJokes.models.joke_comment import JokeComment
from django.db.models import Q
from AnneJokes.models.user_joke import UserJokes


class Comments(View):

    def get(self, request):

        # 评论
        print(request)
        pk = request.GET['joke_id']
        comments = JokeComment.objects.filter(Q(joke_id=pk) & Q(comment_state=True))
        print(comments, type(comments))
        comm = dict()
        # 评论评论的评论
        # comment_comments = JokeComment
        comm['comment'] = comments
        return HttpResponse(comm)

    def post(self, request):
        return HttpResponse('00000')


