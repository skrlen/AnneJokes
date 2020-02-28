from django.db import models
from AnneJokes.models.user import User
from AnneJokes.models.user_joke import UserJokes

# 点赞表


class JokeInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    joke = models.ForeignKey(UserJokes, on_delete=models.CASCADE)
    choice = (
        (1, "点赞"),
        (2, "点踩"),
    )
    joke_type = models.IntegerField(choices=choice)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.joke
