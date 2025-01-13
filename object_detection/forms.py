from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import ModelForm
from django.contrib.auth.models import User
from object_detection.models import PeopleReg


class LoginForm (AuthenticationForm):
    class Meta:
        model=User
        fields=['username','password']
    username=forms.CharField()
    password = forms.CharField()



class RegisterForm (UserCreationForm):
    class Meta:
        model=User
        fields=[
            'username',
            'password',
            'password2',
        ]