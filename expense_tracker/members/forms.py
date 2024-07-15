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

    class Meta:
        model = User
        fields = (
            "username",
            'first_name',
            'last_name',
            'email',
        )

        labels = {
            "username":"",
            "first_name":"",
            "last_name":"",
            "email":"",
            "password1":"password"
        }
        widgets = {
            "username":forms.TextInput(attrs={"class":'form-control',"placeholder":"Username"}),
            "first_name":forms.TextInput(attrs={"class":'form-control',"placeholder":"First Name"}),
            "last_name":forms.TextInput(attrs={"class":'form-control',"placeholder":"Last Name"}),
            "email":forms.EmailInput(attrs={"class":'form-control',"placeholder":"Email"}),
        }

    def __init__(self,*args, **kwargs):
        super(RegisterUserForm, self).__init__(*args,**kwargs)

        self.fields['username'].widget.attrs['class'] = "form-control"

        self.fields['password1'].widget.attrs['class'] = "form-control"
        self.fields['password1'].widget.attrs['placeholder'] = "Password"
        self.fields['password1'].label = ""

        self.fields['password2'].widget.attrs['class'] = "form-control"
        self.fields['password2'].widget.attrs['placeholder'] = "Password Confirmation"
        self.fields['password2'].label = ""
