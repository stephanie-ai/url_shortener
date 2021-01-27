from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
import json
import random, string

from .forms import EnterUrlForm
from .models import Url


def redirect(request, url):
    current_obj = Url.objects.filter(short_url=url)
    if len(current_obj) == 0:
        return render(request, 'Error here')
    context = {'obj':current_obj[0]}
    return render(request, 'redirect.html', context)


def enter(request):
    if request.method == 'POST':
        form = EnterUrlForm(request.POST)
        if form.is_valid():
            original_website = form.cleaned_data['original_url']
            random_chars_list = list(string.ascii_letters)
            random_chars=''
            for i in range(6):
                random_chars += random.choice(random_chars_list)
            while len(Url.objects.filter(shorten=random_chars)) != 0:
                for i in range(6):
                    random_chars += random.choice(random_chars_list)
            s = Url(original_url=original_website, shorten=random_chars)
            s.save()
            return render(request, 'shorten_app/newUrl.html', {'chars':random_chars})
    
    else:
        form = EnterUrlForm()
    context = {'form': form}
    return render(request, 'shorten_app/form.html', context)
