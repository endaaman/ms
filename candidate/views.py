#-*-encoding:utf-8-*-

from rest_framework.permissions import *
from rest_framework import viewsets
from models import Candidate
from serializers import CandidateSerializer



class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    lookup_field = 'entry_number'
    permission_classes = [IsAuthenticatedOrReadOnly]

    # def get_serializer(self, *args, **kwargs):
    #     fields = self.request.GET.get('fields', None)
    #     if fields:
    #         kwargs['fields'] = fields
    #     return super(CandidateViewSet, self).get_serializer(*args, **kwargs)
