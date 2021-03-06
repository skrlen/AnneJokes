from django.conf.urls import url
# from AnneJokes.views.testIndex import Test
from AnneJokes.views.index import Index
from AnneJokes.views.login import UserLogin
from AnneJokes.views.loadImage import LoadImage
from AnneJokes.views.joke_comment import Comments
from AnneJokes.views.joke_info_count import JokeInfoCount
from AnneJokes.views.register import Register
from AnneJokes.views.user_activation import UserActive
from AnneJokes.views.retrieve_password import RetrievePassword
from AnneJokes.views.upload_joke import UploadJokes
from AnneJokes.views.userinfo import ShowUserInfo
from AnneJokes.views.my_joke import MyJoke
from AnneJokes.views.get_message import GetMessage
from AnneJokes.views.joke_detail import JokeDetail


urlpatterns = [
    url(r'^$', Index.as_view()),
    url(r'^index/$', Index.as_view()),
    url(r'^login/$', UserLogin.as_view()),
    url(r'^loadimg/$', LoadImage.as_view()),
    url(r'^comment/$', Comments.as_view()),
    url(r'^jokeic/$', JokeInfoCount.as_view()),
    url(r'^register/$', Register.as_view()),
    url(r'^activate/$', UserActive.as_view()),
    url(r'^retrieve/$', RetrievePassword.as_view()),
    url(r'^upload/$', UploadJokes.as_view()),
    url(r'^info/$', ShowUserInfo.as_view()),
    url(r'^myjoke/$', MyJoke.as_view()),
    url(r'^message/$', GetMessage.as_view()),
    url(r'^detail/$', JokeDetail.as_view()),
]
