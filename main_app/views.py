from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Cookie, Ingredient
from .forms import BatchForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def cookies_index(request):
    cookies = Cookie.objects.all()
    return render(request, 'cookies/index.html', {'cookies': cookies})

@login_required
def cookies_detail(request, cookie_id):
  cookie = Cookie.objects.get(id=cookie_id)
  ingredients_not_added = Ingredient.objects.exclude(id__in = cookie.ingredients.all().values_list('id'))
  batch_form = BatchForm()
  return render(request, 'cookies/detail.html', {
    'cookie': cookie, 'batch_form': batch_form, 'ingredients': ingredients_not_added
  })

class CookieList(LoginRequiredMixin, ListView):
  model = Cookie
  template_name = 'cookies/index.html'
  context_object_name = 'cookies'

  def get_queryset(self):
    queryset = super().get_queryset()
    return queryset.filter(user=self.request.user)

class CookieCreate(LoginRequiredMixin, CreateView):
  model = Cookie
  fields = ['name', 'main_flavor', 'description', 'prep_time']

  def form_valid(self, form):
    # Assign the logged in user (self.request.user)
    form.instance.user = self.request.user  # form.instance is the cat
    # Let the CreateView do its job as usual
    return super().form_valid(form)

class CookieUpdate(LoginRequiredMixin, UpdateView):
  model = Cookie
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['name', 'main_flavor', 'description', 'prep_time', 'image_url']

class CookieDelete(LoginRequiredMixin, DeleteView):
  model = Cookie
  success_url = '/cookies/'

@login_required
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

@login_required
def assoc_ing(request, cookie_id, ingredient_id):
  Cookie.objects.get(id=cookie_id).ingredients.add(ingredient_id)
  return redirect('detail', cookie_id=cookie_id)

@login_required
def remove_ing(request, cookie_id, ingredient_id):
  Cookie.objects.get(id=cookie_id).ingredients.remove(ingredient_id)
  return redirect('detail', cookie_id=cookie_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)