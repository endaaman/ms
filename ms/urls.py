from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin

admin.autodiscover()


from django.conf.urls import patterns, url, include, handler404
from django.views.generic import TemplateView
from rest_framework import routers

import views
import settings
from candidate.views import CandidateViewSet
from photo.views import PhotoViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'candidates', CandidateViewSet)
router.register(r'photos', PhotoViewSet)


api_urlpatterns = patterns(
    '',
    url(r'', include(router.urls)),
    url(r'auth', include('rest_framework.urls', namespace='rest_framework'))
)

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(api_urlpatterns)),
    # url(r'^about/?', TemplateView.as_view(template_name="about.html"), name='about'),
    url(r'^templates/', include('template.urls')),
    url(r'^mail/(?P<addr_type>\S+)/$', 'ms.views.mail', name='mail'),
    url(r'^googlebf07e42e7005708f.html', 'ms.views.anal', name='anal'),
)

urlpatterns += patterns('django.views.static',
    (r'media/(?P<path>.*)', 'serve', {'document_root': settings.MEDIA_ROOT}),
    (r'static/(?P<path>.*)', 'serve', {'document_root': settings.STATIC_ROOT}),
)

# concentrate accesses on index.haml to use angular router
urlpatterns += patterns('',
    url(r'.*', TemplateView.as_view(template_name="index.haml"), name='index'),
)


