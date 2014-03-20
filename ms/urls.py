from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import settings


urlpatterns = patterns('',
    url(r'^$', 'ms.views.home', name='home'),
    url(r'^about/$', 'ms.views.about', name='about'),
    url(r'^mail/$', 'ms.views.mail', name='mail'),
    # url(r'^candidate/', include('blog.urls')),

    url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)



urlpatterns += patterns('django.views.static',
    (r'media/(?P<path>.*)', 'serve', {'document_root': settings.MEDIA_ROOT}),
    (r'static/(?P<path>.*)', 'serve', {'document_root': settings.STATIC_ROOT}),
)