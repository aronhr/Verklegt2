from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'login/index.html', {
        'login': 'Innskráning'
    })


def register(request):
    return render(request, 'login/register.html', {
        'register': 'registerpage'
    })


def forgot(request):
    return render(request, 'login/forgot.html', {
        'forgot': 'forgotpage'
    })
