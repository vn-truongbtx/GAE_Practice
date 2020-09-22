from django.http import HttpResponseBadRequest


class PutParsingMiddleware(object):
    def process_request(self, request):
        if request.method == "PUT":
            if hasattr(request, '_post'):
                del request._post
                del request._files
            try:
                request.method = "POST"
                request._load_post_and_files()
                request.method = "PUT"
            except AttributeError as e:
                request.META['REQUEST_METHOD'] = 'POST'
                request._load_post_and_files()
                request.META['REQUEST_METHOD'] = 'PUT'

            request.PUT = request.POST


class JSONParsingMiddleware(object):
    def process_request(self, request):
        if request.method == "PUT" or request.method == "POST":
            try:
                request.DATA = dict(request.REQUEST)
            except ValueError as ve:
                return HttpResponseBadRequest("Error : {0}".format(ve))
