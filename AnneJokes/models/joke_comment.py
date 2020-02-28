from django.db import models
from AnneJokes.models.user import User
from AnneJokes.models.user_joke import UserJokes

# 评论表


class JokeComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    joke = models.ForeignKey(UserJokes, on_delete=models.CASCADE)
    comment = models.CharField(max_length=128)
    comment_state = models.BooleanField(default=True)
    comment_self = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s <-- %s' % (self.joke, self.user)
