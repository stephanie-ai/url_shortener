from django.urls import path
from .views import *
app_name = "url"
from . import views

urlpatterns = [
    path('', homepage, name='homepage'),
    path("url", urlShort, name="homepage")
    # path("u/<str:slugs>", views.urlRedirect, name="redirect")
]