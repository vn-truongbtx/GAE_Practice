from guestbook.form.classes import ClassForm
from guestbook.models import Class
from guestbook.services.classes import ClassHandler
from guestbook.views.generic import GenericViewset
from guestbook.views.generic.detail import DetailViewMixin
from guestbook.views.generic.edit import UpdateViewMixin, CreateViewMixin, DeleteViewMixin
from guestbook.views.generic.list import ListViewMixin


class ClassViewset(GenericViewset, ListViewMixin, DetailViewMixin, UpdateViewMixin, CreateViewMixin, DeleteViewMixin):
    model = Class
    handler = ClassHandler
    form = ClassForm
