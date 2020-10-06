from django.shortcuts import render
from .models import Cookie

# Create your views here.

from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cookies_index(request):
    cookies = Cookie.objects.all()
    return render(request, 'cookies/index.html', {'cookies': cookies})