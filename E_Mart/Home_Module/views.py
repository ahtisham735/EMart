from django.views import View
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from .Serializer import CustomerSerializer
from .models import Customer
from django import forms
from django.conf import settings
from verify_email.email_handler import send_verification_email
from django.core.mail import send_mail
from django.urls import reverse
from django.utils.encoding import force_bytes,force_text,DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from .tokenGenrator import token_generator

# Create your views here.
class MyForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields=['email','username','password']

@csrf_exempt
def cust_api(request,name=''):
    if request.method=="GET":
        if len(name)!=0:
            try:
                cust=Customer.objects.get(pk=name)
                cust_serializer=CustomerSerializer(cust)
                return JsonResponse(cust_serializer.data,safe=False)      
            except Customer.DoesNotExist:
                return JsonResponse(None,safe=False)
                              
        customers=Customer.objects.all()
        cust_serializer=CustomerSerializer(customers,many=True)
        return JsonResponse(cust_serializer.data,safe=False)
    elif request.method=="POST":
        f=MyForm(request.POST)
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        cust=Customer(email=email,username=username,password=password)
        cust.is_active=False
     
        if f.is_valid():
            inactive_user = send_verification_email(request, MyForm(request.POST))
        # uidb64=urlsafe_base64_encode(force_bytes(cust.pk))
        # domain=get_current_site(request).domain
        # link=reverse('activate',kwargs={'uidb64':uidb64,'token':token_generator.make_token(cust)})
        # activate_url=f'http://{domain}{link}'
        # if f.is_valid():
        #     send_mail(
        #     'Subject here',
        #     f'{activate_url}',
        #     settings.EMAIL_HOST_USER,
        #     [email],
        #     fail_silently=False,
        # )
    
    return HttpResponseRedirect('/')
       

# Create your views here.
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
           
        
def home(request):
    isLogin = request.session.get('is_Login', False)
    if isLogin:
        return render(request,"Home_Module/Home.html")
    else:
        return render(request,"Home_Module/signup.html")
 
def signup(request):
    isLog = request.session.get('is_Login', False)
    if isLog:
       return HttpResponse("You are already login.")
    else:
        return render(request,"Home_Module/signup.html")
def forget(request):
    return render(request,"Home_Module/ForgetPass.html")
def contact(request):
    return render(request,"Home_Module/contact.html")
class Verification(View):
    def get(request,uidb64,token):
        return redirect('/')



