from django.contrib.auth.models import User
from rest_framework import serializers

from .models import BlogPost


class BlogPostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = BlogPost
        fields = (
            "id",
            "author",
            "title",
            "content",
            "english_content",
            "updated_on",
            "created_on",
        )


class UserSerializer(serializers.ModelSerializer):
    blog_posts = serializers.PrimaryKeyRelatedField(
        many=True, queryset=BlogPost.objects.all()
    )

    class Meta:
        model = User
        fields = ("id", "username", "blog_posts")
