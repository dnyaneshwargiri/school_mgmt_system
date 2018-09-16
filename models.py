from django.db import models
import datetime

# Create your models here.
class administrator(models.Model):
    name = models.CharField(max_length=30)
    designation = models.CharField(max_length=20)
    
	
class student(models.Model):
    name = models.CharField(max_length=30)
    rollno = models.CharField(max_length=20)
    classname=models.CharField(max_length=20)
    courseid=models.CharField(max_length=20)
    dob=models.DateField(("Date"))
    addres=models.CharField(max_length=20)
    parentname=models.CharField(max_length=20)

class user(models.Model):
	emailid = models.CharField(max_length=50)
	password = models.CharField(max_length=20)
	role=models.CharField(max_length=20) #student/teacher/parent...'''
