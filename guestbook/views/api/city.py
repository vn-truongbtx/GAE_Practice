from guestbook.form.city import CityForm
from guestbook.models import City
from guestbook.services.city import CityHandler
from guestbook.views.generic import GenericViewset
from guestbook.views.generic.detail import DetailViewMixin
from guestbook.views.generic.edit import UpdateViewMixin, CreateViewMixin, DeleteViewMixin
from guestbook.views.generic.list import ListViewMixin


class CityViewset(GenericViewset, ListViewMixin, DetailViewMixin, UpdateViewMixin, CreateViewMixin, DeleteViewMixin):
    model = City
    handler = CityHandler
    form = CityForm
