from django.views import View
from .models import User,SellerDetail
from .utility_functions import isUserLogin
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect

def seller_center(request):
    return render(request,"Seller_Module/SellerSignUp.html")
def seller_detail(request):
    seller=isUserLogin(request,'seller')
    if request.method=="GET":
        if seller is None:
            return render(request,"Home_Module/SellerSignup.html")
        return render(request,"Seller_Module/SellerDetail.html")
    if request.method=="POST":
        detail=SellerDetail.objects.create(user=seller)
        detail.shop=request.POST['shop']
        detail.cnic=request.POST['cnic']
        detail.phone=request.POST['phone']
        detail.account_no=request.POST['account']
        detail.address=request.POST['address']
        detail.save()
        return render(request,"Seller_Module/Home.html")


        
   