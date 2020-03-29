from django.db import models
from AnneJokes.models.user import User
from AnneJokes.models.joke_comment import JokeComment


class Comment2Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    joke_comment = models.ForeignKey(JokeComment, on_delete=models.CASCADE)
    comment = models.CharField(max_length=125)
    comment2com2com = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
