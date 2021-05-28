from django import forms
from django.db.models import fields
from django.forms import ModelForm
from Home_Module.models import ProductReview, Products
class AddProductForm(ModelForm):
    productName=forms.CharField(label="Product Name",
        widget=forms.TextInput(
            attrs={"placeholder":"Ex. Nikon Coolpix A300 Digital Camera","class":"input","autocomplete":"off"}
        )
    )
    brand=forms.CharField(label="Brand Name",
        widget=forms.TextInput(
            attrs={"placeholder":"Rolex","class":"input","autocomplete":"off"}
        )

    )
    description=forms.CharField(label="Description",required=True,
        widget=forms.Textarea(
            attrs={"autocomplete":"off","class":"input"}
        )

    )
    price=forms.CharField(label="Price",
        widget=forms.NumberInput(
            attrs={"class":"input","autocomplete":"off","min":"1"}
        )

    )
    quantity=forms.CharField(label="Quantity",
        widget=forms.NumberInput(
            attrs={"class":"input","autocomplete":"off","min":"1"}
        )

    )
    image1=forms.ImageField(
        label="Image1",required=False,
        widget=forms.FileInput(
            attrs={"class":"input","autocomplete":"off","accept":"image/*"}
        )
    )

    image2=forms.ImageField(
        label="Image2",required=False,
        widget=forms.FileInput(
            attrs={"class":"input","autocomplete":"off","accept":"image/*"}
        )
    )
    image3=forms.ImageField(
        label="Image3",required=False,
        widget=forms.FileInput(
            attrs={"class":"input","autocomplete":"off","accept":"image/*"}
        )
    )
    image4=forms.ImageField(
        label="Image4",required=False,
        widget=forms.FileInput(
            attrs={"class":"input","autocomplete":"off","accept":"image/*"}
        )
    )
 
    class Meta:
        model=Products
        exclude = ['sellerId']





    # #username=current_password=forms.HiddenInput(max_length=100,required=True,widget=forms.CharField(attrs={'hidden'}))
    # productName=forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={"placeholder":"Ex Red T-Shirt"}))
    # category=forms.CharField(max_length=100,required=True,widget=forms.Select(choices=category_choice))
    # #cnfrm_passwd=forms.CharField(max_length=100,required=True,widget=forms.PasswordInput(attrs={'placeholder':"confirm new password",'id':'cnfrm_passwd'}))
class ProductReviewForm(ModelForm):
    class Meta:
        model = ProductReview
        fields = ['subject', 'content', 'rate']