from django.shortcuts import render
from django.http  import HttpResponse
from .models import Post
from django.views.generic import (
    ListView
)


# Create your views here.
class PostListView(ListView):
    template_name = "post.html"
    queryset = Post.objects.all()
    context_object_name = "posts"