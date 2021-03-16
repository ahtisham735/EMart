from django.shortcuts import render
from Home_Module import models

# Create your views here.
def index(request):
    if User.is_authenticated:
        request(request,"Home_Module/Home.html")
    return render(request,"Home_Module/index.html")
def home(request):
    return render(request,"Home_Module/Home.html")
def signup(request):
    return render(request,"Home_Module/signup.html")