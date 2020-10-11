from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.login, name='login_baker'),
    path('idpw_search/', views.idpw_search, name='idpw_search_baker'),
    path('signUp/', views.signUp, name='signUp_baker'),

    path('manageStore/enrollStore', views.enrollStore, name='enrollStore_baker'),
    path('manageStore/opendays', views.opendays, name='opendays_baker'),
    path('manageStore/storeReview', views.storeReview, name='storeReview_baker'),


    path('manageCake/', views.manageCake, name='manageCake_baker'),
    path('manageOrder/', views.manageOrder, name='manageOrder_baker'),
    path('mypage/', views.mypage, name='mypage_baker')
]
