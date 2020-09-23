from google.appengine.ext import ndb

from guestbook.models import City
from guestbook.services import Handler
from guestbook.services.school import SchoolHandler


class CityHandler(Handler):
    model = City

    def get_schools(self):
        schools = getattr(self.obj, 'schools', None)
        if schools is not None:
            return SchoolHandler(schools).serializer

    def update_school(self, data):
        if 'schools' not in data:
            return data

        schools = data.pop('schools', None)

        id_school = schools.pop('id')
        handler = SchoolHandler(_id=int(id_school))
        handler.update(schools)
        data['schools'] = handler.serializer
        return data

    @ndb.transactional(xg=True)
    def update(self, data):
        updated_data = self.update_school(data)
        self.obj.update(**updated_data)

    def create_school(self, data):
        schools = data.pop('schools', None)
        handler = SchoolHandler(_id=schools)

        data['schools'] = handler.obj
        return data

    @ndb.transactional(xg=True)
    def create(self, data):
        modified_data = self.create_school(data)
        entity = self.model(**modified_data)
        entity.put()
        self.obj = entity
        return CityHandler(entity)
