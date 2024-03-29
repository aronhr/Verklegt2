from profiles.models import Profile, UserBankInfo
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from login.forms.reg_form import SignUpForm


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
            b = UserBankInfo(user=user)
            b.save()
            p = Profile(dob='2000-01-01', user=user)
            p.save()
            login(request, user)
            return redirect('login-index')
    else:
        form = SignUpForm()
    return render(request, 'login/register.html', {'form': form})


def forgot(request):
    if request.method == 'POST':
        data = 'Tölvupóstur sentur'
    else:
        data = ''
    return render(request, 'login/forgot.html', {
        'forgot': data
    })
