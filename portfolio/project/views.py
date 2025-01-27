from django.shortcuts import render

def home_view(request):
    return render(request,'home.html')



def about_view(request):
    return render(request,'about.html')

def resume_view(request):
    return render(request,'resume.html')

def services_view(request):
    return render(request,'services.html')

def contact_view(request):
    return render(request,'contact.html')

# Create your views here.
