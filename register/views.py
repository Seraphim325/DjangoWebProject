from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login

# Create your views here.

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password1')

        if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
            return render(request, 'register/register.html', { "error": "User already exists"})

        user = User.objects.create_user(username=username, email=email, password=password)
        login(request, user)

        return redirect('home')


    return render(request, 'register/register.html')
