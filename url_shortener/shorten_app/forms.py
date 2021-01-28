from django import forms
from .models import Url

class EnterUrlForm(forms.ModelForm):
    class Meta:
        model = Url
        fields = ['original_url']

        widgets = {
            'original_url': forms.TextInput(attrs={'class': 'form-control'})
        }