from django.shortcuts import render
import pdb
from django.http import HttpResponse
import json
from .forms import Url

# Create your views here.
def homepage(request):
    return render(request, 'shorten_app/form.html')


def urlShort(request):
    if request.method == 'POST':
        form = Url(request.POST)
        pdb.set_trace()
        if form.is_valid():
            short = ''.join(random.choice(string.ascii_letters)
                           for x in range(10))
            url = form.cleaned_data["url"]
            new_url = UrlData(url=url, short=short)
            new_url.save()
            pdb.set_trace()
            request.user.urlshort.add(new_url)
            # return redirect('/')
            return render(request, 'shorten_app/form.html', {"url": new_url})
         
    else:
        form = Url()
    data = UrlData.objects.all()
    context = {
        'form': form,
        'data': data
    }
    return render(request, 'shorten_app/form.html', context)


# def urlRedirect(request, slugs):
#     data = UrlData.objects.get(slug=slugs)
#     return redirect(data.url)