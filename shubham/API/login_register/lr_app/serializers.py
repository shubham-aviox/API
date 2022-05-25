from dataclasses import fields
from doctest import Example
from rest_framework import  serializers
from django.db import models
from django.contrib.auth.models import User


# Register serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','password','first_name', 'last_name','email')
        extra_kwargs = {
            'password':{'write_only': True},
        }
        
    def create(self, validated_data):
        try:
            user = User.objects.create_user(username=validated_data['username'], email=validated_data['email'], password = validated_data['password'],first_name=validated_data['first_name'], last_name=validated_data['last_name'])
            return user
        except Exception as e:
            return Exception
            

class GetUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name','email')