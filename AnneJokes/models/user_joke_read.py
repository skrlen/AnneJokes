# -*-coding:utf-8 -*-
"""
用来存储用户看过的joke的id,用以保证看不到重复的joke
"""
from django.db import models
from AnneJokes.models.user import User


class UserJokeRead(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # user_joke的id，必须存在
    joke_id = models.IntegerField()
    create_at = models.DateTimeField(auto_now_add=True)
