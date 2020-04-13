from rest_framework import serializers
from news.models import News
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username']

class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = ['id','author','title','text']