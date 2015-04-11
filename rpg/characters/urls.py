from django.conf.urls import patterns, include, url
from django.contrib import admin
from characters.views import CreateCharView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'form_practice.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^character_creation/$', CreateCharView.as_view(), name='createchar'),    
)

    
