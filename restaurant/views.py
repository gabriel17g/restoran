from django.shortcuts import render, redirect
from .models import Category, Product
from django.http import HttpResponse
from django.contrib import messages 

def homepage(request):
    all_categories = Category.objects.all()
    context = {"all_categories": all_categories}
    return render(request, "restaurant/index.html", context)


def Bookingpage(request):
    return render(request, 'restaurant/booking.html')

def Aboutpage(request):
    return render(request, 'restaurant/about.html')

def Contactpage(request):
    return render(request, 'restaurant/contact.html')

def Service(request):
    return render(request, 'restaurant/service.html')

def Teampage(request):
    return render(request, 'restaurant/team.html')

def Testimonialpage(request):
    return render(request, 'restaurant/testimonial.html')

def Menupage(request):
    return render(request, 'restaurant/menu.html')




def contact(request):
    if request.method == "POST":
        form = Category(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            return HttpResponse("Something isn't right")
    else:
        form = Category()
    # context = {"form": form}    
    return render(request, "restaurant/contact.html", context={"form": form})





def booking(request):
    if request.method == "POST":
        form = Product(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            return HttpResponse("Something isn't right")
    else:
        form = Product()
        return render(request, "restauranrt/booking.html", {"form": form})

        

# Create your views here.
