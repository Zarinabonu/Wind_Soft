from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from Post.models import Post
from .serializers import PostCreateSerializer


class PostCreate(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer