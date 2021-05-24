from django.urls import path
from . import views
app_name="order"
urlpatterns=[
            path('myorders/',views.my_orders,name="my_orders"),
            path('order_details/<int:id>/',views.order_details,name="order_details"),
            path('order_delivered/<int:id>/',views.order_delivered,name="order_delivered"),
            path("orders/",views.seller_orders,name="seller_orders"),
            path('seller_order_details/<int:id>/',views.seller_orders_details,name="seller_orders_details"),

]