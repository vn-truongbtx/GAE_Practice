# -*- coding: utf-8 -*-
from django.conf.urls import url
# from django.conf.urls.defaults import *
from guestbook.router import Router
from guestbook.views import IndexView
from guestbook.views.api.city import CityViewset
from guestbook.views.api.classes import ClassViewset
from guestbook.views.api.school import SchoolViewset

router = Router()
router.register('city', CityViewset)
router.register('school', SchoolViewset)
router.register('class', ClassViewset)

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
]

urlpatterns += router.urls
