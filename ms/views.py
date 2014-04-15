from django import http
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import base

@csrf_exempt
def mail(request):
    return http.HttpResponse('n/a', mimetype='text/plain')
    if request.method == 'POST':
        return http.HttpResponse('n/a', mimetype='text/plain')
    else:
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
