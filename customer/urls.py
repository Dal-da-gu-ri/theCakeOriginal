from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.login_customer, name='login_customer'),
    path('main/', views.main_customer, name='main_customer'),
    path('mypage/', views.mypage, name='mypage_customer')
]
