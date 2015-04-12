from django.conf.urls import patterns, include, url
from django.contrib import admin
from characters.views import HeroView
import characters.views as view

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'form_practice.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^warrior/$', 'characters.views.create_warrior', name='createchar'),
	url(r'^mage/$', 'characters.views.create_warrior', name='createchar'),
	url(r'^paladin/$', 'characters.views.create_warrior', name='createchar'),
	url(r'^(?P<name>)[\w\-]+', HeroView.as_view(), name='get'),

)
