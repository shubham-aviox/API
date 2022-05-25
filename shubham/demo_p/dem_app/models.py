from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=30)
    roll_number=models.IntegerField()
    email=models.EmailField()
    phone=models.CharField(max_length=12)
    address=models.TextField()

    def __str__(self):
        return self.name