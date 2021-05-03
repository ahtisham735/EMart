from django.views import View
from .models import User,SellerDetail
from .utility_functions import isUserLogin
from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse,HttpResponseRedirect

def seller_center(request):
    user=isUserLogin(request,'seller')
    if user is None:
        if "usernameSeller" in request.session:
            return render(request,"Seller_Module/SellerSignUp.html",context={"username":request.session['usernameSeller'],"password":request.session['passwordSeller']})     
        else:
            return render(request,"Seller_Module/SellerSignUp.html")
    return render(request,"Seller_Module/Seller_base.html",context={"user":user})
def seller_detail(request):
    seller=isUserLogin(request,'seller')
    if request.method=="GET":
        if seller is None:
            return HttpResponseRedirect(reverse("Home_Module:seller_center"))
        return render(request,"Seller_Module/SellerDetail.html")
    if request.method=="POST":
        detail=SellerDetail.objects.create(user=seller)
        detail.shop=request.POST['shop']
        detail.cnic=request.POST['cnic']
        detail.phone=request.POST['phone']
        detail.account_no=request.POST['account']
        detail.address=request.POST['address']
        detail.save()
        return render(request,"Seller_Module/Seller_base.html")
def seller_logout(request):
    try:
        del request.session['seller']
        return HttpResponseRedirect(reverse("Home_Module:seller_center"))
    except KeyError:
        return HttpResponseRedirect(reverse("Home_Module:seller_center"))
def add_product(request):
    user=isUserLogin(request,'seller')
    if user is None:
        HttpResponseRedirect(reverse("Home_Module/seller_center"))
    return render(request,"Seller_Module/addproduct.html",context={"user":user})

def seller_detail_update(request):
    user=isUserLogin(request,'seller')
    detail=SellerDetail.objects.get(pk=user.id)
    if request.method=="GET":
        if user is None:
            return HttpResponseRedirect(reverse("Home_Module:seller_center"))     
        return render(request,"Seller_Module/SellerDetailUpdate.html",context={"detail":detail})
    if request.method=="POST":
        detail.shop=request.POST['shop']
        detail.cnic=request.POST['cnic']
        detail.phone=request.POST['phone']
        detail.account_no=request.POST['account']
        detail.address=request.POST['address']
        detail.save()
        return render(request,"Seller_Module/Seller_base.html",context={"user":user})
        
