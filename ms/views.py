from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect


@csrf_protect
def home(request):
    return render_to_response('home.html',
                              {},
                              context_instance=RequestContext(request))
