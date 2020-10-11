from django.shortcuts import render
from thecakeapp.models import Orderer, Order, Store, Baker, Review, Option, DetailedOption, Cake
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.

from django.http import HttpResponse

def signUp(request):
    if request.method == 'POST':
        if request.POST["password1"] == request.POST["confirm"]:
            bakerUser = Baker.objects.create()


            bakerUser.save()



def login(request):
    #person = Baker
    #person.email = request.GET('email')
    #person.password = request.GET('password')
    return render(request, 'baker/login_baker.html')

def idpw_search(request):
    return render(request, 'baker/idpw_search_baker.html')

def valid(request): #사업자번호확인 -> join
    return HttpResponse("Valid page!")

def manageStore(request):
    return render(request, 'baker/manageStore.html')

def manageCake(request):
    return render(request, 'baker/manageCake.html')

def manageOrder(request):
    return render(request, 'baker/manageOrder.html')

