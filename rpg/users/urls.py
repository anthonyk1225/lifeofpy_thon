from django.conf.urls import patterns, include, url
from django.contrib import admin
from users.views import LogInView,RegisterView,IndexView,WelcomeView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'form_practice.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', IndexView.as_view(),name='index'),
    url(r'^welcome_page/$', WelcomeView.as_view(),name='welcome_page'),
    url(r'^register/$',RegisterView.as_view(),name='register'),
    url(r'^log_in/$', LogInView.as_view(),name='log_in'),
)