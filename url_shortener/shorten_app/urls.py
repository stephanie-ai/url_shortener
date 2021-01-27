from django.urls import path
# from .views import *
from . import views
from .views import enter, shortpage

urlpatterns = [
    path("", enter, name='url-homepage'),
    path("short/", shortpage, name='url-shortpage')
    # path("short/", redirect, name="url-show"),
    # path("short/", enter, name='url-short')
    # path('short/<str:url>', siteredirect, name="siteredirect" )
]

