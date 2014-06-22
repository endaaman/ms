#-*-encoding:utf-8-*-

from rest_framework.permissions import *
from rest_framework import viewsets, filters
from models import Photo
from serializers import PhotoSerializer
import django_filters


class PhotoFilter(django_filters.FilterSet):
    candidate = django_filters.CharFilter(name="candidate__entry_number")
    class Meta:
        model = Photo
        fields = ['candidate', ]

class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_class = PhotoFilter