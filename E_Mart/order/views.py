from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from Home_Module.utility_functions import isUserLogin,permission_check
from django.shortcuts import render,redirect,reverse
from .models import Order,OrderDetails
from django.contrib import auth,messages
# Create your views here.
def my_orders(request):
   user=permission_check(request)
   if user is None:
      return redirect(reverse("Home_Module:signup"))
   if request.method=="GET":
      orders=Order.objects.filter(user=user)
      return render(request,"order/orders.html",{"user":user,"orders":orders})
def order_details(request,id):
   user=permission_check(request)
   if user is None:
      return redirect(reverse("Home_Module:signup"))
   if request.method=="GET":
      order_details=OrderDetails.objects.filter(order=id)
      return render(request,"order/order_details.html",{"user":user,"orders_details":order_details})
    
def order_delivered(request,id):
   user=permission_check(request)
   if user is None:
      return redirect(reverse("Home_Module:signup"))
   if request.method=="GET":
      try:
         order=Order.objects.get(id=id)
         order.is_delivered=True
         order.save()
         messages.info(request,"You have confirmed that you have received the order.Hope you like it")
         return redirect(reverse("order:my_orders"))
      except Order.DoesNotExist:
         messages.warning(request,"This order doesn't exist.Perhaps it has been deleted")
         return redirect(reverse("order:my_orders"))
         




