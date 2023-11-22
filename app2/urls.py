from app2.views import *
from django.urls import path
app_name='pak'

urlpatterns=[
    path('pakistan/',
         pakistan ,name='pakistan'),
]