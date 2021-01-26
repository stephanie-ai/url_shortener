# from django.forms import ModelForm
# from django import forms
from .models import UrlData
# class EnterUrlForm(forms.ModelForm):

#     class Meta:
#         model = Url
#         fields = [
#             'url', 
#             'shorten'
#         ]
#         widgets = {'url': forms.HiddenInput()}


#  <p>here is your url shortened {{}}</p>


from django import forms
class Url(forms.Form):
    url = forms.CharField(label="URL")