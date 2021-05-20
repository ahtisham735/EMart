from Home_Module.models import User,Cart
from django.shortcuts import render,redirect,HttpResponse
from Home_Module.utility_functions import isUserLogin
from django.contrib import messages
from .models import ShippingDetail
# Create your views here.
def shipping_detail(request):
    user=isUserLogin(request,'user')
    if user is None:
        user=request.user
    if request.method=="GET":
        if user is None and not user.is_authenticated:
            return redirect(reverse("Home_Module:signup"))
        return render(request,"shipping/shippingDetail.html",{"user":user})
    
    name=request.POST['fname'] + ' ' + request.POST['lname']
    address=request.POST['address']
    city=request.POST['city']
    country=request.POST['country']
    zip_code=request.POST['zip']
    email=request.POST['email']
    phone=request.POST['phone']
    detail=ShippingDetail.objects.create(user=user,name=name,address=address,city=city,zip_code=zip_code,country=country,email=email,contact=phone)
    detail.save()
    return redirect(reverse("Home_Module:checkout"))


def update_shipping_detail(request):
    user=isUserLogin(request,'user')
    try:
        details=ShippingDetail.objects.get(user=user)
        if request.method=="GET":
            if user is None and not user.is_authenticated:
                return redirect(reverse("Home_Module:signup"))
            Name=details.name
            fname=Name.split(' ')[0]
            lname=Name.split(' ')[1]
            context={"details":details,"user":user,"fname":fname,"lname":lname}
            return render(request,"shipping/UpdateshippingDetail.html",context=context)
        if request.method=="POST":
       
            details.name=request.POST['fname'] + ' ' + request.POST['lname']
            details.email=request.POST['email']
            details.address=request.POST['address']
            details.country=request.POST['country']
            details.city=request.POST['city']
            details.contact=request.POST['phone']
            details.zip_code=request.POST['zip']
            details.save()
            cart=Cart.objects.filter(user=user)
            context={"user":user,"notify":len(cart)}
            messages.success(request,"Updated")
            return render(request,"Home_Module/Home.html",context=context)
    except ShippingDetail.DoesNotExist:
        messages.error(request,"You have not any shipping details.Please add details")
        return render(request,"shipping/shippingDetail.html")
