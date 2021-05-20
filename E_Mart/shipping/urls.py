from django.urls import path
from . import views
app_name="shipping"
urlpatterns=[
            path('shipping/',views.shipping_detail,name="shipping_detail"),
            path('shippingUpdate',views.update_shipping_detail,name="update_details"),
        ]