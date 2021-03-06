from rest_framework import serializers

from .models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = (
            "id",
            "event_name",
            "event_banner",
            "event_background",
            "event_pictures",
            "event_description",
            "event_partners",
            "event_google_form",
        )
        depth = 1
