from rest_framework import serializers
from .models import  hexo_config, hexo_theme, hexo_theme_config, hexo_blog_md
from django.contrib.auth.models import User

# HyperlinkedModelSerializer建议和viewsets一起使用，可以自动生成url，且不用自定义url，或者指定fields不带url，注意无法使用exclude对url进行排除

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class hexo_configSerializer(serializers.ModelSerializer):
    class Meta:
        model = hexo_config
        fields = '__all__'


class hexo_themeSerializer(serializers.ModelSerializer):
    class Meta:
        model = hexo_theme
        fields = '__all__'


class hexo_theme_configSerializer(serializers.ModelSerializer):
    class Meta:
        model = hexo_theme_config
        fields = '__all__'

class hexo_blog_mdSerializer(serializers.ModelSerializer):
    class Meta:
        model = hexo_blog_md
        fields = '__all__'
