from Home_Module.models import User,Cart
from django.shortcuts import render,redirect,HttpResponse,reverse
from Home_Module.utility_functions import isUserLogin,permission_check,cart_lenght
from django.contrib import messages
from .models import ShippingDetail
from .utility_functions import is_detail_exist
# Create your views here.
def shipping_detail(request,chk=''):
   
    user=permission_check(request)
    if user is None:
        return redirect(reverse("Home_Module:signup"))
    details=is_detail_exist(user)
    cart=cart_lenght(user)
    context={"user":user,"notify":cart,'chk':chk}
    if request.method=="GET":
        if details is None:
            if len(chk)!=0:
                context["button"]="Save Shipping Details"
            else:
                context["button"]="Place Order"
            return render(request,"shipping/shippingDetail.html",context=context)
        Name=details.name
        fname=Name.split(' ')[0]
        lname=Name.split(' ')[1]
        context["fname"]=fname
        context["lname"]=lname
        context['details']=details
        if len(chk)!=0:
            context['button']="Update Shipping Details" 
        else:
            context["button"]="Place Order"
        return render(request,"shipping/shippingDetail.html",context=context)  
    chk=request.POST['chk']
    if details is None:
        details=ShippingDetail.objects.create(user=user)
        if len(chk)!=0:
            messages.success(request,"Your shipping details have been saved.You can update your details any time")
    else:
        if len(chk)!=0:
            messages.success(request,"Your shipping details have been updated")
        else:
            messages.success(request,"Your order has been placed.It will be delivered in 7 working days.")
    details.name=request.POST['fname'] + ' ' + request.POST['lname']
    details.address=request.POST['address']
    details.city=request.POST['city']
    details.country=request.POST['country']
    details.zip_code=request.POST['zip']
    details.email=request.POST['email']
    details.contact=request.POST['phone']
    details.save()
    if len(chk)!=0:
        return redirect(reverse("Home_Module:home"))
    else:
        return redirect(reverse("Home_Module:checkout"))




