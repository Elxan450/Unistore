from django import forms
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput, FileInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
User = get_user_model()

class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "image"]

        widgets = {
                'first_name': TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'First name',
                    'required':''
                }),

                'last_name': TextInput(attrs={
                    'class': "form-control",
                    'placeholder': 'Last name',
                    'required':''
                }),

                'username': TextInput(attrs={
                    'class': "form-control",
                    'placeholder': 'Username',
                    'required':''
                }),

                'email': EmailInput(attrs={
                    'class': "form-control", 
                    'placeholder': 'Email',
                    'required':'',
                }),   

                'image': FileInput(attrs={
                    'class' : "form-control", 
                    'title' : "Choose a profile photo",
                    'name' : "Profile Photo",
                    'id' : "InputField"
                }),        
            }   
            