from django.shortcuts import render

# Create your views here.

from .models import apitest
from rest_framework import viewsets
from .serializers import apitestSerializer

class apitestViewSet(viewsets.ModelViewSet):
    queryset = apitest.objects.all()
    serializer_class = apitestSerializer

from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework import permissions
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]