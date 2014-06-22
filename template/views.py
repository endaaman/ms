from django import http
from django.views.generic import TemplateView


class AngularTemplateView(TemplateView):
    def dispatch(self, request, *args, **kwargs):
        # if not request.is_ajax():
        #     raise http.Http404()
        return super(AngularTemplateView, self).dispatch(request, *args, **kwargs)