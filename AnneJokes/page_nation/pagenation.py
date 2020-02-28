from django.core.paginator import Paginator
from AnneJokes.models.user_joke import UserJokes


def pager(index: int, count: int = 10):

    all_joke = UserJokes.objects.order_by('-create_at').filter(joke_states=1)
    p = Paginator(all_joke, count)
    pages = p.page(index)
    p_list = p.page_range
    return pages, p_list, index

