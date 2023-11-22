from app1.views import *
from django.urls import path
app_name='ind'

urlpatterns=[
    path('india/',india,name='india'),
]