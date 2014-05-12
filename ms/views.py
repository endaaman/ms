from django import http
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import base


@csrf_exempt
def mail(request, addr_type=None):
    # if request.method == 'POST' and addr_type:
    if addr_type:
        addr_table = dict(
            main='mshu2014@gmail.com',
            recruit='mshu2014mshu@gmail.com',
            entry='mshu2014.entry@gmail.com'
        )
        addr = addr_table.get(addr_type, None)
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


def anal(request):
    return http.HttpResponse('google-site-verification: googlebf07e42e7005708f.html', content_type='text/html')
