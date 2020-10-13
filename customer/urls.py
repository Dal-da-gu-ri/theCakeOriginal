from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.login, name='login_customer'),
    path('signUp/', views.mypage, name='signUp_customer'),
    path('main/', views.main, name='main_customer'),
    path('mypage/', views.mypage, name='mypage_customer'),
    path('orderlist/', views.orderlist, name='orderlist_customer')
]
