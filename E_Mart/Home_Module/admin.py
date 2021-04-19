from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from Home_Module.models import User,SellerDetail
# Register your models here.

class CustomAdmin(UserAdmin):
    list_display=('id','email','username','date_joined','last_login','is_staff','is_active','is_seller','is_social_user')
    search_fields=('email','username')
    readonly_fields=('id','date_joined','last_login')
    filter_horizontal=() 
    list_filter=()
    fieldsets=()
class SellerDetailRegister(admin.ModelAdmin):
    list_display=('pk','user','shop','cnic','phone','address','account_no')
    search_fields=('pk','cnic','account_no','user')
    readonly_fields=('pk','user','cnic','account_no')
    filter_horizontal=() 
    list_filter=()
    fieldsets=()
admin.site.register(User,CustomAdmin)
admin.site.register(SellerDetail,SellerDetailRegister)
