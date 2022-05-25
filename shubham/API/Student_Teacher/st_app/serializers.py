from rest_framework import serializers
from .models import User

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'role']
        extra_kwargs = {
            'password':{'write_only': True},
        }

    def create(self, validated_data):
        try:
            user = User.objects.create_user(username=validated_data['username'], email=validated_data['email'], password = validated_data['password'], role = validated_data['role'])
            return user
        except Exception as e:
            return Exception


class GetUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'role']