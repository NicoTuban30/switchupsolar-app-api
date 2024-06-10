from rest_framework import serializers

# from .models import SendMessage


class SendMessageSerializer(serializers.Serializer):

    msg = serializers.CharField(max_length=1000)
    num = serializers.CharField(max_length=20)


class WebhookSerializer(serializers.Serializer):
    Body = serializers.CharField(max_length=1000)
    From = serializers.CharField(max_length=20)
