from django.db import models
from tinymce.models import HTMLField
import datetime as dt
import datetime

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length = 40)
    email = models.EmailField()
    phonenumber = models.IntegerField(null=True)
    questionfeedback = HTMLField()

    def __str__(self):
        return self.name

class level(models.Model):
    level = models.CharField(max_length = 30)

    def __str__(self):
        return self.level

class Enroll(models.Model):
    firstname = models.CharField(max_length = 40)
    surname = models.CharField(max_length = 40)
    dateofbirth = models.DateField(auto_now_add=True)
    level = models.ManyToManyField(level)
    address = models.CharField(max_length = 40)
    parentgurdianname = models.CharField(max_length = 40)
    email = models.EmailField()
    phonenumber = models.IntegerField(null=True)
    datesubmitted = models.DateTimeField(auto_now_add=True)
    allergiesspecial = models.CharField(max_length = 70)

    def __str__(self):
        return self.firstname
