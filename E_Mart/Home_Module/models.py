from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
# Create your models here.

#for creating users
class UserManager(BaseUserManager):
    def create_user(self,username,email,password=None):
        if not username:
            raise ValueError("User must have a username")
        if not email:
            raise ValueError("User must have an email address")
        user=self.model(
            email=self.normalize_email(email),
            username=username,
        )
    
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,username, email, password):
        user=self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
        )
        user.is_admin=True
        user.is_staff=True
        user.is_superuser=True
        is_social_user=False
        user.save(using=self._db)
        return user
# overriding/customizing default django User
class User(AbstractUser):
    email=models.EmailField(verbose_name="email",max_length=50,unique=False)
    username=models.CharField(max_length=50,unique=True,verbose_name="username")
    date_joined=models.DateTimeField(verbose_name="date joined",auto_now_add=True)
    last_login=models.DateTimeField(verbose_name="last login",auto_now=True)
    is_admin=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)
    is_social_user=models.BooleanField(default=True)

    objects= UserManager()
    USERNAME_FIELD="username"
    REQUIRED_FIELDS=['email']

    def __str__(self):
        return self.username
    def has_perm(self,perm,obj=None):
        return self.is_admin
    def has_module_perms(self,app_Label):
        return True


class SellerDetail(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True, blank=True)
    shop=models.CharField(max_length=255)
    phone=models.CharField(max_length=11)
    cnic=models.CharField(max_length=13,unique=True)
    address=models.CharField(max_length=255)
    account_no=models.CharField(max_length=14)
    def __str__(self):
        return self.cnic

category_choice=[('men',"Men's Fashion"),('women',"Women's Fashion"),('WBJ',"Watches,Bags & Jewelery")]
class Products(models.Model):
    sellerId=models.ForeignKey(User,on_delete=models.CASCADE,related_name="sellerId",null=True, blank=True)
    productName=models.CharField(max_length=255,blank=False)  
    brand=models.CharField(max_length=255,blank=False)
    price=models.PositiveIntegerField(blank=False)
    quantity=models.PositiveIntegerField(blank=False)
    image1=models.ImageField(upload_to='products/images',default=None)
    image2=models.ImageField(upload_to='products/images',default=None)
    image3=models.ImageField(upload_to='products/images',default=None)
    image4=models.ImageField(upload_to='products/images',default=None)
    category=models.CharField(max_length=255,choices=category_choice)
    description=models.CharField(max_length=255,blank=False,default=None)
    def __str__(self):
        return self.productName
class Cart(models.Model):
    user=models.ForeignKey(User,related_name="user",on_delete=models.CASCADE,null=True, blank=True)
    product=models.ForeignKey(Products,on_delete=models.CASCADE,related_name="products",null=True, blank=True)
    qty=models.PositiveIntegerField(default=1)











  

