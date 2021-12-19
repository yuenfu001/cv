from django.db import models
from django.urls.base import translate_url

# Create your models here.
class State(models.Model):
    name = models.CharField(max_length=20, null=False)
class name(models.model):
    first_name = models.CharField(max_length=50, null=False, help_text="please your first name is actually your own name")
    last_name = models.CharField(max_length=50, null=False, help_text="please your last name is actually your surname name")
    summary = models.TextField(null=True, help_text="Tell us all little about yourself")
    date_of_birth = models.DateField(null=False)
    date_created = models.DateField(auto_now=True)
    date_updated = models.DateField(auto_now_add=True)