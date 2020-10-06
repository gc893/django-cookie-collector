# Cookie Collector
###### Python | Django | PostgreSQL
---
![](https://embed.widencdn.net/img/mccormick/u8pntu7ahp/2028x1141px/Vanilla_rich_chocolate_chip_cookies_004.jpg?crop=true&anchor=13,86&q=80&color=ffffffff&u=o2hyef)

* Created the app with: *django-admin startproject catcollector*

* Started main app with: *python3 manage.py startapp main_app*

* Included app by adding *'main_app'* to *INSTALLED APPS* on *settings.py*

* Added PostgreSQL DB information to *settings.py*

* Imported *models* from *django.db* to *models.py*

* Created a model by defining a function on *models.py*

* Migrated the model with *python3 manage.py makemigrations* and *python3 manage.py migrate*

* Created a file in *main_app* to define main_app routes

* Used these routes on the project by adding *path('', include('main_app.urls'))* to *urls.py*

* Imported path and the necessary views on the *urls.py* file

* Added *main_app's* routes to the *urlpatterns* list such as *(path('cookies/<<int:cookie_id>>/', views.cookies_detail, name='detail'))*

* Imported *render* to the *views.py* file

* Imported the model to the *views.py* file

* Defined the function to be called by the route to render a template *(return render(request, 'cookies/index.html', { 'cookies': cookies }))*

* Created HTML templates *({% block content %} {% endblock %} and {% extends 'base.html' %} {% block content %} {% endblock %})* 

* Added CSS file *({% load static %} and link rel="stylesheet" type="text/css" href="{% static 'css/style.css' %}")* 

![](https://i.imgur.com/2dmfF39.png)