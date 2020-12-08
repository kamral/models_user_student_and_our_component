from django.db import models
from account.models import User
# Create your models here.

class  Student(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50,null=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    telephone_number=models.CharField(max_length=100)
    faculty=models.CharField(max_length=100)
    course=models.PositiveIntegerField(null=True, blank=True)
    direction=models.CharField(max_length=100)








