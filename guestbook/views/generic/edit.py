from guestbook.views.generic import JSONResponse


class UpdateViewMixin(object):
    form = None
    handler = None

    def put(self, request, *args, **kwargs):
        form = self.form(request.PUT)
        if not form.is_valid():
            return JSONResponse(['Data is not valid'])

        obj_dict = form.to_dict()
        id_key = kwargs.pop('id', None)
        handler = self.handler(_id=id_key)
        handler.update(obj_dict)
        return JSONResponse(handler.serializer)


class CreateViewMixin(object):
    form = None
    handler = None

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if not form.is_valid():
            return JSONResponse(dict(form.errors))

        obj_dict = form.to_dict()
        handler = self.handler()
        handler.create(obj_dict)
        return JSONResponse(handler.serializer)


class DeleteViewMixin(object):
    handler = None

    def delete(self, request, *args, **kwargs):
        id_key = kwargs.pop('id', None)
        handler = self.handler(_id=int(id_key))
        handler.delete()
        return JSONResponse('Entity with id {} has been deleted'.format(id_key))
