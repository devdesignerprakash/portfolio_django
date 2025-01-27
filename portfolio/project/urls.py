from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_view, name="home"),
    path('about/',views.about_view, name="about"),
    path('resume/',views.resume_view, name="resume"),
     path('contact/',views.contact_view, name="contact"),
    path('services/',views.services_view, name="services")
]