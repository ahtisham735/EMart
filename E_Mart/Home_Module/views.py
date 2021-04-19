from django.views import View
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from django import forms
from django.urls import reverse
from django.contrib import auth,messages
from django.conf import settings
from django.contrib.auth import update_session_auth_hash
from Home_Module.models import User,SellerDetail
from .email_handler import token_generator,send_link
from django.utils.encoding import force_bytes,force_text,DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from .Serializer import CustomerSerializer
from .utility_functions import isUserLogin
# Create your views here.

@csrf_exempt
def cust_api(request,name='',email=''):
    if request.method=="GET":
        if len(name)!=0 or len(email)!=0:
            try:
                if len(email)==0:
                    cust=User.objects.get(username=name)
                else:
                    cust=User.objects.get(email=email)
                cust_serializer=CustomerSerializer(cust)
                return JsonResponse(cust_serializer.data,safe=False)      
                
            except User.DoesNotExist:
                return JsonResponse(None,safe=False)

                              
        customers=User.objects.all()
        cust_serializer=CustomerSerializer(customers,many=True)
        return JsonResponse(cust_serializer.data,safe=False)
    
       

def login(request):
    if request.method=="GET":
        return render(request,"Home_Module/signup.html")
    if request.method=="POST":
        username= request.POST['username']
        password= request.POST['password']  
        cust = auth.authenticate(username=username,password=password)
        if cust is None:
            errorMessage="Invalid Username or Password"
        elif  not cust.is_active:
            errorMessage="Your account is not active.please check your email address"
        else: 
            if 'is_seller' in request.POST: #checking if the request has come from seller center or not
                if not cust.is_seller:# if request has come from seller center ,checking if user is registered as seller
                    errorMessage="you are not registered as seller"
                else:
                    request.session['seller']=cust.username

                    try:                     
                        user=SellerDetail.objects.get(pk=cust.id)
                        return render(request,"Seller_Module/Home.html")
                    except SellerDetail.DoesNotExist:
                        return HttpResponseRedirect(reverse("Home_Module:SellerDetail"))
            else:
                if cust.is_seller:
                    errorMessage="you are not registered as Customer"
                else:
                    request.session['user']=cust.username
                    return render(request,"Home_Module/Home.html",context={"user":cust})
        if "is_seller" in request.POST:
            return render(request,"Seller_Module/SellerSignUp.html",context={"errorMessage":errorMessage})
        else:
            return render(request,"Home_Module/SignUp.html",context={"errorMessage":errorMessage})
    
def home(request):
    user=isUserLogin(request,'user')
    if user is not None:
        return render(request,"Home_Module/Home.html",context={"user":user})
    return render(request,"Home_Module/Home.html")

def forget(request):
    if request.method!="POST":
        return render(request,"Home_Module/ForgetPass.html")
    else:
        email=request.POST['email']
        if len(email)==0:
            messages.error(request,"Please enter your email")   
        else:     
            try:
                user=User.objects.get(email=email,is_staff=False)
                if not user.is_active:
                    messages.warning(request,"your account is not active .please check your inbox")
                else:
                    email_subject="Reset Password"
                    email_body=f'Hey {user.username}\n You have requested a password reset.Please click the following link to  reset your password\n'
                    send_link(email_subject,email_body,user,'reset_password')
                    messages.info(request,f'Please check your inbox.we have sent an email at {user.email} for password reset')
            except User.DoesNotExist:
                messages.error(request,"No such user exist")
        return HttpResponseRedirect(reverse("Home_Module:forget"))
            
def contact(request):
    return render(request,"Home_Module/contact.html")

def products(request):
    if request.method!="POST":
        return render(request,"Home_Module/products.html")
    else:
        return render(request,"Home_Module/productDetail.html")
        
def productDetail(request):
    return render(request,"Home_Module/productDetail.html")
def signup(request):
    if request.method=='GET':
        return render(request,"Home_Module/signup.html")
    
    elif request.method=='POST':
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password'] 
        user = User.objects.create_user(username=username, email=email)
        user.set_password(password)
        user.is_active = False
        user.is_social_user=False
        if 'is_seller' in request.POST:
            user.is_seller=True
        user.save()
        email_subject="Activate your account"
        email_body=f'Hey {user.username}\n Thanks for regestring on E_Mart.We are very delighted to have you.Please click the following link to activate your account\n'
        send_link(email_subject,email_body,user,'activate')
        message=f'Please check your inbox.we have sent an email at {user.email} for email verification'
        return render(request, 'Home_Module/generic_response.html',context={"message":message,"title":"Email verification"})


def logout(request,username):
    try:
        user=User.objects.get(username=username)
        return render(request,"Home_Module/logout.html",context={"user":user})
    except User.DoesNotExist:
        return HttpResponseRedirect(reverse("Home_Module:signup"))
def cust_logout(request):
    try:
        del request.session['user']
        return HttpResponseRedirect(reverse("Home_Module:home"))
    except KeyError:
        return HttpResponseRedirect(reverse("Home_Module:signup"))
    
def change_password(request):
    user=isUserLogin(request,'user')
    if user is None:
        return HttpResponseRedirect(reverse("Home_Module:signup"))
    if request.method=="GET": 
        return render(request,"Home_Module/change_password.html",context={"user":user})
    if request.method=="POST":
        passwd=request.POST['password']
        chkPasswd=auth.authenticate(username=user.username,password=passwd)
        if chkPasswd is None:
            messages.error(request, 'You have entered wrong password')
            return HttpResponseRedirect(reverse("Home_Module:update_password"))
        newPasswd=request.POST['newPasswd']
        user.set_password(newPasswd)
        user.save()
        update_session_auth_hash(request,user)
        messages.success(request,"your password has been changed")
        return HttpResponseRedirect(reverse("Home_Module:update_password"))


   

def reset_password_done(request):
    username=request.POST['username']
    passwd=request.POST['password']
    try:
        user=User.objects.get(username=username)
        user.set_password(passwd)
        user.save()
        update_session_auth_hash(request, user)
        messages.success(request,'your password has been reset.')
        return HttpResponseRedirect(reverse("Home_Module:signup"))
    except:
        messages.error(request,"something has went wrong.please try again later")
        return HttpResponseRedirect(reverse("Home_Module:reset_password_done"))
def reset_password(request,uidb64,token):
        id = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=id)

        if not token_generator.check_token(user, token):
            return render(request,"Home_Module/Home.html")
        return render(request,"Home_Module/reset_password.html",context={"username":user.username,"email":user.email})
        


class Verification(View):
     def get(self, request, uidb64, token):
        try:
            id = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=id)

            if not token_generator.check_token(user, token):
                messages.error(request,"this token has been expired")
                return render(request,"Home_Module/Home.html")

            if user.is_active:
                messages.info(request,"your account is already active")
                return redirect('/')
            user.is_active = True
            user.save()
            messages.success(request,"your account has been activated")
            return HttpResponseRedirect(reverse("Home_Module:signup"))

        except Exception as ex:
            pass

        return redirect('/')