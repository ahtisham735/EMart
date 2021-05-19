from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from Home_Module.utility_functions import isUserLogin
from django.contrib import auth,messages
from .models import Order,OrderDetails

# Create your views here.
def my_orders(request):
   user=isUserLogin(request,'user')
   if user is None:
      user=request.user
   if user is None and not user.is_authenticated:
      messages.error(request,"You must login first to access this page")
      return redirect(reverse("Home_Module:signup"))
   if request.method=="GET":
      orders=Order.objects.filter(user=user)
      return render(request,"order/orders.html",{"user":user,"orders":orders})

