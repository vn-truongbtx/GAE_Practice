from guestbook.views.generic import JSONResponse


class ListViewMixin(object):
    model = None
    handler = None

    def get_queryset(self):
        return self.model.query()

    def list(self, request, *args, **kwargs):
        object_list = self.get_queryset().fetch()

        is_empty = len(object_list) == 0
        if is_empty:
            return JSONResponse(["{model} has no data".format(model=self.model.__name__)])

        ret = []
        for obj in object_list:
            ret.append(self.handler(obj).serializer)

        return JSONResponse(ret)
