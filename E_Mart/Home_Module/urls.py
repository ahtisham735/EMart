from django.urls import path
from .import views
from django.contrib.auth import views as auth_views
app_name='Home_Module'
urlpatterns=[
    path('',views.home,name="home"),
    path('login/', views.login,name="login"),
    path('signup/',views.signup,name="signup"),
    path('forget',views.forget,name="forget"),
    path('customer/',views.cust_api,name="cust_api"),
    path('customer/<str:name>',views.cust_api,name="cust_api"),
   
    path('contact',views.contact,name="contact"),
    path('logout/',views.logout,name="account_logout"),
 
]