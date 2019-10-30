from django.contrib import admin
from django.urls import path
from .views import HomePage,Enc
urlpatterns = [
    path('home/',HomePage,name='home-page'),
    path('encrypt/',Enc,name='encrypt'),
    #path('en/',Enc),
]
