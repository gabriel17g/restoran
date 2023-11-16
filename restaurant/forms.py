from django import forms
from .models import Category, Product



 
class Category(forms.Modelform):
    class Meta:
        model = Category
        fields = "a__all__"



class Product(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "price", "category", "special_request", "party_size"] 