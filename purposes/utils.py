from django.core.paginator import Paginator
from django.conf import settings


def paginator(request, post_list):
    pag = Paginator(post_list, settings.INTERVAL_END_NUM)
    page_number = request.GET.get('page')
    return pag.get_page(page_number)
