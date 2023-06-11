from django.shortcuts import render

# Create your views here.

from queue_client.models import QueueConnection
from queue_client.serializers import QueueConnectionSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
from requests.exceptions import ConnectionError, HTTPError

class QueueConnectionList(generics.ListCreateAPIView):
    queryset = QueueConnection.objects.all()
    serializer_class = QueueConnectionSerializer


class QueueConnectionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = QueueConnection.objects.all()
    serializer_class = QueueConnectionSerializer

    
class CheckQueueConnection(APIView):
    
    def post(self, request):
        queue_name = request.query_params['name']
        queue_connection = QueueConnection.objects.filter(name=queue_name).first().url
        method = request.data['method']
        path = request.data['path']
        
        if (method != 'GET'):
            return Response({ "error": "Only GET method support" }, status=status.HTTP_501_NOT_IMPLEMENTED)
        
        url = f"{queue_connection}{path}"
        
        try:
            result = requests.get(url)
            result.raise_for_status()
        except (HTTPError, ConnectionError)  as err:
            return Response({"error": str(err) },  status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(result.json(), status=status.HTTP_200_OK)
        