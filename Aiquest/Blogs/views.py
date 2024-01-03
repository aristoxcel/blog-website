from django.shortcuts import render
from .models import Blogging

# Create your views here.
def Blog(request):
    blg = Blogging.objects.all()
    return render(request, 'blog/blog.html', {'bloger': blg})
