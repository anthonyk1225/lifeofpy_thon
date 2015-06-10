from django.conf.urls import patterns, include, url
from django.contrib import admin
import battlesystem.views as view

urlpatterns = patterns('',
    url(r'^battle_log/(?P<character_id>[0-9]+)/$', view.BattleLog.as_view(), name="battle_log"),
	url(r'^(?P<character_id>[0-9]+)/$', view.BattleStart.as_view(), name='battle'),
)
