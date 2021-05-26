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
    return render(request,"Seller_Module/AllProduct.html",context={"user":user,"products":productList})
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
        return render(request,"Seller_Module/AllProduct.html",context={"user":seller,"products":productList})
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
        return render(request,"Seller_Module/addproduct.html",context={"user":user,"form":form,"heading":"Add a new Product","button":"Add Product"})
    if not 'image1' in request.FILES:
        messages.error(request,"image1 is a requried filed")
        return render(request,"Seller_Module/addproduct.html",context={"user":user,"form":form,"heading":"Add a new Product","button":"Add Product"})
    if not 'image2' in request.FILES:
        messages.error(request,"image2 is a requried filed")
        return render(request,"Seller_Module/addproduct.html",context={"user":user,"form":form,"heading":"Add a new Product","button":"Add Product"})
    if not 'image3' in request.FILES:
        messages.error(request,"image3 is a requried filed")
        return render(request,"Seller_Module/addproduct.html",context={"user":user,"form":form,"heading":"Add a new Product","button":"Add Product"})
    if not 'image4' in request.FILES:
        messages.error(request,"image4 is a requried filed")
        return render(request,"Seller_Module/addproduct.html",context={"user":user,"form":form,"heading":"Add a new Product","button":"Add Product"})   
    form=AddProductForm(request.POST,request.FILES)
    form.instance.sellerId=user
    print(form.instance)
    if form.is_valid():
        form.save()
        messages.success(request,"Product Added Successfully")
        return HttpResponseRedirect(reverse("Home_Module:seller_center"))
    else:
        messages.error(request,form.errors)
        return render(request,"Seller_Module/addproduct.html",context={"user":user,"form":form,"heading":"Add a new Product","button":"Add Product"})   

        

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

def edit_product(request, pk):
    user=isUserLogin(request,'seller')
    if user is None:
        HttpResponseRedirect(reverse("Home_Module/seller_center"))
    try:
        prodct=Products.objects.get(id=pk) 
        if request.method=="GET":    
            form=AddProductForm(instance=prodct)
            return render(request,"Seller_Module/addproduct.html",context={"user":user,"form":form,"heading":"Update product","button":"update","pk":pk}) 
            
        if request.method=="POST":      
            form=AddProductForm(request.POST,request.FILES,instance=prodct)
            print(form.instance.image1.path)
            if form.is_valid():
                prodct=form.save(commit=False)
                prodct.sellerId=user
                prodct.save()
                messages.success(request,"Product Updated Successfully")
                return redirect(reverse("Home_Module:seller_center"))
                #return render(request,"Seller_Module/Seller_base.html",context={"user":user})
            else:
                messages.success(request,form.errors)
            return redirect(reverse("Home_Module:edit_product"))
    except Products.DoesNotExist:
        messages.error(request,"Product Does not Exist")
        return redirect(reverse("Home_Module:seller_center"))


def delete_product(request, pk):
    try:
        prodct=Products.objects.get(id=pk) 
        user=isUserLogin(request,'seller')
        if user is None:
            return HttpResponseRedirect(reverse("Home_Module:seller_center"))
        if request.method=="GET":
            return render(request,"Seller_Module/deleteProduct.html",{"user":user,"item":prodct})
        prodct.delete() 
        messages.success(request," Successfully Deleted")
        return redirect(reverse("Home_Module:seller_center"))
    except Products.DoesNotExist:
            messages.error(request,"Product Does not Exist")
            return redirect(reverse("Home_Module:seller_center"))


