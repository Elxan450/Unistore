from django import forms
from .models import BlogReview

class BlogReviewForm(forms.ModelForm):

    class Meta:
        model = BlogReview
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