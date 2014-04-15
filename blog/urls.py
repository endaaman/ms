from django.conf.urls import patterns, url

import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='blog.home'),
    url(r'^(?P<url_name>\S+)/$', views.show, name='blog.show'),
)