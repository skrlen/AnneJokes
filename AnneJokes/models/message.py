from django.db import models
from AnneJokes.models.user import User
from AnneJokes.models.user_joke import UserJokes


class FoundMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    from_user = models.IntegerField(null=False)
    message = models.CharField(max_length=64)
    joke = models.ForeignKey(UserJokes, on_delete=models.CASCADE, null=True)
    is_read = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    modify_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.user.nickname
