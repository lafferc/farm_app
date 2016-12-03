from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<tour_name>\w+)/$', views.submit, name='submit'),
    url(r'^(?P<tour_name>\w+)/predictions/$', views.predictions, name='predictions'),
    url(r'^(?P<tour_name>\w+)/table/$', views.table, name='table'),
]
