from django.conf.urls import patterns, include, url
from django.contrib import admin
import users.views as view

urlpatterns = patterns('',
    url(r'^$', view.IndexView.as_view(),name='index'),
    url(r'^register/$', view.RegisterView.as_view(),name='register'),
    url(r'^log_in/$', view.LogInView.as_view(),name='log_in'),
    url(r'^log_out/$', view.LogOutView.as_view(),name='log_out'),
)
