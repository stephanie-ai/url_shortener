# from django.forms import ModelForm
from django import forms
from .models import Url

class EnterUrlForm(forms.ModelForm):

    class Meta:
        model = Url
        fields = [
            'url', 
            'shorten'
        ]
        widgets = {'url': forms.HiddenInput()}


#  <p>here is your url shortened {{}}</p>