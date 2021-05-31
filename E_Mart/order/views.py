from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from Home_Module.utility_functions import isUserLogin,permission_check
from django.shortcuts import render,redirect,reverse
from .models import Order,OrderDetails
from Home_Module.models import Products,Cart
from django.contrib import auth,messages
from django.db.models import Q
# Create your views here.
def my_orders(request):
   user=permission_check(request)
   if user is None:
      return redirect(reverse("Home_Module:signup"))
   if request.method=="GET":
      orders=Order.objects.filter(user=user).order_by('-date')
      cart=Cart.objects.filter(user=user)  #cart-notification
      return render(request,"order/orders.html",{"user":user,"orders":orders,"notify":len(cart)})
def order_details(request,id):
   user=permission_check(request)
   if user is None:
      return redirect(reverse("Home_Module:signup"))
   if request.method=="GET":
      cart=Cart.objects.filter(user=user)   #cart-notification
      order_details=OrderDetails.objects.filter(order=id)
      return render(request,"order/order_details.html",{"user":user,"orders_details":order_details,"notify":len(cart)})
    
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
         
def seller_orders(request):
   user=isUserLogin(request,'seller')
   if user is None:
      return redirect(reverse("Home_Module:seller_center"))
   if request.method=="GET":
      p=Products.objects.filter(sellerId=user)
      ordersDetails=OrderDetails.objects.filter(products__in=p)
      ids=[]
      confirmation={}
      for order in ordersDetails:
         ids.append(order.order.id)
         if order.is_shipped:
            confirmation[order.order.id]=True

      orders=Order.objects.filter(pk__in=ids).order_by('-date')
      return render(request,"order/seller_orders.html",context={"user":user,"orders":orders,"confirmation":confirmation})
def seller_orders_details(request,id):
   user=isUserLogin(request,'seller')
   if user is None:
      return redirect(reverse("Home_Module:seller_center"))
   if request.method=="GET":
      p=Products.objects.filter(sellerId=user)
      order_details=OrderDetails.objects.filter(Q(products__in=p),Q(order=id) )
      return render(request,"order/order_details_seller.html",{"user":user,"orders_details":order_details})
def seller_confirmation(request,id):
   user =isUserLogin(request,'seller')
   if user is None:
      return redirect(reverse("Home_Module:seller_center"))
   if request.method=="GET":
      p=Products.objects.filter(sellerId=user)
      order_details=OrderDetails.objects.filter(order=id)
      order_details_for_this_user=order_details.filter(products__in=p).update(is_shipped=True)
      count=order_details.filter(is_shipped=False).count()
      if count==0:
         try:
            Order.objects.filter(pk=id).update(is_shipped=True)
         except Order.DoesNotExist:
            messages.warning(request,"This order doesn't exist.Perhaps it has been deleted")
      return redirect(reverse("order:seller_orders"))


