from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

# Create your views here.


def index(request):
    return render(request, 'login/index.html', {
        'login': 'loginpage'
    })


def register(request):
    if request == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login-index')
    return render(request, 'login/register.html', {
        'form': UserCreationForm()
    })


def forgot(request):
    return render(request, 'login/forgot.html', {
        'forgot': 'forgotpage'
    })
