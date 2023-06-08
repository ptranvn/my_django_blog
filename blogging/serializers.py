from django.contrib.auth.models import User, Group
from rest_framework import serializers
from blogging.models import Post


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = [
            "url",
            "title",
            "text",
            "author",
            "created_date",
            "modified_date",
            "published_date",
        ]
