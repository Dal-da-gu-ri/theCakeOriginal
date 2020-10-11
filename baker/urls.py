from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.login, name='login_baker'),
    path('idpw_search/', views.idpw_search, name='idpw_search_baker'),
    path('manageStore/', views.manageStore, name='manageStore_baker'),
    path('manageCake/', views.manageCake, name='manageCake_baker'),
    path('manageOrder/', views.manageOrder, name='manageOrder_baker'),
]
