from django.db import models
from django.shortcuts import render

# Create your models here.
class contact(models.Model):
  name = models.CharField(max_length=100)
  email = models.EmailField()
  message = models.TextField()

def __str__(self):
  return self.name



class Comment(models.Model):
    name = models.CharField(max_length=100)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class CourseDetails(models.Model):
  course_name = models.CharField(max_length=100)
  course_fee = models.IntegerField()
  timings = models.TimeField()
  start_date = models.DateField()
  duration = models.IntegerField()
  instructor = models.CharField(max_length=100)