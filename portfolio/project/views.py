from django.shortcuts import render,redirect
from .models import Skill
from django.contrib import messages
from .models import ContactInquiry

def home_view(request):
    return render(request,'home.html')
def about_view(request):
    skills= Skill.objects.all()
    context={
        "skills":skills
    }
    return render(request,'about.html',context)

def resume_view(request):
    return render(request,'resume.html')

def services_view(request):
    return render(request,'services.html')
def contact_view(request):
    print(request.POST)
    success_message = None
    if request.method == "POST":
        email = request.POST.get('email')
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        inquiry = ContactInquiry(name=name, email=email, message=message, subject=subject)
        inquiry.save()
        success_message = "Your message has been sent. Thank you!"
    context={
        'success_message':success_message
    }
    return render(request, 'contact.html',context)

# Create your views here.
