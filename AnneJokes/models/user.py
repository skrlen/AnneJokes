from django.db import models

# 用户表


class User(models.Model):
    user_head_image = models.ImageField()
    nickname = models.CharField(max_length=32, null=False)
    email = models.EmailField(null=False)
    password = models.CharField(null=False, max_length=32)
    user_level = models.IntegerField(default=0)
    user_state = models.BooleanField(default=False)
    is_super_user = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    modify_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nickname
