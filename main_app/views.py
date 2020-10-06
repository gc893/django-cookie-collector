from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

class Cookie:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, main_flavor, description, prep_time):
    self.name = name
    self.main_flavor = main_flavor
    self.description = description
    self.prep_time = prep_time

cookies = [
    Cookie('Chocolate-Chip Cookies', 'Chocolate', 'Incredibly soft chocolate chip cookie', 1.5),
    Cookie('Almond Extract Cookies', 'Almonds', 'Crunchy, flavorful almond cookie', 2),
    Cookie('Sweet Raisin Cookies', 'Raisins', 'Low calorie raisin cookie', 1)
]

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cookies_index(request):
    return render(request, 'cookies/index.html', {'cookies': cookies})