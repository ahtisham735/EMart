from django.contrib import admin
from .models import Order,OrderDetails

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display=('pk','user','is_paid','date','bill','is_delivered')
    search_fields=('pk','user')
class OrderDetailsAdmin(admin.ModelAdmin):
    list_display=('pk','products','qty','order')
    search_fields=('pk','order')
admin.site.register(Order,OrderAdmin)
admin.site.register(OrderDetails,OrderDetailsAdmin)