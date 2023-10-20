from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = (
            "message", 
            "email"
        )

        widgets = {
            'message' : forms.Textarea(attrs={
                'class' : 'form-control',
                'placeholder' : 'Message',
                'required':'',
                'rows':'5'
            }),            
            'email' : forms.EmailInput(attrs={
                'class' : 'form-control',
                'type' : 'email',
                'placeholder' : 'E-mail',
                'required' : ''
            })
        }