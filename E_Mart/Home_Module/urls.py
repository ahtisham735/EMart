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
    path('productDetail/<int:id>',views.productDetail,name="productDetail"),
    path('search',views.search,name="search"),
    path('cart/',views.cart,name="cart"),
    path('checkout/',views.checkout,name="checkout"),
    path('logout/<str:username>',views.logout,name="account_logout"),
    path("reset_password_done",views.reset_password_done,name="reset_password_done"),
    path('update_password/<str:username>',views.change_password,name="update_password"),
    path("cust_logout",views.cust_logout,name="cust_logout"),
    path("Seller_center",Seller_views.seller_center,name="seller_center"),
    path("SellerDetail/",Seller_views.seller_detail,name="SellerDetail"),
    path("seller_logout",Seller_views.seller_logout,name="seller_logout"),
    path("add_product",Seller_views.add_product,name="add_product"),
    path('SellerDetail',Seller_views.seller_detail,name="SellerDetail"),
    path("seller_logout",Seller_views.seller_logout,name="seller_logout"),
    path('SellerDetailUpdate',Seller_views.seller_detail_update,name="SellerDetailUpdate"),
    path("edit_product/<str:pk>/",Seller_views.edit_product,name="edit_product"),
    path("delete_product/<str:pk>/",Seller_views.delete_product,name="delete_product"),
    path("delete_cart/<int:id>",views.delete_cart,name="delete_cart")


    
 
]