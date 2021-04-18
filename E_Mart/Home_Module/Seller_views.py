from django.views import View
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect

def seller_center(request):
    return render(request,"Seller_Module/SellerSignUp.html")
def seller_login(request):
    if request.method=="GET":
        return render(request,"Seller_Module/SellerSignUp.html")
   