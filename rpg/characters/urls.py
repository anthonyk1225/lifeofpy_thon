from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'form_practice.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^warrior/$', 'characters.views.create_warrior', name='createwarrior'),
	url(r'^mage/$', 'characters.views.create_mage', name='createmage'),
	url(r'^paladin/$', 'characters.views.create_paladin', name='createpaladin'),
)
