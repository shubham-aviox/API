from django.shortcuts import render

# Create your views here.
from api_view_app.models import Student
from api_view_app.serializers import StudentSerializer
from rest_framework import mixins, generics

# class StudentList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def get(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer