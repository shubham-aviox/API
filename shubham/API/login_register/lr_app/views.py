
from urllib import request
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from .serializers import GetUserSerializer, RegisterSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class RegisterView(APIView):
    def post(self, request):
        response = {}
        try:
            signup_serializer = RegisterSerializer(data=request.data)
            if signup_serializer.is_valid():
                signup_serializer.save()
                response["status"] = status.HTTP_201_CREATED
                response["message"] = status.HTTP_201_CREATED
            else:
                response["status"] = status.HTTP_400_BAD_REQUEST
                response["message"] = signup_serializer.errors
        except Exception as e:
            response["status"] = status.HTTP_400_BAD_REQUEST
            response["message"] = str(e)
        return Response(response)


class AllUser(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            user = User.objects.all()
            serializer = GetUserSerializer(user, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


