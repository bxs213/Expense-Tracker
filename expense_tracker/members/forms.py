from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class AuthForm(forms.Form):
    username = forms.CharField(label="Username",
                               max_length=100,
                               widget=forms.TextInput(attrs={"class ":'form-control',"placeholder":"Username"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class ":'form-control',"placeholder":"Password"}))
    username = forms.CharField(label="Username",
                               max_length=100,
                               widget=forms.TextInput(attrs={"class ": 'form-control', "placeholder": "Username"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class ": 'form-control', "placeholder": "Password"}))



class RegisterUserForm(UserCreationForm):
    email= forms.EmailField()
    first_name = forms.CharField(max_length=64)
    last_name = forms.CharField(max_length=64)

    class Meta:
        model = User
        fields = ("username",
                  'first_name',
                  'last_name',
                  'email',
                  'password1',
                  'password2')
