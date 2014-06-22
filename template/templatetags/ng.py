# coding: utf-8

from django.template.defaultfilters import register
from django.template.defaultfilters import stringfilter

from django.conf import settings

@register.filter()
@stringfilter
def ng(value):
    return '{{%s}}' % value