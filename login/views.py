from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.shortcuts import render, redirect

# Create your views here.

def login_view(request):
    if request.method == 'POST':
        input = request.POST.get('login')
        password = request.POST.get('password')

        user = None

        try:
            user = User.objects.get(username=input)
        except User.DoesNotExist:
            try:
                user = User.objects.get(email=input)
            except User.DoesNotExist:
                pass

        if user and check_password(password, user.password):
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login/login.html', { "error": "Incorrect username or password"})

    return render(request, 'login/login.html')