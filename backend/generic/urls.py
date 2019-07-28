from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('parteners/', views.PartenerList.as_view()),
    path('parteners/<int:pk>/', views.PartenerDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
