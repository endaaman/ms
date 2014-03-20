#-*-encoding:utf-8-*-
from django.shortcuts import render, render_to_response, get_object_or_404
from django import http
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from models import *
from django.contrib.auth.decorators import user_passes_test, permission_required
from django.core.urlresolvers import reverse


def home(request):
    page = request.GET.get('page', 1)
    page = int(page)
    blogs = Blog.objects.order_by('-pub_date')[(page-1)*5:page*5]
    page_count = Blog.objects.count() / 5
    has_prev = page > 1
    has_next = page - 1 < page_count
    return render_to_response(
        'blog/home.html',
        dict(
            blogs=blogs,
            page=page,
            has_prev=has_prev,
            has_next=has_next,
        ),
        context_instance=RequestContext(request)
    )

def show(request, blog_name):
    blog = get_object_or_404(Blog, url_name=blog_name)

    return render(
        request,
        'blog/show_blog.html',
        dict(
            blog=blog
        ),
        context_instance=RequestContext(request)
    )


