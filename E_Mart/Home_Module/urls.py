from django.urls import path
from .import views,Seller_views
from django.contrib.auth import views as auth_views
app_name='Home_Module'
urlpatterns=[
    path('',views.home,name="home"),
    path('login/', views.login,name="login"),
    path('signup/',views.signup,name="signup"),
    path('forget',views.forget,name="forget"),
    path('customer/',views.cust_api,name="cust_api"),
    path('customer/username=<str:name>',views.cust_api,name="cust_api"),
    path('customer/email=<str:email>',views.cust_api,name="cust_api"),
    path('contact',views.contact,name="contact"),
    path('products',views.products,name="products"),
    path('productDetail',views.productDetail,name="productDetail"),
    path('<str:username>logout/',views.logout,name="account_logout"),
    path("reset_password_done",views.reset_password_done,name="reset_password_done"),
    path('update_password',views.change_password,name="update_password"),
    path("cust_logout",views.cust_logout,name="cust_logout"),
    path("Seller_center",Seller_views.seller_center,name="seller_center"),
    path("SellerDetail",Seller_views.seller_detail,name="SellerDetail"),
  

    
 
]