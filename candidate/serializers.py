#-*- encoding: utf-8 -*-
from django.forms import widgets
from rest_framework import serializers
from models import Candidate



class CandidateSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)

        super(CandidateSerializer, self).__init__(*args, **kwargs)

        if fields:
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    class Meta:
        model = Candidate
        fields = ('entry_number',
                  'name',
                  'roman',
                  'kana',
                  'hometown',
                  'department',
                  'grade',
                  'blood_type',
                  'motive',
                  'message',)