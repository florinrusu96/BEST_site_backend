from django.contrib.auth.models import User
from django.db import models


class BlogPost(models.Model):
    author = models.ForeignKey('auth.User',related_name='blog_posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=64, unique=True)
    content = models.TextField()
    updated_on = models.DateField(auto_now=True)
    created_on = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.title
