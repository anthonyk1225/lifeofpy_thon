from django.conf.urls import patterns, include, url
from django.contrib import admin
<<<<<<< HEAD
from users.views import LogInView,RegisterView,IndexView,WelcomeView,LogOutView
import users.views as view

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'form_practice.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', IndexView.as_view(),name='index'),
    url(r'^welcome/', WelcomeView.as_view(), name='welcome'),
    url(r'^register/$',RegisterView.as_view(),name='register'),
    url(r'^log_in/$', LogInView.as_view(),name='log_in'),
    url(r'^log_out/$', LogOutView.as_view(),name='log_out'),
    url(r'^character_selection/$', ChooseCharView.as_view(), name='createchar'),
=======
import users.views as view

urlpatterns = patterns('',
    url(r'^$', view.IndexView.as_view(),name='index'),
    url(r'^register/$', view.RegisterView.as_view(),name='register'),
    url(r'^log_in/$', view.LogInView.as_view(),name='log_in'),
    url(r'^log_out/$', view.LogOutView.as_view(),name='log_out'),
>>>>>>> 86d43ac4cf97e2116daa9dadc30cab6749b45d74
)
