from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('admin_panel')  
        else:
            messages.error(request, 'Invalid email or password')
    
    return render(request, 'login.html')


def admin_view(request):
    return render(request,'admin_panel.html')

# Create your views here.
