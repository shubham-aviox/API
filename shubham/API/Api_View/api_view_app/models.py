from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=30)
    course = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    owner = models.ForeignKey('auth.user', related_name='student', null=True, on_delete=models.CASCADE)