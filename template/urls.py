from django.conf.urls import url
from views import *

v = AngularTemplateView.as_view

urlpatterns = (
    url(r'^home.html$', v(template_name='home.haml')),
    url(r'^candidates.html$', v(template_name='candidates.haml')),
    url(r'^candidates-each.html$', v(template_name='candidates-each.haml')),
    url(r'^contest.html$', v(template_name='contest.haml')),
    url(r'^vote.html$', v(template_name='vote.haml')),
)
