from django.conf.urls import patterns, include, url
from django.contrib import admin
from characters.views import HeroView, WelcomeView,CharacterListView
import characters.views as view

urlpatterns = patterns('',
    url(r'^$', view.WelcomeView.as_view(), name='welcome'),
    url(r'^list/$', view.CharacterListView.as_view(), name='character_list'),
    url(r'^character_selection/$', view.ChooseCharView.as_view(), name='create_character'),
    url(r'^warrior/$', view.create_warrior, name='create_warrior'),
    url(r'^mage/$', view.create_mage, name='create_mage'),
    url(r'^paladin/$', view.create_paladin, name='create_paladin'),
    url(r'^(?P<name>[\w\-]+)', HeroView.as_view(), name='get'),
)
