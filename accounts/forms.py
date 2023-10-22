from django import forms
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput, FileInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.forms import AuthenticationForm, UsernameField

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(widget=forms.TextInput(
        attrs={'class': "form-control",
                    'placeholder': 'Username',
                    'required':''                    
                    }))
    
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Password',
            'required':'',
        }
))

class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].widget.attrs['required'] = ''
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm password'
        self.fields['password2'].widget.attrs['required'] = ''

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "image", 'password1', 'password2']

    

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

                'password':TextInput(attrs={'class':'form-control'}),
                'password2':TextInput(attrs={'class':'form-control'}),
            }   
            