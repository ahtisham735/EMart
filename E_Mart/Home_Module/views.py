from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from .Serializer import CustomerSerializer
from .models import Customer
# Create your views here.
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
        cust_data=JSONParser().parse(request) #converting data into json form
        cust_serializer=CustomerSerializer(data=cust_data) #using serializer to convert into model type
        if cust_serializer.is_valid():
            cust_serializer.save() # saving data into database
            
            return JsonResponse("Registered Successfully!!",safe=False)
        return JsonResponse("Failed to Register!!",safe=False)

# Create your views here.
def home(request):
    return render(request,"Home_Module/Home.html")
def signup(request):
    return render(request,"Home_Module/signup.html")