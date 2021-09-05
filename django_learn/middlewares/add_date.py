import datetime

from django.utils.deprecation import MiddlewareMixin
from django.utils.functional import SimpleLazyObject


class Middleware(MiddlewareMixin):
    def process_request(self, request):
        request.additional_time = datetime.datetime.now()
        # request.user = SimpleLazyObject(lambda: get_user(request))
