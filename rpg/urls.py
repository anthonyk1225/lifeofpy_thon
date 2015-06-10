from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^characters/', include('characters.urls')),
    url(r'^battlesystem/', include('battlesystem.urls', namespace='battlesystem')),
    url(r'^rpg/', include('users.urls')),
    url(r'^users/', include('users.urls')),
    url(r'^/$', include('users.urls')),
    url(r'^$', include('users.urls')),
)
