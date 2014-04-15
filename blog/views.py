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

def show(request, url_name):
    blog = get_object_or_404(Blog, url_name=url_name)

    return render(
        request,
        'blog/show.html',
        dict(
            blog=blog
        ),
        context_instance=RequestContext(request)
    )


@user_passes_test(lambda u: u.has_module_perms('blog'))
def edit_blog(request, blog_name=None):

    if blog_name is None:
        blog = Blog()
    else:
        blog = get_object_or_404(Blog, url_name=blog_name)

    if request.POST:
        blog_form = BlogForm(request.POST, instance=blog)
        v = blog_form.is_valid()
        if v:
            blog = blog_form.save()
            blog_name = blog.url_name

        v_flag = request.GET.get('validation', None)
        if v_flag != 'true':
            # ajaxでない
            if v:
                # validならリダイレクト
                return http.HttpResponseRedirect(reverse('blog.show', args=(blog_name,)))
            else:
                # invalidなら下で処理
                context = request.POST
        else:
            # ajaxなときvalid,invalid問わず
            import json
            content = dict(result=v, errors=blog_form.errors, redirect_to=reverse('blog.show', args=(blog_name,)))
            return http.HttpResponse(json.dumps(content), mimetype='text/plain')

    else:
        context = {}
        blog_form = BlogForm(instance=blog)

    return render_to_response('blog/edit_blog.html',
                              dict(
                                  blog=blog,
                                  blog_form=blog_form,
                              ),
                              context_instance=RequestContext(request, context))

