from django.http import Http404
from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import GetUserSerializer, RegisterSerializer
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import User
from .permissions import IsTeacher

# Create your views here.
class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserView(APIView):
    # permission_classes = [permissions.IsAuthenticated, IsTeacher]
    def get(self, request):
        user = User.objects.all()
        serializer = GetUserSerializer(user, many=True)
        return Response(serializer.data)


class UpdateView(APIView):
    def get_user(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404
    permission_classes = [permissions.IsAuthenticated, IsTeacher]
    def put(self, request, pk):
        user = self.get_user(pk)
        serializer = RegisterSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)