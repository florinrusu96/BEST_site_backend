from django.db import models
from tinymce.models import HTMLField

class BlogPost(models.Model):
    author = models.ForeignKey(
        "auth.User", related_name="blog_posts", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=64, unique=True)
    content = HTMLField()
    english_content = HTMLField()
    updated_on = models.DateField(auto_now=True)
    created_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
