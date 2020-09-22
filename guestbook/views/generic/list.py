from django.http import Http404
from django.views.generic import View
from django.utils.translation import ugettext as _

from guestbook.views.generic import JSONResponse


class ListView(View):
    model = None
    handler = None

    def get_queryset(self):
        return self.model.query()

    def get(self, request, *args, **kwargs):
        object_list = self.get_queryset().fetch()

        is_empty = len(object_list) == 0
        if is_empty:
            raise Http404(_("{model} has no data".format(model=self.model)))

        ret = []
        for obj in object_list:
            ret.append(self.handler(obj).serializer)

        return JSONResponse(ret)

