from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'map/index.html', {
        'map': 'this is a cool map u know'
    })
