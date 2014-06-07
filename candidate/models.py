#-*- encoding: utf-8 -*-
from django.db import models


class Candidate(models.Model):
    entry_number = models.IntegerField(null=True, default=0, verbose_name='エントリーナンバー')
    name = models.CharField(max_length=100, blank=True, null=True, verbose_name="名前")
    roman = models.CharField(max_length=100, blank=True, null=True, verbose_name="ローマ字")
    kana = models.CharField(max_length=100, blank=True, null=True, verbose_name='よみがな')
    hometown = models.CharField(max_length=100, blank=True, null=True, verbose_name='出身地')
    department = models.CharField(max_length=100, blank=True, null=True, verbose_name='学部')
    grade = models.IntegerField(null=True, default=0, verbose_name='学年')
    blood_type = models.CharField(max_length=5, blank=True, null=True, verbose_name='血液型')
    motive = models.TextField(blank=True, null=True, verbose_name='動機')
    message = models.TextField(blank=True, null=True, verbose_name='メッセージ')

    class Meta:
        verbose_name = verbose_name_plural = '候補者'

    def __unicode__(self):
        return 'No.%d - %s' % (self.entry_number, self.name)