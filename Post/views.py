from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from Post.models import Post


class PostListView(ListView):
    queryset = Post.objects.all()
    context_object_name = 'posts'
    template_name = ''

class PostCreateView(TemplateView):
    template_name = ''



# Create your views here.
