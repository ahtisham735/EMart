from django.views import View
from .forms import AddProductForm
from .models import User,SellerDetail,Products
from .utility_functions import isUserLogin
from django.shortcuts import render,redirect,reverse
from django.contrib import messages
from django.http import HttpResponse,HttpResponseRedirect

def seller_center(request):
    user=isUserLogin(request,'seller')
    if user is None:
        if "usernameSeller" in request.session:
            return render(request,"Seller_Module/SellerSignUp.html",context={"username":request.session['usernameSeller'],"password":request.session['passwordSeller']})     
        else:
            return render(request,"Seller_Module/SellerSignUp.html")
    productList=Products.objects.all().filter(sellerId=user)
    return render(request,"Seller_Module/Seller_base.html",context={"user":user,"products":productList})
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
        productList=Products.objects.all().filter(sellerId=seller)
        return render(request,"Seller_Module/Seller_base.html",context={"user":seller,"products":productList})
        #return render(request,"Seller_Module/Seller_base.html")
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
    if request.method=="GET":
        form=AddProductForm()
        return render(request,"Seller_Module/addproduct.html",context={"user":user,"form":form})
    else:
        form=AddProductForm(request.POST,request.FILES)
        if form.is_valid():
            product=form.save(commit=False)
            product.sellerId=user
            product.save()
            messages.success(request,"Product Added Successfully")
            return HttpResponseRedirect(reverse("Home_Module:seller_center"))
        else:
            messages.error(request,form.errors)
            return HttpResponseRedirect(reverse("Home_Module:seller_center"))

        

def seller_detail_update(request):
    user=isUserLogin(request,'seller')
    detail=SellerDetail.objects.get(user=user)
    if request.method=="GET":
        if user is None:
            return HttpResponseRedirect(reverse("Home_Module:seller_center"))     
        return render(request,"Seller_Module/SellerDetailUpdate.html",context={"detail":detail,"user":user})
    if request.method=="POST":
        detail.shop=request.POST['shop']
        detail.cnic=request.POST['cnic']
        detail.phone=request.POST['phone']
        detail.account_no=request.POST['account']
        detail.address=request.POST['address']
        detail.save()
        messages.success(request,"Updated")
        return HttpResponseRedirect(reverse("Home_Module:seller_center"))

def all_product(request):
    user=isUserLogin(request,'seller')
    productList=Products.objects.all().filter(sellerId=user)
    if user is None:
        HttpResponseRedirect(reverse("Home_Module/seller_center"))
    else:
        return render(request,"Seller_Module/AllProduct.html",context={"user":user,"products":productList})

def edit_product(request, pk):
    user=isUserLogin(request,'seller')
    if user is None:
        HttpResponseRedirect(reverse("Home_Module/seller_center"))
    prodct=Products.objects.get(id=pk) 
    if request.method=="GET":    
        form=AddProductForm(instance=prodct)
        return render(request,"Seller_Module/editproduct.html",context={"user":user,"usr":pk,"form":form}) 
        
    if request.method=="POST": 
        productList=Products.objects.all().filter(sellerId=user) 
        form=AddProductForm(request.POST,request.FILES,instance=prodct)
        if form.is_valid():
            prodct=form.save(commit=False)
            prodct.sellerId=user
            prodct.save()
            messages.success(request,"Product Updated Successfully")
            return render(request,"Seller_Module/Seller_base.html",context={"user":user,"products":productList})
            #return render(request,"Seller_Module/Seller_base.html",context={"user":user})
        else:
            messages.success(request," Product Not Updated")
        return render(request,"Seller_Module/Seller_base.html",context={"user":user,"products":productList})

def delete_product(request, pk):
    prodct=Products.objects.get(id=pk) 
    user=isUserLogin(request,'seller')
    productList=Products.objects.all().filter(sellerId=user) 
    if user is None:
        HttpResponseRedirect(reverse("Home_Module/seller_center"))
    if request.method=="POST":
        prodct.delete() 
        messages.success(request," Successfully Deleted")
        return render(request,"Seller_Module/Seller_base.html",context={"user":user,"products":productList})     
       # return render(request,"Seller_Module/Seller_base.html",context={"user":user})
    return render(request,"Seller_Module/deleteProduct.html",context={"user":user,"item":prodct})
