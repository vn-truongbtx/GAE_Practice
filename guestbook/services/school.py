from guestbook.models import School, Class
from guestbook.services import Handler
from guestbook.services.classes import ClassHandler


class SchoolHandler(Handler):
    model = School

    def get_class_keys(self):
        class_serializer = []

        for key in getattr(self.obj, 'class_keys', []):
            class_serializer.append(ClassHandler(key.get()).serializer)
        return class_serializer

    def update_class_keys(self, data):
        class_ids = data.pop('class_keys', None)
        class_keys = []
        for i in class_ids:
            class_keys.append(Class.get_by_id(i).key)

        data['class_keys'] = class_keys
        return data

    def update(self, data):
        updated_data = self.update_class_keys(data)

        self.obj.update(updated_data)

    def create(self, data):
        updated_data = self.update_class_keys(data)
        entity = self.model(updated_data)
        entity.put()
        return SchoolHandler(entity)
