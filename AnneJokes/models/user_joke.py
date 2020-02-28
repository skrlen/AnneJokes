from django.db import models
from AnneJokes.models.user import User

# 用户发布笑话表


class UserJokes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    states = (
        (0, "未审核"),
        (1, "状态正常"),
        (2, "自行删除"),
        (3, "未通过审核"),
        (4, "举报次数过多"),
        (5, "包含敏感词汇")
    )
    joke_states = models.IntegerField(choices=states, default=0)
    joke_content = models.TextField()
    joke_image = models.ImageField(null=True, default=None)
    joke_video = models.FileField(null=True, default=None)
    create_at = models.DateTimeField(auto_now_add=True)
    modify_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.nickname
