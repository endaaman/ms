#-*- encoding: utf-8 -*-
from django.db import models
from django import forms
from django.utils import html
import markdown2


class Blog(models.Model):
    title = models.CharField(max_length=200, blank=False, verbose_name="タイトル")
    url_name = models.CharField(max_length=100, verbose_name='名前')
    message = models.TextField(blank=False, verbose_name="本文")
    message_html = models.TextField(blank=True)
    raw_message = models.TextField(blank=True)
    pub_date = models.DateTimeField(auto_now_add=True, editable=False, verbose_name="投稿日時")
    author = models.CharField(max_length=100, blank=False, verbose_name='投稿者')

    class Meta:
        verbose_name = verbose_name_plural = 'ブログ'

    def __unicode__(self):
        return self.title

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        md = markdown2.Markdown()
        encoded_html = md.convert(self.message)
        raw_text = html.strip_tags(encoded_html)
        self.raw_message = raw_text
        self.message_html = encoded_html
        return super(Blog, self).save(force_insert, force_update, using, update_fields)

    def message_stripped(self):
        return self.raw_message[0:40]


