# -*- coding: utf-8 -*-
from django.conf.urls import url
# from django.conf.urls.defaults import *
from guestbook.views import IndexView
from guestbook.views.api import SchoolView

url_city = [
    url(r'^api/city/$', SchoolView.as_view(), name='get_post_school'),
    url(r'^api/city/(?P<city_id>\d+)/update/$', SchoolView.as_view(), name='update_school'),
]

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^api/school/$', SchoolView.as_view(), name='get_post_school'),
    url(r'^api/school/(?P<school_id>\d+)/$', SchoolView.as_view(), name='get_school'),
    url(r'^api/school/(?P<school_id>\d+)/update/$', SchoolView.as_view(), name='update_school'),
    url(r'^api/school/(?P<school_id>\d+)/delete/$', SchoolView.as_view(), name='delete_school'),
]
