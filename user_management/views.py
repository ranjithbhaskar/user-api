from .serializers import *
from .models import *
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
import logging
from django.http import HttpResponse, Http404
import re
from django.db.models import Q
log = logging.getLogger(__name__)


#This the API method for getting user activity 
class UserActivityListApiView(generics.ListAPIView):
    pagination_class = None
    authentication_classes = []
    permission_classes = []
    serializer_class = UserDataSerializer

    def get_queryset(self):
        return UserData.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        final_response = {}
        if queryset:
            final_response['ok'] = True
            final_response['members'] = serializer.data
        else:
            final_response['ok'] = False
            final_response['members'] = []
        return Response(
            final_response,
        )