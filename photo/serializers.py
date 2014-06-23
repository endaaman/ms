#-*- encoding: utf-8 -*-
from rest_framework import serializers
from models import Photo


class PhotoSerializer(serializers.HyperlinkedModelSerializer):

    candidate = serializers.RelatedField(many=False)
    image = serializers.SerializerMethodField('image_url')
    thumb = serializers.SerializerMethodField('thumb_url')

    def image_url(self, obj):
        return obj.image.url

    def thumb_url(self, obj):
        return obj.thumb.url

    class Meta:
        model = Photo
        fields = (
            'candidate',
            'image',
            'thumb',
            'title',
            'desc',
            'index',
        )
