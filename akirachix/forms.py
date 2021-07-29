from django import forms
from django.forms import fields
from.models import student

class StudentRegistrationForm(forms.modelForm):
class Meta: 
    # tells the parent class what to do
    model=Student
    fields="__all__"