from django.db import models

# Create your models here.
class Customer(models.Model):
    email=models.EmailField(unique=False,null=False)
    username=models.CharField(max_length=50,primary_key=True)
    password=models.CharField(max_length=20)