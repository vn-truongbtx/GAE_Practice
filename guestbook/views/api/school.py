from guestbook.form.school import SchoolForm
from guestbook.models import School
from guestbook.services.school import SchoolHandler
from guestbook.views.generic import GenericViewset
from guestbook.views.generic.detail import DetailViewMixin
from guestbook.views.generic.edit import UpdateViewMixin, CreateViewMixin, DeleteViewMixin
from guestbook.views.generic.list import ListViewMixin


class SchoolViewset(GenericViewset, ListViewMixin, DetailViewMixin, UpdateViewMixin, CreateViewMixin, DeleteViewMixin):
    model = School
    handler = SchoolHandler
    form = SchoolForm
