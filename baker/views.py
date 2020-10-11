from django.shortcuts import render
from thecakeapp.models import Orderer, Order, Store, Baker, Review, Option, DetailedOption, Cake
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("Index page!")

#def signUp(request):
#    if request.method == "POST":
#        if request.POST["password1"] == request.POST["password2"]:

def login(request):
    person = Baker
    person.email = request.GET('email')
    person.password = request.GET('password')
    return render(request, 'baker/login_baker.html')

def valid(request): #사업자번호확인 -> join
    return HttpResponse("Valid page!")

def manageStore(request):
    return HttpResponse("manageStore page")

def manageCake(request):
    return HttpResponse("manageCake page")

def order(request):
    return HttpResponse("Order page!")

