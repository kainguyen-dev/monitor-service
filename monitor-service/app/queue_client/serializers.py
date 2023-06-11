from rest_framework import serializers
from queue_client.models import QueueConnection


class QueueConnectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QueueConnection
        fields = ['created', 'name', 'url', 'active']