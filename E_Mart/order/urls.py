from django.urls import path
from . import views
app_name="order"
urlpatterns=[
            path('myorders/',views.my_orders,name="my_orders")
]