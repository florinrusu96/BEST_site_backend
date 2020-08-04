from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path("blog-posts/", views.BlogPostList.as_view()),
    path("blog-posts/<int:pk>/", views.BlogPostDetail.as_view()),
    path("users/", views.UserList.as_view()),
    path("users/<int:pk>/", views.UserDetail.as_view()),
    path('tinymce/', include('tinymce.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)
