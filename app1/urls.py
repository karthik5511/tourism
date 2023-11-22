from app1.views import *
from django.urls import path

app_name='specific'

urlpatterns=[
    path('andra/',andra,name='andra'),
    path('tirumala/',tirumala,name='tirumala'),
    path('lepakshi/',lepakshi,name='lepakshi'),
]