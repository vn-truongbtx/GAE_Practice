from guestbook.models import Class
from guestbook.services import Handler


class ClassHandler(Handler):
    model = Class

    def update(self, data):
        self.obj.update(**data)

    def create(self, data):
        entity = self.model(**data)
        entity.put()
        self.obj = entity
        return ClassHandler(entity)
