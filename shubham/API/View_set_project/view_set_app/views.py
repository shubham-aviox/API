from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import RegistrationSerializer
from rest_framework import permissions
from .permissions import IsUserReadOnly

# Create your views here.
class RegisterViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = User.objects.all()
    print(queryset)
    serializer_class = RegistrationSerializer