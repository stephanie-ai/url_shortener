from django.urls import path
# from .views import *
from . import views
from .views import enter, redirect

urlpatterns = [
    path("", enter, name='url-homepage'),
    # path("short/", redirect, name="url-show"),
    path("short/", redirect, name='redirect')
]

