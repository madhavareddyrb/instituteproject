from django.db import models
from django.shortcuts import render
from django.contrib.auth.models import User

# Create your models here.
class contact(models.Model):
  name = models.CharField(max_length=100)
  email = models.EmailField()
  message = models.TextField()

def __str__(self):
  return self.name



class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
       return f"{self.user.username}- {self.content[:20]}"

class CourseDetails(models.Model):
  course_name = models.CharField(max_length=100)
  course_fee = models.IntegerField()
  timings = models.TimeField()
  start_date = models.DateField()
  duration = models.IntegerField()
  instructor = models.CharField(max_length=100)