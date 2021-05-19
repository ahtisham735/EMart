from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from Home_Module.utility_functions import isUserLogin,permission_check
from django.shortcuts import render,redirect,reverse
from .models import Order,OrderDetails

# Create your views here.
def my_orders(request):
   user=permission_check(request)
   if user is None:
      return redirect(reverse("Home_Module:signup"))
   if request.method=="GET":
      orders=Order.objects.filter(user=user)
      return render(request,"order/orders.html",{"user":user,"orders":orders})
def order_details(request):
   pass



