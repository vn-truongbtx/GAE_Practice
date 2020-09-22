from guestbook.form.classes import ClassForm
from guestbook.models import Class
from guestbook.services.classes import ClassHandler
from guestbook.views.generic.detail import DetailView
from guestbook.views.generic.edit import UpdateView, CreateView
from guestbook.views.generic.list import ListView


class ListClassesView(ListView):
    model = Class
    handler = ClassHandler


class DetailClassesView(DetailView):
    model = Class
    handler = ClassHandler


class UpdateClassesView(UpdateView):
    form = ClassForm
    handler = ClassHandler


class CreateClassesView(CreateView):
    form = ClassForm
    handler = ClassHandler

