from django.db import models
from Home_Module.models import User,Products

# Create your models here.
class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="order_user")
    is_paid=models.BooleanField(default=False)
    date=models.DateTimeField(verbose_name="placed on",auto_now_add=True)
    is_delivered=models.BooleanField(verbose_name="status",default=False)
    bill=models.PositiveIntegerField(default=0)
    

    def __str__(self):
        return f'{self.id}'
class OrderDetails(models.Model):
    products=models.ForeignKey(Products,on_delete=models.CASCADE,related_name="product")
    qty=models.PositiveIntegerField()
    order=models.ForeignKey(Order,on_delete=models.CASCADE,related_name="order")