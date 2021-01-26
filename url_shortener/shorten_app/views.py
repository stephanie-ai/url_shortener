from django.shortcuts import render
from django.http import HttpResponse
import json
from .forms import EnterUrlForm

# Create your views here.
def homepage(request):
    return render(request, 'shorten_app/form.html')

def receivedUrl(request, EnterUrlForm):
    if req.method == 'POST':
        form = EnterUrlForm(req.POST)
        # if form.is_valid():
        #     form.save()
        url = form.cleaned_data.get('url')
        messages.success(req, f'you want to shorten, {url}!')
        return render(request, 'shorten_app/form.html', {'url': url})

