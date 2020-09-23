import json

from django.http import HttpResponse
from django.views.generic import View


def JSONResponse(data):
    return HttpResponse(json.dumps(data), content_type="application/json")


class GenericViewset(View):
    def dispatch(self, request, *args, **kwargs):
        id_key_exists = 'id' in kwargs

        if request.method.lower() in self.http_method_names:
            if request.method.lower() == 'get' and id_key_exists:
                handler = getattr(self, 'retrieve', self.http_method_not_allowed)
            elif request.method.lower() == 'get':
                handler = getattr(self, 'list', self.http_method_not_allowed)
            else:
                handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
        else:
            handler = self.http_method_not_allowed
        return handler(request, *args, **kwargs)
