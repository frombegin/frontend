"""frontend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from django.views.generic import TemplateView


class Segmenter(object):
    def __init__(self, iter, step=4):
        self.iter = iter
        self.step = step

    def __iter__(self):
        index = 0
        while True:
            result = self.iter[index: index+self.step]
            if not result:
                raise StopIteration
            yield result
            index += self.step

class MyTemplateView(TemplateView):
    template_name = "pages/index.html"

    def get_context_data(self, **kwargs):
        return {'xobjects': Segmenter( list(xrange(83)), 4), }


urlpatterns = [
                  url(r'^admin/', include(admin.site.urls)),
                  url(r'^$', MyTemplateView.as_view()),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
