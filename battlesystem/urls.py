from django.conf.urls import patterns, include, url
from django.contrib import admin
from battlesystem.views import BattleStart

urlpatterns = patterns('',
	url(r'^(?P<character_id>[0-9]+)/$', BattleStart.as_view(), name='battle'),
)
