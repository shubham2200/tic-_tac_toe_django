from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('',  home  ,  name='home'),
    path('room/' , room , name='room'),
    path('check_name/' , check_room , name='check_name')
   

   
]
