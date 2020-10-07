# Cookie Collector
###### Python | Django | PostgreSQL
---
![](https://embed.widencdn.net/img/mccormick/u8pntu7ahp/2028x1141px/Vanilla_rich_chocolate_chip_cookies_004.jpg?crop=true&anchor=13,86&q=80&color=ffffffff&u=o2hyef)

## Day 1: Rendering Data

* Created the app with: __*django-admin startproject catcollector*__

* Started main app with: __*python3 manage.py startapp main_app*__

* Included app by adding __*'main_app'*__ to __*INSTALLED APPS*__ on __*settings.py*__

* Added PostgreSQL DB information to __*settings.py*__

* Imported __*models*__ from __*django.db*__ to __*models.py*__

* Created a model by defining a function on __*models.py*__

* Migrated the model with __*python3 manage.py makemigrations*__ and __*python3 manage.py migrate*__

* Created a file in __*main_app*__ to define main_app routes

* Used these routes on the project by adding __*path('', include('main_app.urls'))*__ to __*urls.py*__

* Imported path and the necessary views on the __*urls.py*__ file

* Added __*main_app's*__ routes to the __*urlpatterns*__ list such as __*(path('cookies/<<int:cookie_id>>/', views.cookies_detail, name='detail'))*__

* Imported __*render*__ to the __*views.py*__ file

* Imported the model to the __*views.py*__ file

* Defined the function to be called by the route to render a template __*(return render(request, 'cookies/index.html', { 'cookies': cookies }))*__

* Created HTML templates __*({% block content %} {% endblock %} and {% extends 'base.html' %} {% block content %} {% endblock %})*__

* Added CSS file __*({% load static %} and link rel="stylesheet" type="text/css" href="{% static 'css/style.css' %}")*__

## Day 2: CRUD Opeations and CBVs

*  Imported __*ListView, CreateView and UpdateView and DeleteView*__ from __*django.views.generic.edit*__

* Refactored index view function to CBV with:
    ``` 
    class CookieList(ListView):
        model = Cookie
        template_name = 'cookies/index.html'
        context_object_name = 'cookies'
    ```
    &
    ```
    path('cookies/', CookieList.as_view(), name='cookies_index')
    ```

* Imported the class in the __*urls.py*__ file __*(from .views import CookieList
)*__

* Added create, update and delete links, classes and routes __*(also created main_app directory on Templates to add a form and confirm template).*__

![](https://i.imgur.com/2dmfF39.png)