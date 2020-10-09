from django.urls import path
from main_app.views import CookieList
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cookies/', CookieList.as_view(), name='index'),
    path('cookies/<int:cookie_id>/', views.cookies_detail, name='detail'),
    path('cookies/create/', views.CookieCreate.as_view(), name='cookies_create'),
    path('cookies/<int:pk>/update/', views.CookieUpdate.as_view(), name='cookies_update'),
    path('cookies/<int:pk>/delete/', views.CookieDelete.as_view(), name='cookies_delete'),
    path('cookies/<int:cookie_id>/add_batch/', views.add_batch, name='add_batch'),
    path('cookies/<int:cookie_id>/assoc_ing/<int:ingredient_id>/', views.assoc_ing, name='assoc_ing'),
    path('cookies/<int:cookie_id>/remove_ing/<int:ingredient_id>/', views.remove_ing, name='remove_ing'),
    path('accounts/signup/', views.signup, name='signup'),
]