import time

from polls.models import Log


class LogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        o = Log()
        o.path = request.path
        if not o.path.startswith('/admin/'):
            o.method = request.method
            o.timestamp = int(time.time())
            o.save()
        return response
