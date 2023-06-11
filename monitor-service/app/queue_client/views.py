from django.shortcuts import render

# Create your views here.

from queue_client.models import QueueConnection
from queue_client.serializers import QueueConnectionSerializer
from rest_framework import generics


class QueueConnectionList(generics.ListCreateAPIView):
    queryset = QueueConnection.objects.all()
    serializer_class = QueueConnectionSerializer


class QueueConnectionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = QueueConnection.objects.all()
    serializer_class = QueueConnectionSerializer