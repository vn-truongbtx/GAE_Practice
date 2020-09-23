from guestbook.models import School, Class
from guestbook.services import Handler
from guestbook.services.classes import ClassHandler


class SchoolHandler(Handler):
    model = School

    def get_class_keys(self):
        class_serializer = []

        for key in getattr(self.obj, 'class_id', []):
            class_serializer.append(ClassHandler(key.get()).serializer)
        return class_serializer

    def update_class_keys(self, data):
        class_ids = data.pop('class_id', None)
        if class_ids is None:
            return data

        class_keys = []
        for i in class_ids:
            class_keys.append(Class.get_by_id(i).key)

        data['class_id'] = class_keys
        return data

    def update(self, data):
        updated_data = self.update_class_keys(data)

        self.obj.update(**updated_data)

    def create(self, data):
        updated_data = self.update_class_keys(data)
        entity = self.model(**updated_data)
        entity.put()
        self.obj = entity
        return SchoolHandler(entity)

    @staticmethod
    def convert_key_to_id(key):
        return key.id()

    @property
    def serializer(self):
        serializer = super(SchoolHandler, self).serializer
        class_id = serializer.pop('class_id', [])
        for i in range(len(class_id)):
            class_id[i] = self.convert_key_to_id(class_id[i])
        serializer['class_id'] = class_id
        return serializer
