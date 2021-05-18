from django.shortcuts import render,redirect
from Home_Module.utility_functions import isUserLogin

# Create your views here.
def shipping_detail(request):
    user=isUserLogin(request,'user')
    if user is None:
        user=request.user
    if request.method=="GET":
        if user is None and not user.is_authenticated:
            return redirect(reverse("Home_Module:signup"))
        return render(request,"shipping/shippingDetail.html",{"user":user})