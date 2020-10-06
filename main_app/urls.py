from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cookies/', views.cookies_index, name='index'),
    path('cookies/<int:cookie_id>/', views.cookies_detail, name='detail'),
]