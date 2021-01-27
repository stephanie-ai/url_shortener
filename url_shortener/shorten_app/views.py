from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
import json
import random, string

from .forms import EnterUrlForm
from .models import Url

# Create your views here.
# def enter(request):
#     if request.method == 'POST':
#         url = EnterUrlForm(request.POST)
#         if url.is_valid():
#             url_id = url.save().id
#             return redirect("url-show", url_id=url_id)
#     else:
#         form = EnterUrlForm()
#     data = {'form': form }
#     return render(request, 'shorten_app/form.html', data)
    # return render(request, 'shorten_app/form.html')


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



# users enter a url
# def enter(request):
#     if request.method == 'POST':
#         url = EnterUrlForm(request.POST)
#         if url.is_valid():
#             url_id = url.save().id
#             return redirect("url-show", url_id=url_id)
#     else:
#         form = EnterUrlForm()
#     data = {'form': form }
#     return render(request, 'shorten_app/form.html', data)


# show the new shortened url
# def show(request, url_id):
#     url = get_object_or_404(Url, pk=url_id)
#     if request.method == "POST":
#         form = EnterUrlForm(request.POST)
#         if form.is_valid():
#             url.save()
#             return redirect('url-show', url_id=url_id)
#     else:
#         form = EnterUrlForm(initial={'url'})
#     data = {
#         'url': url,
#         'form': form
#     }
#     return render(request, 'shorten_app/newUrl.html', data)


# def urlShort(request):
#     if request.method == 'POST':
#         form = Url(request.POST)
#         pdb.set_trace()
#         if form.is_valid():
#             short = ''.join(random.choice(string.ascii_letters)
#                            for x in range(10))
#             url = form.cleaned_data["url"]
#             new_url = UrlData(url=url, short=short)
#             new_url.save()
#             pdb.set_trace()
#             request.user.urlshort.add(new_url)
#             return redirect("url-short", url_id=url_id)
#             return render(request, 'shorten_app/newUrl.html', {"url": new_url})
         
#     else:
#         form = Url()
#     data = UrlData.objects.all()
#     context = {
#         'form': form,
#         'data': data
#     }
#     return render(request, 'shorten_app/form.html', context)

