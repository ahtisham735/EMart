from django.contrib import admin
from Home_Module.models import *

# Register your models here.
class RegisterCustomer:
    list_display=("email","username","password")
