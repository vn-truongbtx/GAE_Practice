from google.appengine.ext import ndb


class School(ndb.Model):
    name = ndb.StringProperty()
    number_of_class = ndb.IntegerProperty()
