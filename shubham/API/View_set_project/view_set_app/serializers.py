from rest_framework import serializers, viewsets
from django.contrib.auth.models import User

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'password', 'email', 'first_name']