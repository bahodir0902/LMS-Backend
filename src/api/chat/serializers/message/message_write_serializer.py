from rest_framework import serializers

from src.apps.chat.models import Message


class MessageWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ["content", "file"]

    def create(self, validated_data):
        validated_data["sender"] = self.context["request"].user
        validated_data["chat_room"] = self.context["chat_room"]
        return super().create(validated_data)
