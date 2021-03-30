from django.views import View
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from django import forms
from django.urls import reverse
from django.contrib import auth
from django.conf import settings
from Home_Module.models import User
from .email_handler import token_generator,send_link
from django.utils.encoding import force_bytes,force_text,DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from .Serializer import CustomerSerializer
# Create your views here.


@csrf_exempt
def cust_api(request,name=''):
    if request.method=="GET":
        if len(name)!=0:
            try:
                cust=User.objects.get(pk=name)
                cust_serializer=CustomerSerializer(cust)
                return JsonResponse(cust_serializer.data,safe=False)      
            except User.DoesNotExist:
                return JsonResponse(None,safe=False)
                              
        customers=User.objects.all()
        cust_serializer=CustomerSerializer(customers,many=True)
        return JsonResponse(cust_serializer.data,safe=False)
    
       

def login(request):
    if request.method=="POST":
        username= request.POST['username']
        password= request.POST['password']
        
        try:
            if 'chkbox1' in request.POST:
                 isChecked = request.POST['chkbox1']
            else:
                 isChecked = False
            if request.session.get('is_Login', False):
                  return HttpResponse("You are already login.") 
            if isChecked:  
                request.session['is_Login'] = True
            cust = Customer.objects.get(username=username,password=password)
            return render(request,"Home_Module/Home.html",context={"LoginCust":cust})
        except Customer.DoesNotExist:
            ErrorMessage="Login faild!,Invalid Username or Password"
            return render(request,"Home_Module/SignUp.html",context={"ErrorMessage":ErrorMessage})
           
        
# def home(request):
#     isLogin = request.session.get('is_Login', False)
#     if isLogin:
#         return render(request,"Home_Module/Home.html")
#     else:
#         return render(request,"Home_Module/signup.html")
 
# def signup(request):
#     isLog = request.session.get('is_Login', False)
#     if isLog:
#        return HttpResponse("You are already login.")
#     else:
#         return render(request,"Home_Module/signup.html")
def forget(request):
    return render(request,"Home_Module/ForgetPass.html")
def contact(request):
    return render(request,"Home_Module/contact.html")

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
        user.save()
        email_subject="Activate your account"
        email_body=f'Hey {user.username}\n Thanks for regestring on E_Mart.We are very delighted to have you.Please click the following link to activate your account\n'
        send_link(email_subject,email_body,user,'activate')
        return render(request, 'Home_Module/email_verification.html',context={"email":user.email})
    
def home(request):
    return render(request,"Home_Module/Home.html")
def logout(request):
    return render(request,"Home_Module/logout.html")


class Verification(View):
     def get(self, request, uidb64, token):
        try:
            id = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=id)

            if not token_generator.check_token(user, token):
                return render(request,"Home_Module/Home.html")

            if user.is_active:
                return redirect('/')
            user.is_active = True
            user.save()
            return redirect('/')

        except Exception as ex:
            pass

        return redirect('/')