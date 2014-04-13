__author__ = 'rebecca'

from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
                       url(r'^$', views.resume, name='resume'),
    )