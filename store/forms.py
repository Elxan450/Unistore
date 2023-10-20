from django import forms
from .models import ProductReview

class ProductReviewForm(forms.ModelForm):

    class Meta:
        model = ProductReview
        fields = (
            "review",
        )

        widgets = {
            'review' : forms.Textarea(attrs={
                'class' : 'form-control',
                'placeholder' : 'Type here',
                'required':'',
                'rows':'5'
            }),            
        }