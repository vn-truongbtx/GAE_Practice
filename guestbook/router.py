from django.conf.urls import url


class Router(object):
    def __init__(self):
        self.registers = []

    def register(self, url, view):
        self.registers.append([url, view])

    @property
    def urls(self):
        urls = []
        for source, view in self.registers:
            url_regexs = self.generate_url(source)
            urls.extend([url(u, view.as_view()) for u in url_regexs])
        return urls

    def generate_url(self, source):
        ret = []
        patterns = ['^api/{}/$', '^api/{}/(?P<id>\d+)/$']
        for p in patterns:
            ret.append(p.format(source))

        return ret
