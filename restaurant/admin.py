from django.contrib import admin
from .models import Category, Product, Reservation

# Register your models here.

admin.site.register([Category, Reservation]),
admin.site.register(Product)