from django import http
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect


def mail(request):
    if request.method == 'POST':
        return http.HttpResponse('ms.hokudai@gmail.com', mimetype='text/plain')
    else:
        return http.HttpResponse('ms.hokudai@gmail.com', mimetype='text/plain')


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
