from django.db import models
from django import forms

class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="category_images")


    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name 



class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="product_image")
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)


class Menu(models.Model):
    name = models.CharField(max_length=100)
    dishes = models.ManyToManyField(Dish)  

    class Meta:
        verbose_name_plural = "Menu"

    def __str__(self):
        return self.name   


class Order(models.Model):
    dishes = models.ManyToManyField(Dish)
    email = models.EmailField()
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)  
    special_request = models.TextField(max_length=7000)


    class Meta:
        verbose_name_plural = "Order"

    def __str__(self):
        return self.name



class Reservation(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    party_size = models.IntegerField()  


    class Meta:
        verbose_name_plural = "Reservation"

    def __str__(self):
        return self.name     


# Create your models here.
