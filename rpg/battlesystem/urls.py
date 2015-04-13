from django.conf.urls import patterns, include, url
from django.contrib import admin
from battlesystem.views import BattleStart

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'form_practice.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^$', BattleStart.as_view(), name='battle'),
)
