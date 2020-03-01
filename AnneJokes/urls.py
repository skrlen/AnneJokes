from django.conf.urls import url
# from AnneJokes.views.testIndex import Test
from AnneJokes.views.index import Index
from AnneJokes.views.login import UserLogin
from AnneJokes.views.loadImage import LoadImage
from AnneJokes.views.joke_comment import Comments
from AnneJokes.views.joke_info_count import JokeInfoCount


urlpatterns = [
    url(r'^$', Index.as_view()),
    url(r'^index/$', Index.as_view()),
    url(r'^login/$', UserLogin.as_view()),
    url(r'^loadimg/$', LoadImage.as_view()),
    url(r'^comment/$', Comments.as_view()),
    url(r'^jokeic/$', JokeInfoCount.as_view()),
]
