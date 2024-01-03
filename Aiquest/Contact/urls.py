from django.urls import path
from .views import *

urlpatterns = [
    path('cn/', contact, name='contact'),
]