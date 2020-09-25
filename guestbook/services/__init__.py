from django.core.exceptions import ValidationError
from google.appengine.ext.ndb import Property


#  Using to_dict, entity.to_dict()
class Handler(object):
    model = None

    def __init__(self, obj=None, _id=None):
        try:
            if _id is not None:
                _id = int(_id)
        except ValueError as e:
            raise ValidationError('ID is not a integer')

        if _id is not None and isinstance(_id, int):
            self.obj = self.model.get_by_id(_id)
        else:
            self.obj = obj
        self.fields = self.get_fields()

    def get_fields(self):
        fields = []
        for attr in dir(self.model):
            if attr in ['created', 'updated', '_key']:
                continue
            if isinstance(getattr(self.model, attr, None), Property):
                fields.append(attr)
        return fields

    @property
    def serializer(self):
        ret = {}

        for field in self.fields:
            if field == 'key':
                value = getattr(self.obj, field, None)
                if value is not None:
                    value = value.id()
                    ret['id'] = value
                continue
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

    def delete(self, *args, **kwargs):
        self.obj.key.delete()
