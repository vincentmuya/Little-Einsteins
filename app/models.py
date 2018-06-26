from django.db import models
from tinymce.models import HTMLField
# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length = 40)
    email = models.EmailField()
    phonenumber = models.IntegerField(null=True)
    questionfeedback = HTMLField()
