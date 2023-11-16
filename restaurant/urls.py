from django.urls import path
from .views import homepage, Bookingpage, Aboutpage, Contactpage, Service, Teampage, Menupage, Testimonialpage


urlpatterns = [
    path("", homepage, name='home'),
    path('Booking/', Bookingpage, name='booking'),
    path('About/', Aboutpage, name='about'),
    path('Contact/', Contactpage, name='contact'),
    path('Service/', Service, name='service'),
    path('Teampage/', Teampage, name='team'),
    path('Menupage/', Menupage, name='menu'),
    path('Testimonialpage/', Testimonialpage, name='testimonial'),

]