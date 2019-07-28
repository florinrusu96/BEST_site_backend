from django.contrib.auth.models import User
from rest_framework import generics

from .models import Partener
from .serializers import PartenerSerializer


class PartenerList(generics.ListAPIView):
    queryset = Partener.objects.all()
    serializer_class = PartenerSerializer

class PartenerDetail(generics.RetrieveAPIView):
    queryset = Partener.objects.all()
    serializer_class = PartenerSerializer
