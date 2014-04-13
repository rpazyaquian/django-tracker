__author__ = 'rebecca'

from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^addapp/$', views.addapp, name='addapp'),
                       url(r'^user/(?P<username>[\w\.\-\+_@]+)/$', views.apps, name='apps'),
                       url(r'^register/$', views.register, name='register'),
                       url(r'^login/$', views.user_login, name='login'),
                       url(r'^logout/$', views.user_logout, name='logout'),
                       url(r'^delete/(?P<app_id>\w+)/$', views.delete, name='delete'),
                       url(r'^edit/(?P<app_id>\w+)/$', views.edit, name='edit'),
    )