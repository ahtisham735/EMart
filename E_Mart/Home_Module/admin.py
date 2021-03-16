from django.contrib import admin
from Home_Module.models import *

# Register your models here.
class RegisterCustomer(admin.ModelAdmin):
    list_display=("email","username","password")

admin.site.register(Customer,RegisterCustomer)
