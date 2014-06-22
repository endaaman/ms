from django.conf.urls import url
from views import *

urlpatterns = (
    url(r'^home.html$', AngularTemplateView.as_view(template_name='home.haml')),
    url(r'^candidates.html$', AngularTemplateView.as_view(template_name='candidates.haml')),
    url(r'^candidates-each.html$', AngularTemplateView.as_view(template_name='candidates-each.haml')),
    url(r'^contest.html$', AngularTemplateView.as_view(template_name='contest.haml')),
    url(r'^vote.html$', AngularTemplateView.as_view(template_name='vote.haml')),    
)