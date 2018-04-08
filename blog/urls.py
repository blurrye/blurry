from django.conf.urls import url
from django.views.generic.base import RedirectView

from blog import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/favicon.ico')),
    url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'^TAKI/$', views.taki, name='taki'),
]
