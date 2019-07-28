from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Partener


class PartenerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partener
        fields = ('name', 'logo', 'group')

