from django.shortcuts import render,redirect,HttpResponse
from Home_Module.utility_functions import isUserLogin
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
    name=request.POST['fname']
    address=request.POST['address']
    city=request.POST['city']
    country=request.POST['country']
    zip_code=request.POST['zip']
    email=request.POST['email']
    phone=request.POST['phone']
    detail=ShippingDetail.objects.create(user=user,name=name,address=address,city=city,zip_code=zip_code,country=country,email=email,contact=phone)
    detail.save()
    return redirect(reverse("Home_Module:checkout"))