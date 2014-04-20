from django import http
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import base


@csrf_exempt
def mail(request, mail_type=None):
    if request.method == 'POST' and mail_type:
        addr_table = dict(
            main='2014mshu@gmail.com',
            recruit='shinkan.2014mshu@gmail.com'
        )
        addr = addr_table.get(mail_type, None)
        if addr:
            return http.HttpResponse(addr, content_type='text/plain')

    return http.HttpResponseForbidden()


def home(request):
    return render_to_response('home.html',
                              {},
                              context_instance=RequestContext(request))

def about(request):
    return render_to_response('about.html',
                              {},
                              context_instance=RequestContext(request))

def contact(request):
    return render_to_response('contact.html',
                              {},
                              context_instance=RequestContext(request))
