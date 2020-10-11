from django.shortcuts import render
from thecakeapp.models import Orderer, Order, Store, Baker, Review, Option, DetailedOption, Cake

# Create your views here.

def login_customer(request):
    return render(request, 'customer/login_customer.html')

def signUp(request):
    if request.method == 'POST':
        if request.POST["password1"] == request.POST["confirm"]:
            customerUser = Orderer.objects.create()


            customerUser.save()


# login에 성공하면 main_customer.html으로 이동!
def main_customer(request):
    return render(request, 'customer/main_customer.html')

def mypage(request):
    return render(request, 'customer/mypage.html')