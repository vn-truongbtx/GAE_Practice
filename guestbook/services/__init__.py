from google.appengine.ext.ndb import Property


class Handler(object):
    model = None

    def __init__(self, obj=None, _id=None):
        if _id is not None and isinstance(_id, int):
            self.obj = self.model.get_by_id(_id)
        else:
            self.obj = obj
        self.fields = self.get_fields()

    def get_fields(self):
        fields = []
        for attr in dir(self.model):
            if isinstance(attr, Property):
                fields.append(attr)
        return fields

    @property
    def serializer(self):
        ret = {}

        for field in self.fields:
            method = getattr(self, 'get_{}'.format(field), None)
            if method is None:
                value = getattr(self.obj, field, None)
            else:
                value = method()

            ret[field] = value

        return ret

    def update(self, *args, **kwargs):
        pass

    def create(self, *args, **kwargs):
        pass
