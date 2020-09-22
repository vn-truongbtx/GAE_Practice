from guestbook.models.school import School


class SchoolHandler(object):
    def fetch_all_school(self):
        return School.query().fetch()

    def fetch_school_by_id(self, _id):
        return School.get_by_id(int(_id))

    def create_school_obj(self, name, number_of_class):
        school = School(name=name, number_of_class=int(number_of_class))
        school_key = school.put()
        return school_key.get()

    def delete_school_obj(self, obj):
        obj.key.delete()

    def update_school_obj(self, obj, name, number_of_class):
        obj.name = name
        obj.number_of_class = int(number_of_class)
        obj.put()
        return obj


school_handler = SchoolHandler()
