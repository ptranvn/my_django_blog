from django.shortcuts import render
from django.http.response import HttpResponse, Http404
from blogging.models import Post
from django.template import loader
from django.views.generic import ListView
from django.views.generic import DetailView

from mysite.blogging.models import Category
from mysite.blogging.serializers import PostSerializer
from rest_framework import permissions
from rest_framework import viewsets
from mysite.quickstart.serializers import CategorySerializer


# Create your views here


class PostListView(ListView):
    published = Post.objects.exclude(published_date__exact=None)
    queryset = published.order_by("-published_date")
    template_name = "blogging/list.html"


class PostDetailView(DetailView):
    queryset = Post.objects.exclude(published_date__exact=None)
    template_name = "blogging/detail.html"


class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    published = Post.objects.exclude(published_date__exact=None)
    queryset = published.order_by("-published_date")
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Post.objects.exclude(published_date__exact=None)
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]