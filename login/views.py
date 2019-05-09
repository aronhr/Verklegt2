from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from login.forms.forms import SignUpForm

# Create your views here.


def index(request):
    return render(request, 'login/index.html', {
        'login': 'Innskráning'
    })


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login-index')
    else:
        form = SignUpForm()
    return render(request, 'login/register.html', {'forms': form})


def forgot(request):
    return render(request, 'login/forgot.html', {
        'forgot': 'forgotpage'
    })
