
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
USER_ROLE = (('student', 'student'), ('teacher', 'teacher'))
class User(AbstractUser):
    role = models.CharField(max_length=50, choices=USER_ROLE, default='student')


class UnivStudent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subject = models.CharField(name='subject', max_length=50)