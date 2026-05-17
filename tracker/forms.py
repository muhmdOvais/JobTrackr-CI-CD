from django import forms
from .models import Job
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class JobForm(forms.ModelForm):

    class Meta:
        model = Job
        fields = ['company', 'role', 'status', 'notes']

class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']