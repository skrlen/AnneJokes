from django.db import models
from AnneJokes.models.user import User

# 用户信息表


class UserInformation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=8)
    gender_choices = (
        (0, "未填写"),
        (1, "男"),
        (2, "女"),
        (3, "不方便透露")
    )
    user_gender = models.IntegerField(choices=gender_choices, default=0)
    user_birthday = models.DateTimeField()
    user_autograph = models.CharField(max_length=64, default='')
    # user_autograph  用户签名   默认为空
    user_country = models.CharField(max_length=12)
    user_address = models.CharField(max_length=12)

    def __str__(self):
        return self.user.nickname
