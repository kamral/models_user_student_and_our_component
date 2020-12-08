from django.db import models
from account.models import User
# Create your models here.

class PhoneNmuber(models.Model):
    phone_number=models.PositiveIntegerField(null=True,blank=True)

class Course(models.Model):
    kurs_number=models.PositiveIntegerField(null=True, blank=True)

class Faculty(models.Model):
    faculty_number=models.PositiveIntegerField(null=True,blank=True)

class Direction(models.Model):
    direction_name=models.CharField(max_length=100)

class Room(models.Model):
    room_number=models.PositiveIntegerField(null=True,blank=True)

class  Student(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50,null=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    telephone_number=models.ForeignKey(PhoneNmuber, on_delete=models.CASCADE)
    faculty=models.ForeignKey(Faculty,on_delete=models.CASCADE)
    course=models.ForeignKey(Course, on_delete=models.CASCADE)
    direction=models.ForeignKey(Direction,on_delete=models.CASCADE)
    room=models.ForeignKey(Room,on_delete=models.CASCADE)









