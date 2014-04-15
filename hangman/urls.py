__author__ = 'rebecca'

from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
                       url(r'^$', views.hangman, name='hangman'),
                       url(r'^register/', views.register, name='register'),
                       url(r'^login/', views.user_login, name='login'),
                       url(r'^logout/', views.user_logout, name='logout')
    )