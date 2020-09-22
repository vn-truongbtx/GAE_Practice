from guestbook.form.city import CityForm
from guestbook.models import City
from guestbook.services.city import CityHandler
from guestbook.views.generic.detail import DetailView
from guestbook.views.generic.edit import UpdateView, CreateView
from guestbook.views.generic.list import ListView


class ListCityView(ListView):
    model = City
    handler = CityHandler


class DetailCityView(DetailView):
    model = City
    handler = CityHandler


class UpdateCityView(UpdateView):
    form = CityForm
    handler = CityHandler


class CreateCityView(CreateView):
    form = CityForm
    handler = CityHandler