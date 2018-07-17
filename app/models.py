from django.db import models
from tinymce.models import HTMLField
import datetime as dt
import datetime

# Create your models here.
class Contact(models.Model):
    Name = models.CharField(max_length = 40)
    email = models.EmailField()
    Phone_Number = models.IntegerField(null=True)
    subject = models.CharField(max_length=40, null = True)
    Question_or_Feedback = HTMLField()

    def __str__(self):
        return self.name

class level(models.Model):
    level = models.CharField(max_length = 30)

    def __str__(self):
        return self.level

class Enroll(models.Model):
    Firstname = models.CharField(max_length = 40)
    Surname = models.CharField(max_length = 40)
    dateofbirth =  models.DateTimeField(auto_now_add=True)
    level = models.ManyToManyField(level)
    Address = models.CharField(max_length = 40)
    Parent_Gurdian_Name = models.CharField(max_length = 40)
    email = models.EmailField()
    Phone_Number = models.IntegerField(null=True)
    datesubmitted = models.DateTimeField(auto_now_add=True)
    Allergies_or_Special_Needs = models.CharField(max_length = 70)

    def __str__(self):
        return self.firstname

class Sponsor(models.Model):
    Firstname = models.CharField(max_length = 40)
    Surname = models.CharField(max_length = 40)
    email = models.EmailField()
    Phone_Number = models.IntegerField(null=True)
