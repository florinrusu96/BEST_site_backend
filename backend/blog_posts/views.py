from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import permissions

from .models import BlogPost
from .permissions import IsOwnerOrReadOnly
from .serializers import BlogPostSerializer, UserSerializer


class BlogPostList(generics.ListAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class BlogPostDetail(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
