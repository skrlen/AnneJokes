from django.contrib import admin
from AnneJokes.models.user import User
from AnneJokes.models.user_information import UserInformation
from AnneJokes.models.user_joke import UserJokes
from AnneJokes.models.joke_info import JokeInfo
from AnneJokes.models.joke_comment import JokeComment


# Register your models here.

admin.site.register(User)
admin.site.register(UserInformation)
admin.site.register(UserJokes)
admin.site.register(JokeInfo)
admin.site.register(JokeComment)
