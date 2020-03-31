# -*-coding:utf-8 -*-
from django.core.paginator import Paginator
from AnneJokes.models.user_joke import UserJokes
from AnneJokes.models.user_joke_read import UserJokeRead
from AnneJokes.models.user import User
from django.db.models.query import Q


def pager(index: int, user: object = None, count: int = 10):
    # .order_by('-create_at')
    """
    判断是否有用户，如果有则只显示未看过的，如果没有则显示所有，按时间倒叙， 如果用户看完了所有的则显示所有的jokes
    :param index: 当前观看第几页
    :param user: 是用户还是游客，如果是用户则返回未看的，如果是游客返回所有
    :param count: 每页多少个， 默认为10
    :return: pages：当前页数据， p_list: 当前页码， index：索引
    """
    if user:
        already = [i.joke_id if i else None for i in UserJokeRead.objects.filter(user=user)]
        all_joke = UserJokes.objects.exclude(pk__in=already).order_by('-create_at').filter(joke_states=1)
        if all_joke:
            p = Paginator(all_joke, count)
            pages = p.page(index)
            p_list = p.page_range
            for i in pages:
                obj = UserJokeRead.objects.create(user=user, joke_id=i.id)
                obj.save()
            return pages, p_list, index
        else:
            all_joke = UserJokes.objects.order_by('-create_at')
            p = Paginator(all_joke, count)
            pages = p.page(index)
            p_list = p.page_range
            return pages, p_list, index

    else:
        all_joke = UserJokes.objects.order_by('-create_at')
        p = Paginator(all_joke, count)
        pages = p.page(index)
        p_list = p.page_range
        return pages, p_list, index


def pager_user_info(index: int, user: object, count: 10):

    user_joke = UserJokes.objects.filter(user=user)
    if user_joke:
        p = Paginator(user_joke.order_by('-create_at'), count)
        page = p.page(index)
        p_list = p.page_range
        return page, p_list, index
