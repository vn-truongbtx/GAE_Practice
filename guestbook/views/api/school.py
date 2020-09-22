
from guestbook.form.school import SchoolForm
from guestbook.models import School
from guestbook.services.school import SchoolHandler
from guestbook.views.generic.detail import DetailView
from guestbook.views.generic.edit import UpdateView, CreateView
from guestbook.views.generic.list import ListView


class ListSchoolView(ListView):
    model = School
    handler = SchoolHandler


class DetailSchoolView(DetailView):
    model = School
    handler = SchoolHandler


class UpdateSchoolView(UpdateView):
    form = SchoolForm
    handler = SchoolHandler


class CreateSchoolView(CreateView):
    form = SchoolForm
    handler = SchoolHandler
