from django.urls import path
from .views import *

urlpatterns = [
    path('ab/', about, name='about'),
]