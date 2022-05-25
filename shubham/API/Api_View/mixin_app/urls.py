from django.contrib import admin
from django.urls import path, include
from mixin_app import views

urlpatterns = [
    path('', views.StudentList.as_view()),
    path('/details/<int:pk>', views.StudentDetail.as_view()),
]