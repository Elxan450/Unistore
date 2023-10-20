from django import forms
from .models import Checkout

class CheckoutForm(forms.ModelForm):

    class Meta:
        model = Checkout
        fields = (
            "phone", 
            "street", 
            "building", 
            "email",
            "zip",
            "payment"
        )

        widgets = {
            'phone' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : '',
                'required':'',
                'name':'phone'
            }),     

            'email' : forms.EmailInput(attrs={
                'class' : 'form-control',
                'type': 'email',
                'placeholder' : '',
                'required':'',
                'name':'email'
            }),     

            'street' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : '',
                'required':'',
                'name':'street'
            }),     

            'building' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : '',
                'required':'',
                'name':'building'
            }),     

            'zip' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : '',
                'required':'',
                'name':'zip'
            }),     

            'payment' : forms.TextInput(attrs={
                'class' : 'form-control select',
                'placeholder' : '',
                'required':'',
                'name':'payment',
                'id':'payment',
                'value':'Cash on Delivery'
            }),     
        }