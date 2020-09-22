# -*- coding: utf-8 -*-

from django.views.generic import TemplateView

class IndexView(TemplateView):
	template_name = 'guestbook/index.html'

	def get(self, request, *args, **kwargs):
		return self.render_to_response({})
