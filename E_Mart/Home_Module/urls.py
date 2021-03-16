from django.urls import path
from . import views
app_name='Home_Module'
urlpatterns=[
    path('',views.index,name="index"),
]