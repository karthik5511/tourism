from app2.views import *
from django.urls import path

app_name='karthik'

urlpatterns=[
    path('arakuvally/',arakuvally,name='arakuvally'),
    path('amaravathi',amaravathi,name='amaravathi'),
]