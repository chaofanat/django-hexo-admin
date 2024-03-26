from rest_framework import serializers
from .models import apitest
from django.contrib.auth.models import User
class apitestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = apitest
        fields = '__all__'

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']