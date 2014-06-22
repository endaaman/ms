# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Candidate'
        db.create_table(u'candidate_candidate', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('entry_number', self.gf('django.db.models.fields.IntegerField')(default=0, null=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('roman', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('kana', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('hometown', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('department', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('grade', self.gf('django.db.models.fields.IntegerField')(default=0, null=True)),
            ('blood_type', self.gf('django.db.models.fields.CharField')(max_length=5, null=True, blank=True)),
            ('motive', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('message', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'candidate', ['Candidate'])


    def backwards(self, orm):
        # Deleting model 'Candidate'
        db.delete_table(u'candidate_candidate')


    models = {
        u'candidate.candidate': {
            'Meta': {'object_name': 'Candidate'},
            'blood_type': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'department': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'entry_number': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True'}),
            'grade': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True'}),
            'hometown': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kana': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'motive': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'roman': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['candidate']