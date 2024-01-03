from django.urls import path
from .views import Blog

urlpatterns = [
    path('bl/', Blog, name="blog"),
]