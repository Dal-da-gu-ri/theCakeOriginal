from django.shortcuts import render

# Create your views here.

def login_customer(request):
    return render(request, 'customer/login_customer.html')

# login에 성공하면 main_customer.html으로 이동!
def main_customer(request):
    return render(request, 'customer/main_customer.html')