from django.contrib.auth.models import User, Group
from rest_framework import serializers

from mysite.blogging.models import Category


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'text', 'created_date', 'modified_date', 'published_date']


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['url', 'name', 'description', 'posts']