from django.views.generic import View

from guestbook.views.generic import JSONResponse


class UpdateView(View):
    form = None
    handler = None

    def put(self, request, *args, **kwargs):
        form = self.form(request.PUT)
        if not form.is_valid():
            return JSONResponse(['Data is not valid'])

        obj_dict = form.to_dict()
        _id = obj_dict.pop('id')
        handler = self.handler(_id=_id)
        handler.update(obj_dict)
        return JSONResponse(handler.serializer)


class CreateView(View):
    form = None
    handler = None

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if not form.is_valid():
            return JSONResponse(['Data is not valid'])

        obj_dict = form.to_dict()
        handler = self.handler()
        handler.create(obj_dict)
        return JSONResponse(handler.serializer)
