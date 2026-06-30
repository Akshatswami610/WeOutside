from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            "event_id",
            "user",
            "event_name",
            "event_category",
            "description",
            "poster",
            "max_members",
            "fee",
            "gender",
            "age_limit",
            "location",
            "event_date",
            "event_time",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "event_id",
            "user",
            "created_at",
            "updated_at",
        ]

    def create(self, validated_data):
        return Event.objects.create(
            user=self.context["request"].user,
            **validated_data
        )