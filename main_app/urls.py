from django.urls import path
from main_app.views import CookieList
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cookies/', CookieList.as_view(), name='index'),
    path('cookies/<int:cookie_id>/', views.cookies_detail, name='detail'),
]