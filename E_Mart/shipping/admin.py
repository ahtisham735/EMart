from django.contrib import admin
from .models import ShippingDetail
# Register your models here.
class ShippingDetailAdmin(admin.ModelAdmin):
    list_display=('pk','user','email')
    search_fields=('pk','user')
admin.site.register(ShippingDetail,ShippingDetailAdmin)