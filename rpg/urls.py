from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^battlesystem/', include('battlesystem.urls')),
    url(r'^rpg/', include('users.urls')),
    url(r'^fight/', include('battlesystem.urls')),
    url(r'^users/', include('users.urls')),
    url(r'^$', include('users.urls')),
    url(r'^characters/', include('characters.urls')),
)
