from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("Index page!")

def login(request):
    return render(request, 'baker/login_baker.html')

def valid(request): #사업자번호확인 -> join
    return HttpResponse("Valid page!")

def manageStore(request):
    return HttpResponse("manageStore page")

def manageCake(request):
    return HttpResponse("manageCake page")

def order(request):
    return HttpResponse("Order page!")

