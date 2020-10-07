from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Cookie
from .forms import BatchForm

# Create your views here.

from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cookies_index(request):
    cookies = Cookie.objects.all()
    return render(request, 'cookies/index.html', {'cookies': cookies})

def cookies_detail(request, cookie_id):
  cookie = Cookie.objects.get(id=cookie_id)
  batch_form = BatchForm()
  return render(request, 'cookies/detail.html', {
    'cookie': cookie, 'batch_form': batch_form
  })

class CookieList(ListView):
    model = Cookie
    template_name = 'cookies/index.html'
    # queryset = Cookie.objects.all()
    context_object_name = 'cookies'

class CookieCreate(CreateView):
  model = Cookie
  fields = '__all__'

class CookieUpdate(UpdateView):
  model = Cookie
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = '__all__'

class CookieDelete(DeleteView):
  model = Cookie
  success_url = '/cookies/'

def add_batch(request, cookie_id):
  # create a ModelForm instance using the data in request.POST
  form = BatchForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_batch = form.save(commit=False)
    new_batch.cookie_id = cookie_id
    new_batch.save()
  return redirect('detail', cookie_id=cookie_id)