from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import State, Name

class CreateInfoForm(forms.ModelForm):
    class Meta:
        model = Name
        fields = ["first_name","last_name","state_of_origin","date_of_birth","summary"]