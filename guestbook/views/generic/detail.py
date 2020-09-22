from django.views.generic import View

from guestbook.views.generic import JSONResponse


class DetailView(View):
    model = None
    handler = None

    def get(self, request, *args, **kwargs):
        id_key = kwargs.pop('id', None)

        obj = self.model.get_by_id(int(id_key))
        if obj is None:
            return JSONResponse(['Entity with id {} is not found'.format(id_key)])
        return JSONResponse(self.handler(obj).serializer)
