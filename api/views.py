from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics ,filters
from rest_framework.parsers import JSONParser
from .models import Posts
from rest_framework import status
from .serializers import SongsSerializer
from rest_framework.decorators import api_view
import csv


class ListSongsView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Posts.objects.all()
    serializer_class = SongsSerializer
    search_fields = ['title', 'label']
    filter_backends = (filters.SearchFilter,)


class CreateSong(generics.ListCreateAPIView):
    """
    Provides a post method handler.
    """
    queryset = Posts.objects.all()
    serializer_class = SongsSerializer


class ExampleView(APIView):
    """
    A view that can accept POST requests with JSON content.
    """
    parser_classes = [JSONParser]

    def post(self, request, format=None ,*args, **kwargs):
        respon = request.data['name']
        
        return Response({'received data': respon})