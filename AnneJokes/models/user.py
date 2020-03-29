from django.db import models
import os
from django.db.models.fields.files import ImageFieldFile
from Anne.settings import MEDIA_ROOT
from AnneJokes.method.image_thumb import make_thumb

# 用户表


class User(models.Model):
    user_head_image = models.ImageField()
    user_thumb_head_image = models.ImageField(null=True)
    nickname = models.CharField(max_length=32, null=False)
    email = models.EmailField(null=False)
    password = models.CharField(null=False, max_length=32)
    user_level = models.IntegerField(default=0)
    user_state = models.BooleanField(default=False)
    is_super_user = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    modify_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s-%s' % (self.nickname, self.id)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        """
        用于自动保存缩略图
        :param force_insert:
        :param force_update:
        :param using:
        :param update_fields:
        :return:
        """
        super(User, self).save()
        img_name = self.user_head_image.name.split('/')[0]
        thumb_pixbuf = make_thumb(os.path.join(MEDIA_ROOT, img_name))
        thumb_path = os.path.join(MEDIA_ROOT, 'mini'+img_name)
        thumb_pixbuf.save(thumb_path)
        self.user_thumb_head_image = ImageFieldFile(self, self.user_thumb_head_image, 'mini'+img_name)
        super(User, self).save()
