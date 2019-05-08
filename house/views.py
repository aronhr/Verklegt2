from django.shortcuts import render, get_object_or_404
from house.models import *


def index(request):
    p = PostalCodes.objects.all()
    context = {
        'houses': House.objects.all(),
        'types': HouseType.objects.all(),
        'towns': PostalCodes.objects.all(),
        'filter': {
            'postal_codes': request.POST.getlist('postal_codes'),
            'lyfta': request.POST.get('lyfta'),
            'rooms': request.POST.get('rooms')

        },
    }
    print(str(p[0].id) in request.POST.getlist('postal_codes'))
    print("req", request)
    print("post", request.POST.get('types'))
    print("post", request.POST.getlist('postal_codes'))

    print("get", request.GET)
    print("body", request.body)
    return render(request, 'house/index.html', context)


def get_house_by_id(request, id):
    return render(request, 'house/house.html', {
        'house': get_object_or_404(House, pk=id),
    })


