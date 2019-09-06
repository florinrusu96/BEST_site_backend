from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path("partners/", views.PartnerList.as_view()),
    path("partners/<int:pk>/", views.PartnerDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
