from google.appengine.ext import ndb


class ModelMixin(object):
    @classmethod
    def list(cls):
        return cls.query().fetch()

    @classmethod
    def update_by_id(cls, _id, **kwargs):
        obj = cls.get_by_id(_id)
        if obj is None:
            return

        for attr, value in kwargs.items():
            setattr(obj, attr, value)
        obj.put()
        return obj

    @classmethod
    def delete_by_id(cls, _id):
        obj = cls.get_by_id(_id)
        if obj is None:
            return
        obj.key.delete()

    def update(self, **kwargs):
        for attr, value in kwargs.items():
            setattr(self, attr, value)
        self.put()
        return self

    def delete(self):
        self.key.delete()


class EntityModel(ndb.Model, ModelMixin):
    created = ndb.DateTimeProperty(auto_now_add=True)
    updated = ndb.DateTimeProperty(auto_now=True)


class Class(EntityModel):
    name = ndb.StringProperty()
    number_of_student = ndb.IntegerProperty()


class School(EntityModel):
    name = ndb.StringProperty()
    class_keys = ndb.KeyProperty(kind=Class, repeated=True)
    is_closed = ndb.BooleanProperty(default=False)


class City(EntityModel):
    name = ndb.StringProperty()
    population = ndb.IntegerProperty()
    gdp = ndb.FloatProperty()
    schools = ndb.StructuredProperty(School, repeated=True)
