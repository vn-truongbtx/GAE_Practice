from guestbook.models import City
from guestbook.services import Handler
from guestbook.services.school import SchoolHandler


class CityHandler(Handler):
    model = City

    def get_schools(self):
        school_serializer = []

        for school in getattr(self.obj, 'schools', []):
            school_serializer.append(SchoolHandler(school).serializer)
        return school_serializer

    def update_school(self, data):
        schools = data.pop('schools', None)
        updated_schools = []

        for school in schools:
            id_school = school.pop('id')
            handler = SchoolHandler(_id=int(id_school))
            handler.update(school)
            updated_schools.append(handler.serializer)
        data['schools'] = updated_schools
        return data

    def update(self, data):
        updated_data = self.update_school(data)
        self.obj.update(updated_data)

    def create_school(self, data):
        schools = data.pop('schools', None)
        ret = []
        handler = SchoolHandler()

        for school in schools:
            ret.append(handler.create(school).obj)

        data['schools'] = ret
        return data

    def create(self, data):
        modified_data = self.create_school(data)
        entity = self.model(modified_data)
        entity.put()
        return CityHandler(entity)
