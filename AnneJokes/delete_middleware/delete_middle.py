# -*-coding:utf-8 -*-
from django.http import QueryDict
try:
    from django.utils.deprecation import MiddlewareMixin
except ImportError:
    MiddlewareMixin = object


class HttpPost2HttpOtherMiddleware(MiddlewareMixin):

    def process_request(self, request):
        """
        可以继续添加head, patch, options
        :param request:
        :return:
        """
        try:
            http_method = request.META['REQUEST_METHOD']
            if http_method.upper() not in ('GET', "POST"):
                setattr(request, http_method.upper(), QueryDict(request.body))
        except Exception as e:
            print(e)
        finally:
            return None
