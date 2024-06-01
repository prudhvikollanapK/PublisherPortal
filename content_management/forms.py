from django import forms
from .models import ContentOffering

class ContentOfferingForm(forms.ModelForm):
    class Meta:
        model = ContentOffering
        fields = ['title', 'description', 'price', 'document']
