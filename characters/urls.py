from django.conf.urls import patterns, include, url
from django.contrib import admin
import characters.views as view

urlpatterns = patterns('',
    url(r'^$', view.WelcomeView.as_view(), name='welcome'),
    url(r'^list/$', view.ListHeroView.as_view(), name='hero_list'),
    url(r'^create/$', view.CreateHeroView.as_view(), name='create_hero'),
    url(r'^edit/$', view.EditHeroView.as_view(), name='edit_hero'),
    url(r'^delete/$', view.DeleteHeroView.as_view(), name='delete_hero'),
    url(r'^(?P<character_id>[0-9]+)/', view.HeroView.as_view(), name='get_hero'),
)
