from django.conf.urls import patterns, url
from ToDo import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'))