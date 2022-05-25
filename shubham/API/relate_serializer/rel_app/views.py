from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import AlbumSerializer
from .models import Album
from rest_framework import status

# Create your views here.
class AlbumView(APIView):
    def get(self, request):
        album = Album.objects.all()
        serializer = AlbumSerializer(album, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
