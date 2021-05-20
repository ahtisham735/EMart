from django.db import models
from Home_Module.models import User

# Create your models here.
class ShippingDetail(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    email=models.EmailField(verbose_name="email",max_length=255,unique=False)
    address=models.CharField(max_length=255)
    contact=models.CharField(max_length=11)
    country=models.CharField(max_length=255,default="")
    city=models.CharField(max_length=255)
    zip_code=models.CharField(max_length=5)