from django.shortcuts import render
from thecakeapp.models import Orderer, Order, Store, Baker, Review, Option, DetailedOption, Cake
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.

from django.http import HttpResponse

def signUp(request):
    if request.method == 'POST':
        #confirm이 아닌 re-password로 수정함. -예슬
        if request.POST["password_baker"] == request.POST["re-password_baker"]:
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

# 가게 관리
def enrollStore(request):
    return render(request, 'baker/enrollStore.html')
def opendays(request):
    return render(request, 'baker/opendays.html')
def storeReview(request):
    return render(request, 'baker/storeReview.html')

# 케이크 관리
def myCakes(request):
    return render(request, 'baker/myCakes.html')
def options(request):
    return render(request, 'baker/options.html')


def manageOrder(request):
    return render(request, 'baker/manageOrder.html')

def mypage(request):
    return render(request, 'baker/mypage_baker.html')
