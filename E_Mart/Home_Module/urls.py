from django.urls import path
from . import views
app_name='Home_Module'
urlpatterns=[
    path('',views.home,name="home"),
    path('signup/',views.signup,name="signup"),
]