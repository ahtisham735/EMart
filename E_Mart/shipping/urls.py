from django.urls import path
from . import views
app_name="shipping"
urlpatterns=[
            path('shipping/',views.shipping_detail,name="shipping_detail"),
            path('shipping/<str:chk>',views.shipping_detail,name="shipping_detail"),
           
        ]