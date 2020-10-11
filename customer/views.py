from django.shortcuts import render

# Create your views here.

def login_customer(request):
    return render(request, 'customer/login_customer.html')