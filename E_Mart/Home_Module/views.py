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
from django.contrib.auth import update_session_auth_hash
from Home_Module.models import User
from .email_handler import token_generator,send_link
from django.utils.encoding import force_bytes,force_text,DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from .Serializer import CustomerSerializer
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
    if request.method=="POST":
        username= request.POST['username']
        password= request.POST['password']

            # if 'chkbox1' in request.POST:
            #      isChecked = request.POST['chkbox1']
            # else:
            #      isChecked = False
            # if request.session.get('is_Login', False):
            #       return HttpResponseRedirect("You are already login.") 
            # if isChecked:  
            #     request.session['is_Login'] = True     
        cust = auth.authenticate(username=username,password=password)
        if cust is None:
            errorMessage="Invalid Username or Password"
            return render(request,"Home_Module/SignUp.html",context={"errorMessage":errorMessage})
        if  not cust.is_active:
            errorMessage="Your account is not active.please check your email address"
            return render(request,"Home_Module/SignUp.html",context={"errorMessage":errorMessage})
        return render(request,"Home_Module/Home.html",context={"LoginCust":cust})
    
           
def home(request):
    return render(request,"Home_Module/Home.html")
 
# def signup(request):
#     isLog = request.session.get('is_Login', False)
#     if isLog:
#        return HttpResponse("You are already login.")
#     else:
#        return render(request,"Home_Module/signup.html")
def forget(request):
    if request.method!="POST":
        return render(request,"Home_Module/ForgetPass.html")
    else:
        email=request.POST['email']
        try:
            user=User.objects.get(email=email,is_staff=False)
            if not user.is_active:
                return render(request,"Home_Module/ForgetPass.html",context={"errorMessage":"Your account is not active.please activate your account first"})
            else:
                email_subject="Reset Password"
                email_body=f'Hey {user.username}\n You have requested a password reset.Please click the following link to  reset your password\n'
                send_link(email_subject,email_body,user,'reset_password')
                message=f'Please check your inbox.we have sent an email at {user.email} for password reset'
                return render(request, 'Home_Module/generic_response.html',context={"message":message,"title":"Reset Password"})

        except User.DoesNotExist:
            return render(request,"Home_Module/ForgetPass.html",context={"errorMessage":"User does not exist"})
            
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
        message=f'Please check your inbox.we have sent an email at {user.email} for email verification'
        return render(request, 'Home_Module/generic_response.html',context={"message":message,"title":"Email verification"})


def logout(request):
    return render(request,"Home_Module/logout.html")
def reset_password_done(request):
    username=request.POST['username']
    passwd=request.POST['password']
    try:
        user=User.objects.get(username=username)
        user.set_password(passwd)
        user.save()
        update_session_auth_hash(request, user)
        message='your password has been reset.'
        return render(request,"Home_Module/generic_response.html",context={"message":message,"title":"Password changed"})
    except User.DoesNotExist:
        return render(request,"Home_Module/generic_response.html",context={"message":"something has went wrong.Please try again later ","title":"Error"})
def reset_password(request,uidb64,token):
        id = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=id)

        if not token_generator.check_token(user, token):
            return render(request,"Home_Module/Home.html")
        return render(request,"Home_Module/reset_password.html",context={"username":user.username})
        


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