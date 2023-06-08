from django.shortcuts import render
from django.http.response import HttpResponse, Http404
from blogging.models import Post
from django.template import loader
from django.views.generic import ListView
from django.views.generic import DetailView


# Create your views here


class PostListView(ListView):
    published = Post.objects.exclude(published_date__exact=None)
    queryset = published.order_by("-published_date")
    template_name = "blogging/list.html"


class PostDetailView(DetailView):
    queryset = Post.objects.exclude(published_date__exact=None)
    template_name = "blogging/detail.html"
