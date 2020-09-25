from django.conf.urls import url

from api_search.views import index, text_search, add

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'add/', add, name='add'),
    url(r'^s', text_search, name='search')
]